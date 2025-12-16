from classes.temporada import Temporada
from classes.episodio import Episodio
from classes.serie import Serie
from classes.filme import Filme
from classes.historico import Historico
from classes.registro_visualizacao import RegistroVisualizacao
from datetime import datetime
from datetime import date
from classes.usuario import Usuario
from classes.lista_personalizada import ListaPersonalizada
import json
import os

CAMINHO = "data/midias.json"
CAMINHO_USUARIOS = "data/usuarios.json"

def salvar_midias(lista_midias):
    lista_dados = []
    for midia in lista_midias:
        lista_dados.append(midia.gerar_dicionario())
    verifica_pasta = os.path.dirname(CAMINHO)
    os.makedirs(verifica_pasta, exist_ok=True)
    try:
        with open(CAMINHO, "w", encoding="utf-8") as arquivo:
            json.dump(lista_dados, arquivo, indent=4, ensure_ascii=False)
        print("💾 Dados atualizados no arquivo.")
    except Exception as e:
        print(f"Erro ao salvar{e}")
    
def carregar_midias():
    print("SISTEMA: Carregando dados do sistema")
    try:
        with open(CAMINHO, 'r', encoding='utf-8') as arquivo:
            dados_lidos = json.load(arquivo)
            catalogo = []
            for midia in dados_lidos:
                if midia['tipo'] == "FILME":
                    filme = Filme(
                        midia['id'],
                        midia['titulo'],
                        midia['genero'],
                        midia['ano'],
                        midia['duracao_minutos'],
                        midia['classificacao_indicativa'],
                        midia['elenco'],
                        midia['status'],
                        midia.get('notas', [])
                        )
                    catalogo.append(filme)
                elif midia['tipo'] == "SÉRIE":
                    obj_temporadas = []
                    for temporada in midia['temporadas']:
                        obj_episodios = []
                        for episodio in temporada['episodios']:
                            data_obj = datetime.fromisoformat(episodio['data_lancamento'])
                            episodio = Episodio(
                                episodio['numero_episodio'],
                                episodio['titulo'],
                                episodio['duracao_minutos'],
                                data_obj,
                                episodio['status'],
                                episodio['notas']
                            )
                            obj_episodios.append(episodio)
                        temporada = Temporada(
                            temporada['numero_temporada'],
                            temporada['status'],
                            obj_episodios     
                        )
                        obj_temporadas.append(temporada)
                        
                    serie = Serie(
                        midia['id'],
                        midia['titulo'],
                        midia['genero'],
                        midia['ano'],
                        midia['duracao_minutos'],
                        midia['classificacao_indicativa'],
                        midia['elenco'],
                        midia['status'],
                        midia['notas'],
                        obj_temporadas
                    )
                    catalogo.append(serie)
            print("SISTEMA: Dados carregados com sucesso")
            return catalogo

    except FileNotFoundError:
        return []
    
def salvar_usuarios(lista_usuarios):
    dados_formatados = []
    for usuario in lista_usuarios:
        dados_formatados.append(usuario.criar_dicionario())
    
    os.makedirs(os.path.dirname(CAMINHO_USUARIOS), exist_ok=True)
    
    with open(CAMINHO_USUARIOS, 'w', encoding='UTF-8') as arquivo:
        json.dump(dados_formatados, arquivo, indent=4, ensure_ascii=False)
    print("Usuários salvos com sucesso!")

def carregar_usuarios(catalogo, config_sistema):
    lista_usuarios = []
    try:
        with open(CAMINHO_USUARIOS, 'r', encoding='UTF-8') as arquivo:
            dados_brutos = json.load(arquivo)
            
            for u_dict in dados_brutos:
                if 'historico' in u_dict and isinstance(u_dict['historico'], dict):
                    dados_hist = u_dict['historico']
                    obj_historico = Historico(id_historico=dados_hist.get('id'))
                    
                    for reg in dados_hist.get('registros', []):
                        midia_obj = None
                        for m in catalogo:
                            if m.titulo == reg['midia_titulo']:
                                midia_obj = m
                                break
                        
                        if midia_obj:
                            data_reg = datetime.fromisoformat(reg['data'])
                            novo_reg = RegistroVisualizacao(midia_obj, reg['status'], reg['nota'], data_reg)
                            obj_historico.registros.append(novo_reg)
                else:
                    obj_historico = Historico()

                listas_obj = []
                for l_dict in u_dict['listas']:
                    midias_lista = []
                    for titulo in l_dict['midias']:
                        for m in catalogo:
                            if m.titulo == titulo:
                                midias_lista.append(m)
                                break
                    data_lista = date.fromisoformat(l_dict['data_criacao'])
                    listas_obj.append(ListaPersonalizada(l_dict['id'], l_dict['nome'], l_dict['descricao'], data_lista, midias_lista))

                novo_user = Usuario(
                    u_dict['id'], u_dict['nome'], u_dict['email'], config_sistema,
                    listas=listas_obj,
                    historico=obj_historico
                )
                lista_usuarios.append(novo_user)

        return lista_usuarios
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"Erro ao carregar usuários: {e}")
        return []
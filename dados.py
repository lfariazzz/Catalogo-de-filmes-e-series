from classes.temporada import Temporada
from classes.episodio import Episodio
from classes.serie import Serie
from classes.filme import Filme
from datetime import datetime
from datetime import date
from classes.usuario import Usuario
from classes.lista_personalizada import ListaPersonalizada
import json
import os

CAMINHO = "data/midias.json"

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
    nova_lista = ListaPersonalizada.criar_dicionario()
    
    for usuario in lista_usuarios:
        dicionario_usuario = usuario.criar_dicionario()
        dados_formatados.append(nova_lista)
    
    verifica_pasta = os.path.dirname("data/usuarios.json")
    os.makedirs(verifica_pasta, exist_ok=True)

    try:
        with open("data/usuarios.json", 'w', encoding='UTF-8') as arquivo:
            json.dump(dados_formatados, arquivo, indent=4, ensure_ascii=False)
        print("Usuários salvos com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar usuários: {e}")

def carregar_usuarios(catalogo, config_sistema):
    lista_usuarios_formatada = []
    
    try:
        with open("data/usuarios.json", 'r', encoding='UTF-8') as arquivo:
            dados_brutos = json.load(arquivo)
            
            for usuario_dict in dados_brutos:
                
                listas_obj = []
                for lista in usuario_dict['listas']:
                    midias = []
                    for titulo in lista['midias']:
                        for midia_original in catalogo:
                            if midia_original.titulo == titulo:
                                midias.append(midia_original)
                                break
                    
                    data_obj = date.fromisoformat(lista['data_criacao'])
                    
                    nova_lista = ListaPersonalizada(
                        lista['id'],
                        lista['nome'],
                        lista['descricao'],
                        data_obj,
                        midias
                    )
                    listas_obj.append(nova_lista)

                historico_obj = []
                if 'historico' in usuario_dict:
                    for item_hist in usuario_dict['historico']:
                    
                        midia_encontrada = None
                        for m in catalogo:
                            if m.titulo == item_hist['midia_titulo']:
                                midia_encontrada = m
                                break
                        
                        data_hist = date.fromisoformat(item_hist['data_conclusao'])
                        
                        if midia_encontrada:
                            historico_obj.append({
                                "midia": midia_encontrada,
                                "data_conclusao": data_hist
                            })

                novo_usuario = Usuario(
                    usuario_dict['id'],
                    usuario_dict['nome'],
                    usuario_dict['email'],
                    config_sistema,
                    listas=listas_obj,
                    historico=historico_obj
                )
                lista_usuarios_formatada.append(novo_usuario)
                
        return lista_usuarios_formatada

    except FileNotFoundError:
        print("Arquivo de usuários não encontrado. Iniciando vazio.")
        return []
    except Exception as e:
        print(f"Erro ao ler usuários: {e}")
        return []
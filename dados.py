from classes.temporada import Temporada
from classes.episodio import Episodio
from classes.serie import Serie
from classes.filme import Filme
from datetime import date
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
        print("Dados salvos.")
    except Exception as e:
        print(f"Erro ao salvar{e}")
    
def carregar_midias():
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
                        midia['notas']
                        )
                    catalogo.append(filme)
                elif midia['tipo'] == "SÉRIE":
                    obj_temporadas = []
                    for temporada in midia['temporadas']:
                        obj_episodios = []
                        for episodio in temporada['episodios']:
                            data_obj = date.fromisoformat(episodio['data_lancamento'])
                            episodio = Episodio(
                                episodio['numero_episodio'],
                                episodio['titulo'],
                                episodio['duracao_minutos'],
                                data_obj,
                                episodio['status'],
                                episodio['nota']
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
            return catalogo

    except FileNotFoundError:
        return []

def criar_midia(self):
    pass

def ler_midia(self):
    pass

def atualizar_midia(self):
    pass

def deletar_midia(self):
    pass
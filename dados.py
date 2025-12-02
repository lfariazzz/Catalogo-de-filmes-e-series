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
        
def criar_midia(self):
    pass

def ler_midia(self):
    pass

def atualizar_midia(self):
    pass

def deletar_midia(self):
    pass
from classes.midia import Midia
from datetime import date
from classes.serie import Serie
from classes.filme import Filme
import json

def exibir_menu():
    print("-" * 50, "🔥🎬ForgeFlix🎬🔥", "-" * 50)
    print("Seja bem vindo ao ForgeFlix, seu catálogo de filmes e séries desenvolvido por Levi Farias.")
    print("Estes são os comando implementados para controle por CLI:")
    print("-" * 30, "🎞️Comando de mídia🎞️", "-" * 30)
    print("1. Exibir lista com as mídias disponíveis no catálogo")
    print("2. Adicionar mídia ao catálogo")
    print("3. Avaliar mídia")
    print("4. Relatório de mídias")
    print("-" * 30, "📺Comandos de Série📺", "-" * 30)
    print("5. Adicionar episódio de uma temporada de uma série")
    print("6. Alterar status de visualização")
    print("-" * 30, "👤Comandos de Usuário👤", "-" * 30)
    print("7. Criar Lista personalizada de um Usuário")
    print("8. Adicionar mídia à lista")
    print("0. Encerrar programa")
    decisao = input("O que deseja fazer? ")

def exibir_catalogo(catalogo):
    print("-" * 30, "Este é o catálogo disponível no ForgeFlix", "-" * 30)
    if not catalogo:
        print("🚫NENHUMA MÍDIA CADASTRADA🚫")
    else:
       for midia in catalogo:
            print(midia)

def adicionar_midia(catalogo):
    print("Este é modo de adição de mídias e séries do ForgeFlix:")

    #Decisão do tipo de mídia e geração do ID
    filme_ou_serie = int(input("Deseja criar um (1) filme ou uma (2) série? "))
    decisao_midia = None
    if filme_ou_serie == 1:
        decisao_midia = "FILME"
        qtd_filmes = len([m for m in catalogo if isinstance(m, Filme)])
        id = qtd_filmes + 1
    elif filme_ou_serie == 2:
        decisao_midia = "SÉRIE"
        qtd_series = len([m for m in catalogo if isinstance(m, Serie)])
        id = qtd_series + 1
    else:
        print("Opção inválida")

    titulo = str(input("Digite o título da mídia: "))
    nome = titulo

    genero = str(input("""Digite o gênero da mídia:
DISPONÍVEIS:
Ação
Aventura
Comédia
Drama
Ficção Científica
Terror
Romance
Suspense
Documentário
Animação
Fantasia
Policial
Musical
DIGITE: """))

    ano = int(input("Digite o ano da mídia: "))

    duracao_minutos = float(input("Digite a duração (em minutos) da mídia: "))

    classificacao_indicativa = input("""Digite a classificação indicativa da mídia:
L
10
12
14
16
18
DIGITE: """)

    #Decisão do elenco:
    elenco_ou_nao = int(input("Deseja adicionar o elenco da mídia? \n (1) Sim \n (2) Não \n DIGITE: "))
    if elenco_ou_nao == 2:
        elenco = []    
    elif elenco_ou_nao == 1:
        elenco = []
        artista = str(input("Digite o nome do primeiro artista: \n"))
        elenco.append(artista)
        print("Artista Adicionado!")
        continuar_elenco = int(input("Deseja adicionar mais artistas ao elenco? \n Se sim digite 1: "))
        while continuar_elenco == 1:
            artista = str(input("Digite o nome do outro artista artista: \n"))
            elenco.append(artista)
            print("Artista Adicionado!")
            continuar_elenco = int(input("Deseja adicionar mais artistas ao elenco? \n Se sim digite 1: "))

    else:
        print("Digite uma opção válida.")

    #Criação da mídia
    nome = Midia(id, titulo, decisao_midia, genero, ano, duracao_minutos, classificacao_indicativa, elenco, "NÃO ASSISTIDO" )
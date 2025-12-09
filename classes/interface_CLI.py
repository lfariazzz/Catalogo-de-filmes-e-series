from classes.midia import Midia
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

def adicionar_midia():
    print("Este é modo de adição de mídias e séries do ForgeFlix:")
    filme_ou_seroe = input(int("Deseja criar um (1) filme ou uma (2) série? "))
    decisao_midia = None
    if filme_ou_seroe == 1:
        decisao_midia = "FILME"
    elif filme_ou_seroe == 2:
        decisao_midia = "SÉRIE"
    else:
        print("Opção inválida")
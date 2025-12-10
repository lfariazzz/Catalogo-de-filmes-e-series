from classes.midia import Midia
from datetime import date
from classes.serie import Serie
from classes.filme import Filme
from classes.episodio import Episodio
import dados
import json

def exibir_menu():
    print("-" * 43, "🔥🎬ForgeFlix🎬🔥", "-" * 43)
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

def rodar_sistema():
    print("🔄 Carregando dados...")
    catalogo = dados.carregar_midias()
    print(f"✅ {len(catalogo)} mídias carregadas na memória.")

    exibir_menu()

    while True:
        entrada = (input("O que deseja fazer? "))        
        if entrada.upper() == "MENU":
            exibir_menu()
            continue
        try:
            decisao = int(entrada)
        except ValueError:
            print("❌ Comando inválido. Digite um número ou 'MENU'.")
            continue

        if decisao == 0:
            encerrar_programa()
            break
        elif decisao == 1:
            exibir_catalogo(catalogo)
        elif decisao == 2:
            adicionar_midia(catalogo)
        elif decisao == 3:
            avaliar_midia(catalogo)
        
        else:
            print("Digite uma opção válida")

        print("Digite uma nova opção ou digite menu para exibir o menu novamente")

def exibir_catalogo(catalogo):
    print("-" * 30, "Este é o catálogo disponível no ForgeFlix", "-" * 30)
    if not catalogo:
        print("🚫NENHUMA MÍDIA CADASTRADA🚫")
    else:
       for midia in catalogo:
            print(midia)

def adicionar_midia(catalogo):
    print("-" * 30, "Este é modo de adição de mídias e séries do ForgeFlix:", "-" * 30)

    #Decisão do tipo de mídia e geração do ID
    filme_ou_serie = int(input("Deseja criar um (1) filme ou uma (2) série? "))
    decisao_midia = None
    if filme_ou_serie == 1:
        decisao_midia = "FILME"
        qtd_filmes = len([m for m in catalogo if isinstance(m, Filme)])
        id = int(f"10{qtd_filmes + 1}")
    elif filme_ou_serie == 2:
        decisao_midia = "SÉRIE"
        qtd_series = len([m for m in catalogo if isinstance(m, Serie)])
        id = int(f"20{qtd_series + 1}")
    else:
        print("❌ Opção inválida.")
        return 

    #Definição do título
    titulo = str(input("Digite o título da mídia: "))

    #Definição do gênero
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
    
    #Definição do ano
    ano = int(input("Digite o ano da mídia: "))

    #Definição da duração (CASO SEJA FILME)
    if decisao_midia == "FILME":
        duracao_minutos = int(input("Digite a duração (em minutos) da mídia: "))
    elif decisao_midia == "SÉRIE":
        duracao_minutos = 0

    #Definição da classificação
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
    #Filme
    if decisao_midia == "FILME":
        nova_midia = Filme(id, titulo, genero, ano, duracao_minutos, classificacao_indicativa, elenco, "NÃO ASSISTIDO")
    #Série
    elif decisao_midia == "SÉRIE":
        nova_midia = Serie(id, titulo, genero, ano, duracao_minutos, classificacao_indicativa, elenco, "NÃO ASSISTIDO")
    #Salvamento no json
    catalogo.append(nova_midia)
    dados.salvar_midias(catalogo)
    print("Mídia adicionada ao catálogo!")

def avaliar_midia(catalogo):
    for midia in catalogo:
        print(f"ID: {midia.id:<5} | {midia.tipo:<7} | {midia.ano} | {midia.titulo}")
    selecao_encontrada = False
    selecao_midia = int(input("Digite o ID da mídia que você quer avaliar: "))
    for midia in catalogo:
        if midia.id == selecao_midia:
            selecao_encontrada = True
            if midia.tipo == "FILME":
                nota = float(input("Digite a nota que deseja adicionar: "))
                midia.avaliar_filme(nota)
                dados.salvar_midias(catalogo)
            elif midia.tipo == "SÉRIE":
                escolha_temporada = int(input(f"Qual temporada de {midia.titulo} você quer avaliar um episódio: "))
                temporada_encontrada = False
                for temporada in midia.temporadas:
                    if escolha_temporada == temporada.numero_temporada:
                        temporada_encontrada = True
                        escolha_episodio = int(input(f"Qual episódio da {escolha_temporada}a de {midia.titulo} você quer avaliar: "))
                        episodio_encontrado = False
                        for episodio in temporada.episodios:
                            if escolha_episodio == episodio.numero_episodio:
                                episodio_encontrado = True
                                nota = float(input("Qual a nota que deseja dar: "))
                                episodio.avaliar_episodio(nota)
                                dados.salvar_midias(catalogo)
                        if not episodio_encontrado:
                            print("Esse episódio não é válida nessa série.")
                                
                if not temporada_encontrada:
                    print("Essa temporada não é válida nessa série.")
                    
            break
    if not selecao_encontrada:
        print("❌ ID não encontrado no catálogo.")

def relatorio_midia():
    pass

def encerrar_programa():
    pass
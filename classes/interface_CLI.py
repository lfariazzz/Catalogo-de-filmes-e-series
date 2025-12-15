from classes.midia import Midia
from datetime import date
from classes.serie import Serie
from classes.filme import Filme
from classes.episodio import Episodio
from classes.temporada import Temporada
from datetime import datetime
from classes.historico import Historico
from classes import relatorios
import dados
import json

def exibir_menu():
    print("-" * 43, "🔥🎬ForgeFlix🎬🔥", "-" * 43)
    print("Seja bem vindo ao ForgeFlix, seu catálogo de filmes e séries desenvolvido por Levi Farias.")
    print("Estes são os comando implementados para controle por CLI:")
    print("-" * 30, "🎞️Gestão de mídia🎞️", "-" * 30)
    print("1. Exibir lista com as mídias disponíveis no catálogo")
    print("2. Adicionar mídia ao catálogo")
    print("3. Avaliar mídia")
    print("4. Atualizar mídia")
    print("5. Excluir mídia")
    print("6. Relatório de mídias")
    print("-" * 30, "📺Gestão de Série📺", "-" * 30)
    print("7. Exibir menu de séries")
    print("-" * 30, "👤Comandos de Usuário👤", "-" * 30)
    print("11. Criar Lista personalizada de um Usuário")
    print("12. Adicionar mídia à lista")
    print("0. Encerrar programa")

def exibir_menu_serie():
    print("------------COMANDOS EXTRAS DE SÉRIES------------")
    print("8. Adicionar temporada de uma série")
    print("9. Adicionar episódio de uma temporada de uma série")
    print("10. Atualizar um episódio")


def rodar_sistema():
    print("🔄 Carregando dados...")
    catalogo = dados.carregar_midias()
    print(f"✅ {len(catalogo)} mídias carregadas na memória.")

    historico = Historico()

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
        elif decisao == 4:
            atualizar_midia(catalogo, historico)
        elif decisao == 5:
            excluir_midia(catalogo)
        elif decisao == 6:
            exibir_relatorio(catalogo, historico)
        elif decisao == 7:
            exibir_menu_serie()
        elif decisao == 8:
            adicionar_temporada(catalogo)
        elif decisao == 9:
            adicionar_episodio(catalogo)
        elif decisao == 10:
            atualizar_episodio(catalogo, historico)
        else:
            print("Digite uma opção válida")

        print("Digite uma nova opção ou digite menu para exibir o menu novamente")

def exibir_catalogo(catalogo):
    print("-" * 30, "Este é o catálogo disponível no ForgeFlix", "-" * 30)
    if not catalogo:
        print("🚫NENHUMA MÍDIA CADASTRADA🚫")
    else:
        for midia in catalogo:
           print(f"{midia}")
        historico = Historico() 
        media_geral = historico.media_catalogo(catalogo)
        if media_geral > 0:
            print(f"\n⭐  Média Geral do Catálogo: {media_geral:.2f} ⭐")

def adicionar_midia(catalogo):
    print("-" * 30, "Este é modo de adição de mídias e séries do ForgeFlix:", "-" * 30)

    #Definição do título
    titulo = str(input("Digite o título da mídia: "))

    #Definição do ano
    ano = int(input("Digite o ano da mídia: "))

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
    
    for midia in catalogo:
        if midia.titulo.lower() == titulo.lower() and midia.ano == ano and midia.tipo == decisao_midia:
            print("Essa mídia já foi adicionada ao catálogo.")
            return

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

def atualizar_midia(catalogo, historico):
    for midia in catalogo:
        print(f"ID: {midia.id:<5} | {midia.tipo:<7} | {midia.ano} | {midia.titulo}")
    selecao_encontrada = False
    selecao_midia = int(input("Digite o ID da mídia que você quer atualizar: "))
    for midia in catalogo:
        if midia.id == selecao_midia:
            selecao_encontrada = True
            decisao_midia = int(input(f"""\n🖊️ Editando: {midia.titulo}
1. Título
2. Ano
3. Gênero
4. Classificação Indicativa
5. Status (Assistido/Não Assistido) de um filme
0. Cancelar
Digite a opção desejada: """))
            
            if decisao_midia == 1:
                novo_titulo = str(input(f"Digite o novo título que quer atribuir a {midia.titulo}: "))
                midia.titulo = novo_titulo
                print("✅ Alteração realizada com sucesso!")
            elif decisao_midia == 2:
                novo_ano = int(input(f"Digite o novo ano que quer atribuir a {midia.titulo}: "))
                midia.ano = novo_ano
                print("✅ Alteração realizada com sucesso!")
            elif decisao_midia == 3:
                novo_genero = str(input(f"Digite o novo gênero que quer atribuir a {midia.titulo}: "))
                midia.genero = novo_genero
                print("✅ Alteração realizada com sucesso!")
            elif decisao_midia == 4:
                novo_classificacao = input(f"Digite a nova classificação indicativa que quer atribuir a {midia.titulo}: ")
                midia.classificacao_indicativa = novo_classificacao
                print("✅ Alteração realizada com sucesso!")
            elif decisao_midia == 5:
                if midia.tipo == "FILME":

                    print(f"Status atual: {midia.status}")
                    print("1. NÃO ASSISTIDO")
                    print("2. ASSISTINDO")
                    print("3. ASSISTIDO")
                    op_status = input("Escolha o novo status: ")  
                    if op_status == "1": midia.status = "NÃO ASSISTIDO"
                    elif op_status == "2": midia.status = "ASSISTINDO"
                    elif op_status == "3": 
                        historico.registrar_conclusao(midia, 0.0)
                    else: print("❌ Opção inválida, mantendo anterior.")
                else:
                    print("Avaliações de séries devem ser feitas usando comandos de séries. Retornando...")

            elif decisao_midia == 0:
                print("Edição cancelada, voltando ao menu principal...")
                return
            else:
                print("Essa não é uma opção disponível, voltando ao menu principal...")
                return
            dados.salvar_midias(catalogo)

    if not selecao_encontrada:
        print("❌ ID não encontrado no catálogo.")

def excluir_midia(catalogo):
    for midia in catalogo:
        print(f"ID: {midia.id:<5} | {midia.tipo:<7} | {midia.ano} | {midia.titulo}")
    selecao_encontrada = False
    selecao_midia = int(input("Digite o ID da mídia que você quer excluir: "))
    for midia in catalogo:
        if midia.id == selecao_midia:
            selecao_encontrada = True
            confirmacao_exclusao = str(input(f"Tem certeza que deseja excluir {midia.titulo}? (S/N) "))
            if confirmacao_exclusao.lower() == 's':
                catalogo.remove(midia)
                dados.salvar_midias(catalogo)
                break
            elif confirmacao_exclusao.lower() == 'n':
                print("Cancelando operação...")
                break
    if not selecao_encontrada:
        print("❌ ID não encontrado no catálogo.")

def exibir_relatorio(catalogo, historico):
    print("\n" + "="*40)
    print("      📊 RELATÓRIOS DO CATÁLOGO      ")
    print("="*40)
    media_geral = historico.media_catalogo(catalogo)
    if media_geral > 0:
        print(f"⭐ Média de Qualidade do Catálogo: {media_geral:.2f} / 10.0")
    else:
        print("⭐ Média de Qualidade: N/A (Nenhuma avaliação ainda)")


    print("-" * 40)
    print("\n1 - ⏱️  CÁLCULO DE TEMPO DE TELA")
    print("Descubra quanto tempo você gastou assistindo num período.")
    print("\n2 - ⏱️  CÁLCULO DE TEMPO DE MÍDIA")
    print("\nDescubra qual tipo de mídia você mais assiste.")
    print("\n3 - ⭐  TOP 10 MÍDIAS")
    print("\nDescubra quais são as melhores mídias avaliadas do catálogo.")

    decisao_relatorio = int(input("Qual relatório deseja exibir? "))
    
    if decisao_relatorio == 1:
        relatorios.relatorio_tempo_assistido(historico)
    elif decisao_relatorio == 2:
        relatorios.relatorio_tempo_tipos(historico)
    elif decisao_relatorio == 3:
        relatorios.relatorio_top_midias(catalogo)
        

def adicionar_temporada(catalogo):
    print("----------Modo de adição de temporada----------")
    for midia in catalogo:
        if midia.tipo == "SÉRIE":
            print(f"ID: {midia.id:<5} | {midia.tipo:<7} | {midia.ano} | {midia.titulo} ")
    serie_encontrada = False
    escolha_serie = int(input("Digite o ID da série que deseja adicionar a temporada: "))
    for midia in catalogo:
        if midia.tipo == "SÉRIE" and escolha_serie == midia.id:
            serie_encontrada = True
            numero_temporada_nova = int(input("Qual temporada deseja adicionar? "))
            ja_existe = False
            for temporada in midia.temporadas:
                if numero_temporada_nova == temporada.numero_temporada:
                    ja_existe = True
                    break
            if ja_existe:
                print("❌ Essa temporada já existe.")
            else:
                nova_temp = Temporada(numero_temporada_nova, "NÃO ASSISTIDO", [])
                midia.temporadas.append(nova_temp)
                dados.salvar_midias(catalogo)
                print(f"✅ Temporada {numero_temporada_nova} adicionada com sucesso!")
            break


    if not serie_encontrada:
        print("❌ ID da série não encontrado no catálogo.")

def adicionar_episodio(catalogo):
    print("----------Modo de adição de episódio----------")
    for midia in catalogo:
        if midia.tipo == "SÉRIE":
            print(f"ID: {midia.id:<5} | {midia.tipo:<7} | {midia.ano} | {midia.titulo}")
    serie_encontrada = False
    escolha_serie = int(input("Digite o ID da série que deseja adicionar o episódio: "))
    for midia in catalogo:
        if midia.tipo == "SÉRIE" and escolha_serie == midia.id:
            serie_encontrada = True
            print(f"Essas são as temporadas adicionadas de {midia.titulo}:")
            for temporada in midia.temporadas:
                print(f"Temporada {temporada.numero_temporada}")
            temporada_encontrada = False
            escolha_temporada = int(input("Em qual deseja adicionar um episódio? "))
            for temporada in midia.temporadas:
                if escolha_temporada == temporada.numero_temporada:
                    temporada_encontrada = True
                    print(f"Adicionando na Temporada {temporada.numero_temporada}...")
                    num__ep = int(input("Qual episódio deseja adicionar a série? "))
                    tit_ep = str(input("Qual é o título do episódio? "))
                    duracao_ep = int(input("Qual é a duração do ep em minutos? "))
                    episodio_novo = Episodio(num__ep, tit_ep, duracao_ep, datetime.now(), "NÃO ASSISTIDO")
                    temporada.episodios.append(episodio_novo)
                    dados.salvar_midias(catalogo)
            if not temporada_encontrada:
                print("❌ Você não digitou uma temporada válida.")
    if not serie_encontrada:
        print("❌ ID da série não encontrado no catálogo.")
            
def atualizar_episodio(catalogo, historico):
    print("----------Modo de edição de episódio----------")
    for midia in catalogo:
        if midia.tipo == "SÉRIE":
            print(f"ID: {midia.id:<5} | {midia.tipo:<7} | {midia.ano} | {midia.titulo}")
    serie_encontrada = False
    escolha_serie = int(input("Digite o ID da série que deseja editar o episódio: "))
    for midia in catalogo:
        if midia.tipo == "SÉRIE" and escolha_serie == midia.id:
            serie_encontrada = True
            for temporada in midia.temporadas:
                print(f"Temporada {temporada.numero_temporada}")
                for episodio in temporada.episodios:
                    print(f" Ep {episodio.numero_episodio} - {episodio.titulo}")
            temporada_encontrada = False
            escolha_temporada = int(input("Em qual temporada deseja editar um episódio? "))
            for temporada in midia.temporadas:
                    if escolha_temporada == temporada.numero_temporada:
                        temporada_encontrada = True
                        escolha_episodio = int(input(f"Qual episódio da {temporada.numero_temporada}a temporada deseja atualizar? "))
                        episodio_encontrado = False
                        for episodio in temporada.episodios:
                            if escolha_episodio == episodio.numero_episodio:
                                episodio_encontrado = True
                                print(f"\n🖊️ Editando Ep {episodio.numero_episodio}: {episodio.titulo}")
                                print("1. Alterar Título")
                                print("2. Alterar Duração")
                                print("3. Alterar Status")
                                decisao_edicao = int(input("O que deseja fazer? "))
                                if decisao_edicao == 1:
                                    titulo_novo = str(input("Digite o novo título"))
                                    episodio.titulo = titulo_novo
                                elif decisao_edicao == 2:
                                    duracao_nova = int(input("Digite a nova duração"))
                                    episodio.duracao_minutos = duracao_nova
                                elif decisao_edicao == 3:
                                    print(f"Status Atual: {episodio.status}")
                                    print("1. NÃO ASSISTIDO | 2. ASSISTINDO | 3. ASSISTIDO")
                                    status_novo = input("Novo Status: ")
                                    status_anterior = episodio.status
                                    if status_novo == "1": episodio.status = "NÃO ASSISTIDO"
                                    elif status_novo == "2": episodio.status = "ASSISTINDO"
                                    elif status_novo == "3":
                                        historico.registrar_conclusao(episodio, 0.0)
                                    if episodio.status != status_anterior:
                                                midia.verificar_status_automatico()
                                                print(f"✅ Status salvo. Série atualizada para: {midia.status}")
                                    dados.salvar_midias(catalogo)
                                else:
                                    print("❌ Você não digitou uma opção válida.")
                        if not episodio_encontrado:
                            print("❌ Você não digitou um episódio válido.")
            if not temporada_encontrada:
                print("❌ Você não digitou uma temporada válida.")
    if not serie_encontrada:
        print("❌ ID da série não encontrado no catálogo.")

#0
def encerrar_programa():
    pass
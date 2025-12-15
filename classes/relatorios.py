from datetime import datetime
from classes.historico import Historico

def relatorio_tempo_assistido(historico):
    print("\n" + "-"*40)
    print("   ⏱️  RELATÓRIO DE TEMPO DE TELA")
    print("-" * 40)
    try:
        print("Digite as datas no formato dia/mês/ano (Ex: 15/12/2024)")
        inicio_str = input("Data Inicial: ")
        fim_str = input("Data Final:   ")

        data_inicio = datetime.strptime(inicio_str, "%d/%m/%Y")

        data_fim = datetime.strptime(fim_str, "%d/%m/%Y").replace(hour=23, minute=59, second=59)

        total_minutos = historico.calcular_tempo_assistido(data_inicio, data_fim)
        horas = int(total_minutos // 60)
        minutos = int(total_minutos % 60)

        print(f"\n✅ Resultados entre {inicio_str} e {fim_str}:")
        print(f"   Total assistido: {total_minutos} minutos")
        print(f"   Equivalente a:   {horas}h {minutos}min")
    except ValueError:
        print("\n❌ Erro: Data inválida. Use o formato DD/MM/AAAA.")
    input("\nPressione Enter para continuar...")

def relatorio_tempo_tipos(historico):
    total_filme = 0
    total_serie = 0
    for registro in historico.registros:
        if hasattr(registro.midia, 'tipo') and registro.midia.tipo == "FILME":
            total_filme += registro.midia.duracao_minutos
        else:
            total_serie += registro.midia.duracao_minutos
    horas_filme = total_filme // 60
    minutos_filme = total_filme % 60
    horas_serie = total_serie // 60 
    minutos_serie = total_serie % 60
    print(f"\n🎬 FILMES: {horas_filme}h {minutos_filme}min")
    print(f"📺 SÉRIES: {horas_serie}h {minutos_serie}min")

    input("\nPressione Enter para continuar...")

def relatorio_top_midias(catalogo):
    print("\n" + "-"*40)
    print("   ⭐ TOP 10 MÍDIAS MELHOR AVALIADAS")
    print("-" * 40)
    midias_avaliadas = []
    for midia in catalogo:
        if midia.media:
            midias_avaliadas.append(midia)
    if not midias_avaliadas:
        print("⚠️ Nenhuma mídia avaliada ainda.")
    else:
        midias_avaliadas.sort(reverse=True)
    for i, midia in enumerate(midias_avaliadas[:10], 1):
        print(f"{i}º | {midia.media:.1f} ★ | {midia.titulo}")
    input("\nPressione Enter para continuar...")

def relatorio_top_series_assistidas(catalogo):
    print("\n" + "-"*40)
    print("   🏃 TOP 3 SÉRIES MAIS MARATONADAS")
    print("-" * 40)

    placar = []

    for midia in catalogo:
        episodios_assistidos = 0
        if midia.tipo == "SÉRIE":
            for temporada in midia.temporadas:
                for episodio in temporada.episodios:
                    if episodio.status == "ASSISTIDO":
                        episodios_assistidos += 1
            if episodios_assistidos > 0:
                placar.append((midia.titulo, episodios_assistidos))
    if not placar:
        print("⚠️ Nenhuma série maratonada ainda.")
    else:
        placar.sort(key=lambda x: x[1], reverse=True)
        
        for i, item in enumerate(placar[:3], 1):
            print(f"{i}º | {item[1]} eps | {item[0]}")

    input("\nPressione Enter para continuar...")        

def relatorio_media_genero(catalogo):
    medias_generos = {}
    for midia in catalogo:
        if midia.media > 0 and midia.genero:
            if midia.genero in medias_generos:
                medias_generos[midia.genero].append(midia.media)
            else:
                medias_generos[midia.genero] = [midia.media]
    for generos, medias in medias_generos.items():
        sum(medias) / len(medias) 
    for generos, medias in medias_generos.items():
        media_final = sum(medias) / len(medias)
        print(f'Genero: {generos} | Media: {media_final:.2f}')
from datetime import datetime

def relatorio_tempo_assistido(historico):
    print("\n" + "-"*40)
    print("   ⏱️  RELATÓRIO DE TEMPO DE TELA")
    print("-" * 40)
    try:
        print("Digite as datas no formato dia/mês/ano (Ex: 15/12/2024)")
        inicio_str = input("Data Inicial: ")
        fim_str = input("Data Final:   ")

        data_inicio = datetime.strptime(inicio_str, "%d/%m/%Y")
        # O fix da meia-noite que implementamos
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
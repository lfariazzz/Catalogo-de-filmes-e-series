from datetime import date
from classes.midia import Midia
from classes.filme import Filme
from classes.serie import Serie
from classes.episodio import Episodio
from classes.temporada import Temporada
from classes.historico import Historico # <--- IMPORT NOVO
import dados

"""Main desenvolvida por IA para testar persistência e relatórios"""

if __name__ == "__main__":
    print("="*40)
    print("🎬 TESTE 1: SALVAMENTO E CARREGAMENTO")
    print("="*40)

    # --- 1. CRIAÇÃO DOS DADOS ---
    # Criar um Filme
    filme1 = Filme(
        1, "Matrix", "Ficção Científica", 1999, 130, "14", 
        ["Keanu Reeves"], "ASSISTIDO", [10, 9]
    )

    # Criar uma Série (com Temporada e Episódio)
    ep1 = Episodio(1, "Piloto", 50, date(2008, 1, 20), "ASSISTIDO", 9.5)
    temp1 = Temporada(1, "ASSISTIDO", [ep1])
    serie1 = Serie(
        2, "Breaking Bad", "Drama", 2008, 50, "18", 
        ["Bryan Cranston"], "ASSISTINDO", [], 
        temporadas=[temp1]
    )

    # Colocar tudo numa lista
    catalogo = [filme1, serie1]

    # --- 2. PERSISTÊNCIA ---
    # Salvar
    dados.salvar_midias(catalogo)

    # Carregar de volta
    print("\n🔄 Tentando carregar os dados do arquivo...")
    catalogo_carregado = dados.carregar_midias()
    
    print(f"✅ Foram carregados {len(catalogo_carregado)} itens.")
    
    for midia in catalogo_carregado:
        print(f"   - {midia}") 
        if midia.tipo == "SÉRIE":
            print(f"     (Série com {len(midia)} episódios no total)")

    print("\n" + "="*40)
    print("📊 TESTE 2: RELATÓRIO DE OCUPAÇÃO")
    print("="*40)

    # --- 3. TESTE DO HISTÓRICO ---
    # Vamos criar um histórico fictício usando as mídias que já criamos acima
    meu_historico = Historico(id_historico=1)

    # Cenário:
    # 1. Assistiu 'Matrix' (130 min) no dia 15/Jan
    meu_historico.registrar_conclusao(filme1, date(2025, 1, 15), 10)
    
    # 2. Assistiu 'Matrix' de novo (130 min) no dia 20/Jan
    meu_historico.registrar_conclusao(filme1, date(2025, 1, 20), 9)

    # 3. Assistiu 'Breaking Bad' (50 min) no dia 10/Março (FORA DO PERÍODO)
    meu_historico.registrar_conclusao(serie1, date(2025, 3, 10), 8)

    # Definir o período do relatório (Apenas Janeiro de 2025)
    inicio = date(2025, 1, 1)
    fim = date(2025, 1, 31)

    # Calcular
    minutos = meu_historico.calcular_tempo_assistido(inicio, fim)
    
    print(f"📅 Período analisado: {inicio} até {fim}")
    print(f"⏱️  Tempo Total Assistido: {minutos} minutos")
    
    # Validação
    print(f"\n>> Esperado: 260 minutos (2x Matrix de 130min).") 
    print(f">> O episódio da série (Março) deve ser ignorado.")
from datetime import date
from classes.midia import Midia
from classes.filme import Filme
from classes.serie import Serie
from classes.episodio import Episodio
from classes.temporada import Temporada
import dados

"""Main desenvolvida por IA apenas para testar a persistências de dados (feita manualmente)"""

if __name__ == "__main__":
    print("🎬 Iniciando teste de salvamento...")

    # 1. Criar um Filme
    filme1 = Filme(
        1, "Matrix", "Ficção Científica", 1999, 130, "14", 
        ["Keanu Reeves"], "ASSISTIDO", [10, 9]
    )

    # 2. Criar uma Série (com Temporada e Episódio)
    # Primeiro o Episódio (com data!)
    ep1 = Episodio(1, "Piloto", 50, date(2008, 1, 20), "ASSISTIDO", 9.5)
    
    # Depois a Temporada
    temp1 = Temporada(1, "ASSISTIDO", [ep1])
    
    # Depois a Série
    serie1 = Serie(
        2, "Breaking Bad", "Drama", 2008, 50, "18", 
        ["Bryan Cranston"], "ASSISTINDO", [], 
        temporadas=[temp1]
    )

    # 3. Colocar tudo numa lista
    catalogo = [filme1, serie1]

    # 4. Mandar salvar (A Hora da Verdade!)
    dados.salvar_midias(catalogo)

    # --- NOVO TESTE: CARREGAMENTO ---
    print("\n🔄 Tentando carregar os dados do arquivo...")
    catalogo_carregado = dados.carregar_midias()
    
    print(f"✅ Foram carregados {len(catalogo_carregado)} itens.")
    
    for midia in catalogo_carregado:
        # Aqui vamos testar o __str__ que criamos na Semana 2!
        print(f"   - {midia}") 
        
        # Se for série, mostra detalhes extras para provar que carregou a cascata
        if midia.tipo == "SÉRIE":
            print(f"     (Série com {len(midia)} episódios no total)")
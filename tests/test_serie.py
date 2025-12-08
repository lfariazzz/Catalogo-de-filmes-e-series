import pytest
from datetime import date
from classes.serie import Serie
from classes.temporada import Temporada
from classes.episodio import Episodio

def test_fluxo_completo_serie():
    """
    Testa a integração completa: Serie -> Temporada -> Episodio
    Verifica contagem (__len__) e cálculo de média.
    """
    # 1. Criando Datas (Seu código exige objeto date)
    d1 = date(2022, 1, 1)
    d2 = date(2022, 1, 8)

    # 2. Criando Episódios
    # ep1: Nota 10
    # ep2: Nota 8
    ep1 = Episodio(1, "Piloto", 45, d1, "ASSISTIDO", 10.0)
    ep2 = Episodio(2, "Segundo", 45, d2, "ASSISTIDO", 8.0)
    
    # 3. Criando Temporada com os episódios
    # A média deve ser (10 + 8) / 2 = 9.0
    temp1 = Temporada(1, "ASSISTINDO", [ep1, ep2])
    
    # 4. Criando Série com a temporada
    serie = Serie(
        1, "Breaking Bad", "Drama", 2008, 50, "18", ["Bryan Cranston"], "ASSISTINDO", [], 
        temporadas=[temp1]
    )
    
    # --- ASSERTS (A Prova Real) ---
    
    # Teste do __len__ da Série (Soma os episódios)
    assert len(serie) == 2
    
    # Teste da nota média da Temporada (Sua lógica de @property)
    assert temp1.nota_media == 9.0

def test_validacao_tipo_temporada_na_serie():
    """Testa se a Série recusa coisas que não são Temporada"""
    with pytest.raises(TypeError):
        # Tenta passar uma string "Gato" no lugar de um objeto Temporada
        Serie(1, "Teste", "Drama", 2022, 50, "10", [], "NÃO ASSISTIDO", [], temporadas=["Gato"])

def test_status_automatico_serie():
    """Testa se a série atualiza o status conforme os episódios são assistidos"""
    from datetime import date
    
    # 1. Arrange: Série com 2 episódios não assistidos
    ep1 = Episodio(1, "Ep1", 50, date(2022, 1, 1), "NÃO ASSISTIDO")
    ep2 = Episodio(2, "Ep2", 50, date(2022, 1, 2), "NÃO ASSISTIDO")
    temp = Temporada(1, "NÃO ASSISTIDO", [ep1, ep2])
    serie = Serie(1, "Teste", "Drama", 2022, 50, "10", [], "NÃO ASSISTIDO", [], [temp])

    # Caso 1: Nada assistido -> NÃO ASSISTIDA
    serie.verificar_status_automatico()
    assert serie.status == "NÃO ASSISTIDO"

    # Caso 2: Assiste o primeiro -> ASSISTINDO
    ep1.status = "ASSISTIDO" # Usuário assistiu um
    serie.verificar_status_automatico() # Recalcula
    assert serie.status == "ASSISTINDO"

    # Caso 3: Assiste o último -> ASSISTIDA
    ep2.status = "ASSISTIDO" # Usuário terminou tudo
    serie.verificar_status_automatico() # Recalcula
    assert serie.status == "ASSISTIDO"
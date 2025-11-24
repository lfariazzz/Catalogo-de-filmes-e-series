from classes.filme import Filme
import pytest # <--- Importante!

def test_criar_filme_valido():
    filme = Filme(
        1, 
        "Matrix", 
        "Ficção", 
        1999, 
        130, 
        "14 anos", 
        ["Keanu Reeves"], 
        "NÃO ASSISTIDO", 
        []
    )

    assert filme.titulo == "Matrix"
    assert filme.duracao_minutos == 130
    assert filme.ano == 1999
    assert filme.tipo == "FILME"

def test_validacao_titulo_vazio():
    """Testa se o sistema bloqueia filmes com título vazio"""
    with pytest.raises(ValueError): # Esperamos um ValueError
        Filme(1, "", "Gênero", 2022, 120, "10", [], "NÃO", [])

def test_validacao_duracao_negativa():
    """Testa se o sistema bloqueia filmes com duração negativa"""
    with pytest.raises(ValueError): # Esperamos um ValueError
        Filme(1, "Matrix", "Gênero", 2022, -100, "10", [], "NÃO", [])
from classes.filme import Filme
import pytest

def test_criar_filme_valido():
    filme = Filme(
        1, 
        "Matrix", 
        "Ficção Científica", 
        1999, 
        130, 
        "14", 
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

# --- TESTES DE ANO ---
def test_validacao_ano_muito_antigo():
    """Testa se bloqueia anos anteriores a 1895"""
    with pytest.raises(ValueError):
        Filme(1, "Matrix", "Ficção Científica", 1800, 130, "14", [], "NÃO ASSISTIDO", [])

def test_validacao_ano_tipo_errado():
    """Testa se bloqueia ano como texto"""
    with pytest.raises(TypeError):
        Filme(1, "Matrix", "Ficção Científica", "2022", 130, "14", [], "NÃO ASSISTIDO", [])

# --- TESTES DE CLASSIFICAÇÃO ---
def test_validacao_classificacao_invalida():
    """Testa se bloqueia classificações que não estão na lista permitida"""
    with pytest.raises(ValueError):
        # Tenta criar com classificação "21" (que não existe)
        Filme(1, "Matrix", "Ficção Científica", 1999, 130, "21", [], "NÃO ASSISTIDO", [])

def test_sanitizacao_classificacao():
    """Testa se aceita 'l' minúsculo e converte para 'L'"""
    filme = Filme(1, "Matrix", "Ficção Científica", 1999, 130, "l", [], "NÃO ASSISTIDO", [])
    assert filme.classificacao_indicativa == "L"

# --- TESTES DE STATUS ---
def test_validacao_status_invalido():
    """Testa se bloqueia status estranhos"""
    with pytest.raises(ValueError):
        Filme(1, "Matrix", "Ficção Científica", 1999, 130, "14", [], "VENDO AGORA", [])

def test_sanitizacao_status():
    """Testa se aceita status minúsculo e salva maiúsculo"""
    filme = Filme(1, "Matrix", "Ficção Científica", 1999, 130, "14", [], "assistido", [])
    assert filme.status == "ASSISTIDO"

# --- TESTES DE GÊNERO ---
def test_validacao_genero_invalido():
    """Testa se bloqueia gêneros que não estão na lista"""
    with pytest.raises(ValueError):
        Filme(1, "Matrix", "Culinária", 1999, 130, "14", [], "NÃO ASSISTIDO", [])

def test_sanitizacao_genero():
    """Testa se o Title Case (Ação) funciona mesmo digitando 'ação'"""
    # "ação" deve virar "Ação"
    filme = Filme(1, "Matrix", "ação", 1999, 130, "14", [], "NÃO ASSISTIDO", [])
    assert filme.genero == "Ação"

# --- TESTES DE ELENCO ---
def test_validacao_elenco_nao_lista():
    """Testa se bloqueia passar o elenco como string solta"""
    with pytest.raises(TypeError):
        Filme(1, "Matrix", "Ficção Científica", 1999, 130, "14", "Keanu Reeves", "NÃO ASSISTIDO", [])

# --- TESTES DE NOTAS ---
def test_validacao_notas_fora_do_intervalo():
    """Testa se bloqueia notas maiores que 10"""
    with pytest.raises(ValueError):
        Filme(1, "Matrix", "Ficção Científica", 1999, 130, "14", [], "NÃO ASSISTIDO", [11.0])

def test_validacao_notas_tipo_errado():
    """Testa se bloqueia passar notas fora de uma lista"""
    with pytest.raises(TypeError):
        # Passando nota 10 solta, sem colchetes
        Filme(1, "Matrix", "Ficção Científica", 1999, 130, "14", [], "NÃO ASSISTIDO", 10)
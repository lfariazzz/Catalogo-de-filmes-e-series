import pytest
from datetime import datetime, date, timedelta
from classes.filme import Filme
from classes.serie import Serie
from classes.temporada import Temporada
from classes.episodio import Episodio
from classes.usuario import Usuario
from classes.historico import Historico
from classes.configuracao import Configuracao

# ==========================================
# 🏗️ FIXTURES (Dados prontos para os testes)
# ==========================================

@pytest.fixture
def config_mock():
    # Mock simples da configuração para não depender de arquivo externo
    class ConfigMock:
        nota_recomendada = 7.0
        limite_listas = 10
    return ConfigMock()

@pytest.fixture
def filme_matrix():
    # CORREÇÃO: Gênero ajustado para "Ficção Científica" para passar no validador
    return Filme(101, "Matrix", "Ficção Científica", 1999, 136, "14", ["Keanu"], "NÃO ASSISTIDO")

@pytest.fixture
def serie_breaking_bad():
    # Série com 1 Temporada e 2 Episódios para testes de lógica
    ep1 = Episodio(1, "Pilot", 50, date(2008, 1, 20), "NÃO ASSISTIDO")
    ep2 = Episodio(2, "Cat's in the Bag", 45, date(2008, 1, 27), "NÃO ASSISTIDO")
    temp1 = Temporada(1, "NÃO ASSISTIDO", [ep1, ep2])
    return Serie(201, "Breaking Bad", "Drama", 2008, 0, "18", ["Bryan"], "NÃO ASSISTIDO", temporadas=[temp1])

@pytest.fixture
def usuario_padrao(config_mock):
    return Usuario(1, "Tester", "test@email.com", config_mock)

# ==========================================
# 🎞️ TESTES DE FILME E VALIDAÇÕES (MÍDIA)
# ==========================================

def test_criacao_filme_valido(filme_matrix):
    """1. Testa se um filme é criado com os atributos corretos."""
    assert filme_matrix.titulo == "Matrix"
    assert filme_matrix.duracao_minutos == 136

def test_validacao_ano_invalido():
    """2. Testa se o sistema rejeita anos anteriores a 1895 (Cinema mudo)."""
    with pytest.raises(ValueError):
        Filme(102, "Filme Velho", "Drama", 1800, 120, "L", [], "NÃO ASSISTIDO")

def test_validacao_nota_limites(filme_matrix):
    """3. Testa se o sistema rejeita notas maiores que 10 ou menores que 0."""
    with pytest.raises(ValueError):
        filme_matrix.avaliar_filme(11.0)
    with pytest.raises(ValueError):
        filme_matrix.avaliar_filme(-1.0)

def test_calculo_media_filme(filme_matrix):
    """4. Testa o cálculo da média aritmética das notas."""
    filme_matrix.avaliar_filme(10.0)
    filme_matrix.avaliar_filme(8.0)
    # (10 + 8) / 2 = 9.0
    assert filme_matrix.media == 9.0

def test_validacao_genero_invalido(filme_matrix):
    """5. Testa se o setter de gênero rejeita strings aleatórias."""
    with pytest.raises(ValueError):
        filme_matrix.genero = "Gênero Inexistente"

# ==========================================
# 📺 TESTES DE SÉRIE (LÓGICA COMPLEXA)
# ==========================================

def test_calculo_duracao_total_serie(serie_breaking_bad):
    """6. Testa se a duração da série é a soma dos episódios (50 + 45)."""
    assert serie_breaking_bad.duracao_minutos == 95

def test_status_serie_nao_assistido(serie_breaking_bad):
    """7. Testa status inicial quando nenhum episódio foi visto."""
    serie_breaking_bad.verificar_status_automatico()
    assert serie_breaking_bad.status == "NÃO ASSISTIDO"

def test_status_serie_assistindo(serie_breaking_bad):
    """8. Testa status 'ASSISTINDO' quando vê apenas 1 episódio de 2."""
    ep1 = serie_breaking_bad.temporadas[0].episodios[0]
    ep1.status = "ASSISTIDO"
    
    serie_breaking_bad.verificar_status_automatico()
    assert serie_breaking_bad.status == "ASSISTINDO"

def test_status_serie_completa(serie_breaking_bad):
    """9. Testa status 'ASSISTIDO' apenas quando TODOS episódios são vistos."""
    for temp in serie_breaking_bad.temporadas:
        for ep in temp.episodios:
            ep.status = "ASSISTIDO"
            
    serie_breaking_bad.verificar_status_automatico()
    assert serie_breaking_bad.status == "ASSISTIDO"

def test_media_serie_por_episodios(serie_breaking_bad):
    """10. Testa se a média da série baseia-se nas notas dos episódios."""
    ep1 = serie_breaking_bad.temporadas[0].episodios[0]
    ep2 = serie_breaking_bad.temporadas[0].episodios[1]
    
    ep1.avaliar_episodio(10.0)
    ep2.avaliar_episodio(8.0)
    
    # Média do ep1 é 10, média do ep2 é 8. Média da série = (10+8)/2 = 9.0
    assert serie_breaking_bad.media == 9.0

# ==========================================
# 👤 TESTES DE USUÁRIO E LISTAS
# ==========================================

def test_validacao_email_usuario(config_mock):
    """11. Testa validação simples de email (deve conter @)."""
    with pytest.raises(ValueError):
        Usuario(1, "User", "emailinvalido.com", config_mock)

def test_criar_lista_personalizada(usuario_padrao):
    """12. Testa a criação de uma nova lista vazia."""
    lista = usuario_padrao.criar_lista("Favoritos", "Meus tops")
    assert len(usuario_padrao.listas) == 1
    assert lista.nome == "Favoritos"

def test_adicionar_midia_lista(usuario_padrao, filme_matrix):
    """13. Testa adicionar uma mídia a uma lista."""
    lista = usuario_padrao.criar_lista("Favoritos", "...")
    resultado = lista.adicionar_midia(filme_matrix)
    
    assert resultado is True
    assert len(lista.midias) == 1
    assert lista.midias[0].titulo == "Matrix"

def test_bloqueio_duplicidade_lista(usuario_padrao, filme_matrix):
    """14. Testa se o sistema impede adicionar o mesmo filme duas vezes na lista."""
    lista = usuario_padrao.criar_lista("Favoritos", "...")
    lista.adicionar_midia(filme_matrix)
    resultado = lista.adicionar_midia(filme_matrix) # Tenta de novo
    
    assert resultado is False # Deve falhar
    assert len(lista.midias) == 1

def test_remover_midia_lista(usuario_padrao, filme_matrix):
    """15. Testa remoção de item da lista."""
    lista = usuario_padrao.criar_lista("Temp", "...")
    lista.adicionar_midia(filme_matrix)
    lista.remover_midia(filme_matrix)
    
    assert len(lista.midias) == 0

# ==========================================
# 📜 TESTES DE HISTÓRICO E RELATÓRIOS
# ==========================================

def test_registro_historico(usuario_padrao, filme_matrix):
    """16. Testa se registrar visualização atualiza o histórico e o status da mídia."""
    usuario_padrao.registrar_visualizacao(filme_matrix, nota=10.0)
    
    assert len(usuario_padrao.historico.registros) == 1
    assert usuario_padrao.historico.registros[0].nota == 10.0
    assert filme_matrix.status == "ASSISTIDO"

def test_calculo_tempo_assistido_filtro_data(usuario_padrao, filme_matrix):
    """17. Testa o cálculo de minutos assistidos dentro de um intervalo de datas."""
    # Simula ter assistido hoje
    usuario_padrao.registrar_visualizacao(filme_matrix) # 136 min
    
    hoje = datetime.now().date()
    ontem = hoje - timedelta(days=1)
    amanha = hoje + timedelta(days=1)
    
    # Filtro que inclui hoje
    tempo = usuario_padrao.historico.calcular_tempo_assistido(ontem, amanha)
    assert tempo == 136

def test_calculo_tempo_fora_intervalo(usuario_padrao, filme_matrix):
    """18. Testa se o cálculo ignora registros fora da data selecionada."""
    # Hack para inserir registro com data antiga manualmente
    usuario_padrao.historico.registrar_conclusao(filme_matrix, 10, datetime(2020, 1, 1))
    
    hoje = datetime.now().date()
    tempo = usuario_padrao.historico.calcular_tempo_assistido(hoje, hoje)
    
    assert tempo == 0 # Não deve contar o filme de 2020

# ==========================================
# 🧩 OUTROS / EDGE CASES
# ==========================================

def test_ordenacao_midias(filme_matrix):
    """19. Testa se o método __lt__ funciona para ordenar por nota (Ranking)."""
    filme_ruim = Filme(999, "Ruim", "Ação", 2020, 90, "L", [], "NÃO ASSISTIDO")
    
    filme_matrix.avaliar_filme(10.0)
    filme_ruim.avaliar_filme(2.0)
    
    # Python usa __lt__ para sort. Se filme_ruim < filme_matrix (nota), está certo.
    assert filme_ruim < filme_matrix 

def test_igualdade_midias(filme_matrix):
    """20. Testa o __eq__ para evitar duplicatas (Mesmo Titulo + Ano + Tipo)."""
    filme_clone = Filme(999, "Matrix", "Drama", 1999, 100, "12", [], "NÃO ASSISTIDO")
    # Mesmo título e ano = devem ser considerados iguais para evitar duplicidade
    assert filme_matrix == filme_clone
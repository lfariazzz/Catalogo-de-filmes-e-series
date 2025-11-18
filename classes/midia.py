class Midia:
    """Classe base responsável pelo registro de filmes e séries do catálogo"""
    def __init__(self,id, titulo, tipo, genero, ano, duracao_minutos, classificacao_indicativa, elenco, status, notas):
        """Método responsável pela inicialização da classe"""
        self.id = id
        self.titulo = titulo
        self.tipo = tipo
        self.genero = genero
        self.ano = ano
        self.duracao_minutos = duracao_minutos
        self.classificacao_indicativa = classificacao_indicativa
        self.elenco = elenco
        self.status = status
        self.notas = notas

    def calcular_media(self):
        """Método responsável pelo cálculo da média da mídia com base nas notas atribuídas"""
        pass

    def atualizar_status(self):
        """Método responsável pela atualização do registro de visualização da série"""
        pass

    def __str__(self):
        """Método responsável por representar de forme legível a exibição do filme"""
        pass

    def __eq__(self):
        """Método responsável pela comparação de mídias para conferência de duplicidade"""
        pass

    def __lt__(self):
        """Método responsável por ordenação para organização dos filmes com base em requisitos"""
        pass
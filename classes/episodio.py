class Episodio:
    """Classe que controla os atributos de episódios das mídias de séries"""
    def __init__(self, numero_episodio, titulo, duracao_minutos, data_lancamento, status, nota=None):
        """Método responsável por inicializar a classe"""
        self.numero_episodio = numero_episodio
        self.titulo = titulo
        self.duracao_minutos = duracao_minutos
        self.data_lancamento = data_lancamento
        self.status = status
        self.nota = nota
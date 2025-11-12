class Episodio:
    def __init__(self, numero_episodio, titulo, duracao_minutos, data_lancamento, status, nota=None):
        self.numero_episodio = numero_episodio
        self.titulo = titulo
        self.duracao_minutos = duracao_minutos
        self.data_lancamento = data_lancamento
        self.status = status
        self.nota = nota
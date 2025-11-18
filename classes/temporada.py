class Temporada:
    """Classe que controla os atributos de temporada das mídias de séries"""
    def __init__(self, numero_temporada, status, episodios = None):
        """Método responsável por inicializar a classe"""
        self.numero_temporada = numero_temporada
        self.status = status
        self.episodios = episodios if episodios is not None else []
        self.nota_media = 0.0

    def registrar_episodio(self, episodio):
        """Método responsável pela criação de instâncias da classe episódio"""
        pass
class Temporada:
    def __init__(self, numero_temporada, status, episodios = None):
        self.numero_temporada = numero_temporada
        self.status = status
        self.episodios = episodios if episodios is not None else []
        self.nota_media = 0.0

    def registrar_episodio(self, episodio):
        pass
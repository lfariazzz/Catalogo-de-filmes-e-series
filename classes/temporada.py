class Temporada:
    """Classe que controla os atributos de temporada das mídias de séries"""
    def __init__(self, numero_temporada, status, episodios = None):
        """Método responsável por inicializar a classe"""
        self.numero_temporada = numero_temporada
        self.status = status
        self.episodios = episodios if episodios is not None else []
        self.nota_media = 0.0

    @property
    def numero_temporada(self):
        return self._numero_temporada
    
    @numero_temporada.setter
    def numero_temporada(self,valor):
        if not isinstance(valor, int):
            raise ValueError("O número de uma temporada deve ser um valor inteiro.")
        if valor > 0:
            self._numero_temporada = valor
        else:
            raise ValueError("O número de uma temporada deve ser um valor positivo.")
    
    @property
    def episodios(self):
        return self._episodios
    
    @episodios.setter
    def episodios(self, valor):
        if isinstance(valor, list):
            self._episodios = valor
        else:
            raise ValueError("O atributo deve ser uma lista.") 

    def registrar_episodio(self, episodio):
        """Método responsável pela criação de instâncias da classe episódio"""
        pass
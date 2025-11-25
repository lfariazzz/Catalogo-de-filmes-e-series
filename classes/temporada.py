class Temporada:
    """Classe que controla os atributos de temporada das mídias de séries"""
    def __init__(self, numero_temporada, status, episodios = None):
        """Método responsável por inicializar a classe"""
        self._numero_temporada = None
        self.numero_temporada = numero_temporada
        self._status = None
        self.status = status
        self._episodios = []
        self.episodios = episodios if episodios is not None else []

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
    def status(self):
        return self._status
    
    @status.setter
    def status(self, valor):
        status_validos = ["ASSISTIDO", "ASSISTINDO", "NÃO ASSISTIDO"]
        if valor.upper() not in status_validos:
            raise ValueError(f"Insira um status disponível: {status_validos}")
        else:
            self._status = valor.upper()
    
    @property
    def episodios(self):
        return self._episodios
    
    @episodios.setter
    def episodios(self, valor):
        if isinstance(valor, list):
            self._episodios = valor
        else:
            raise ValueError("O atributo deve ser uma lista.") 
        

    @property
    def nota_media(self):
        notas_validas = [ep.nota for ep in self.episodios if ep.nota is not None]
        if not notas_validas:
            return 0.0
        return sum(notas_validas) / len(notas_validas)
        

    def registrar_episodio(self, episodio):
        """Método responsável pela criação de instâncias da classe episódio"""
        pass
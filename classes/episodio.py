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

    @property
    def numero_episodio(self):
        return self._numero_episodio
    
    @numero_episodio.setter
    def numero_episodio(self,valor):
        if not isinstance(valor, int):
            raise ValueError("O número de um episódio deve ser um valor inteiro.")
        if valor > 0:
            self._numero_episodio = valor
        else:
            raise ValueError("O número de uma episódio deve ser um valor positivo.")
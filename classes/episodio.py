from datetime import date

class Episodio:
    """Classe que controla os atributos de episódios das mídias de séries"""
    def __init__(self, numero_episodio, titulo, duracao_minutos, data_lancamento, status, notas = None):
        """Método responsável por inicializar a classe"""
        self._numero_episodio = None
        self.numero_episodio = numero_episodio
        self._titulo = None
        self.titulo = titulo
        self._duracao_minutos = None
        self.duracao_minutos = duracao_minutos
        self.data_lancamento = data_lancamento
        self._status = None
        self.status = status
        self._notas = None
        self.notas = notas if notas is not None else []

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
    
    @property
    def titulo(self):
        return self._titulo
    
    @titulo.setter
    def titulo(self, valor):
        if not valor or valor.strip() == "":
            raise ValueError("O título não pode ser vazio.")
        else:
            self._titulo = valor

    @property
    def duracao_minutos(self):
        return self._duracao_minutos
    
    @duracao_minutos.setter
    def duracao_minutos(self, valor):
        if isinstance(valor, (int, float)):
            if valor <= 0:
                raise ValueError("A duração da mídia deve ser maior que 0 minutos")
            else:
                self._duracao_minutos = valor
        else:
            raise TypeError("A duração deve ser um número.")
        
    @property
    def data_lancamento(self):
        return self._data_lancamento
    
    @data_lancamento.setter
    def data_lancamento(self, valor):
        if isinstance(valor, date):
            self._data_lancamento = valor
        else:
            raise TypeError("Digite uma data válida: DD/MM/AAAA")
    
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
    def notas(self):
        return self._notas
    
    @notas.setter
    def notas(self, valor):
        if valor is not None:
            if isinstance(valor, list):
                for notas in valor:
                    if notas > 10 or notas < 0:
                        raise ValueError("A notas deve estar entre 0 e 10")
                    else:
                        self._notas = valor
            else:
                raise TypeError("A nota deve ser uma lista")
        else:
            self._notas = valor

    @property
    def media(self):
        if not self.notas:
            return 0.0
        return sum(self.notas) / len(self.notas)

    def gerar_dicionario(self):
        return{
            "numero_episodio": self.numero_episodio,
            "titulo": self.titulo,
            "duracao_minutos": self.duracao_minutos,
            "data_lancamento": self.data_lancamento.isoformat(),
            "status": self.status,
            "notas": self.notas
        }
    
    def avaliar_episodio(self, nota):
        if isinstance(nota, (int,float)):
            if nota > 10 or nota < 0:
                raise ValueError("A nota deve estar entre 0 e 10")
            else:
                self.notas.append(nota)
        else:
            raise TypeError("A nota deve ser um número.")
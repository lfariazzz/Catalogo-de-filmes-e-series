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
        if valor <= 0:
            raise ValueError("A duração da mídia deve ser maior que 0 minutos")
        else:
            self._duracao_minutos = valor

    @property
    def notas(self):
        return self._notas
    
    @notas.setter
    def notas(self, valores):
        if isinstance(valores, list):
            for valor in valores:
                if valor > 10 or valor < 0:
                    raise ValueError("As notas devem estar entre 0 e 10")
                else:
                    continue
            self._notas = valores
        else:
            raise TypeError("O atributo notas deve ser uma lista de números")


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
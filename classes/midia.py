class Midia:
    """Classe base responsável pelo registro de filmes e séries do catálogo"""
    def __init__(self,id, titulo, tipo, genero, ano, duracao_minutos, classificacao_indicativa, elenco, status, notas = None):
        """Método responsável pela inicialização da classe"""
        self.id = id
        self._titulo = None
        self.titulo = titulo
        self.tipo = tipo
        self._genero = None
        self.genero = genero
        self._ano = None
        self.ano = ano
        self._duracao_minutos = None
        self.duracao_minutos = duracao_minutos
        self._classificacao_indicativa = None
        self.classificacao_indicativa = classificacao_indicativa
        self._elenco = None
        self.elenco = elenco
        self._status = None
        self.status = status
        self._notas = []
        self.notas = notas if notas is not None else []

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
    def genero(self):
        return self._genero
    
    @genero.setter
    def genero(self, valor):
        generos_validos = [
        "Ação",
        "Aventura",
        "Comédia",
        "Drama",
        "Ficção Científica",
        "Terror",
        "Romance",
        "Suspense",
        "Documentário",
        "Animação",
        "Fantasia",
        "Policial",
        "Musical"
        ]
        if isinstance(valor,str):
            if valor.title() not in generos_validos:
                raise ValueError(f"Digite um gênero disponível: \n{generos_validos}")
            else:
                self._genero = valor.title()
        else:
                raise ValueError(f"Digite um gênero disponível: \n{generos_validos}")


    @property
    def ano(self):
        return self._ano
    
    @ano.setter
    def ano(self, valor):
        if isinstance(valor, int):
            if valor < 1895:
                raise ValueError("Selecione um ano válido.")
            else:
                self._ano = valor
        else:
            raise TypeError("Selecione um ano válido (deve ser inteiro).")

    @property
    def duracao_minutos(self):
        return self._duracao_minutos
    
    @duracao_minutos.setter
    def duracao_minutos(self, valor):
        if isinstance(valor,(int, float)):
            if valor <= 0:
                raise ValueError("A duração da mídia deve ser maior que 0 minutos")
            else:
                self._duracao_minutos = valor
        else:
            raise TypeError("A duração deve ser um número.")

    @property
    def classificacao_indicativa(self):
        return self._classificacao_indicativa
    
    @classificacao_indicativa.setter
    def classificacao_indicativa(self, valor):
        classificacoes_indicativas_validas = ["L", "10", "12", "14", "16", "18"]
        if str(valor).upper() not in classificacoes_indicativas_validas:
            raise ValueError(f"Insira uma classificação indicativa válida: {classificacoes_indicativas_validas}")
        else:
            self._classificacao_indicativa = valor.upper()

    @property
    def elenco(self):
        return self._elenco
    
    @elenco.setter
    def elenco(self, valores):
        if not isinstance(valores, list):
            raise TypeError("O elenco deve ser uma lista.")
        else:
            for valor in valores:
                if not isinstance(valor, str):
                    raise ValueError("O elenco deve conter apenas letras.")
            self._elenco = valores

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
        
    @property
    def media(self):
        if not self.notas:
            return 0
        else:
            return sum(self.notas)/len(self.notas)

    def calcular_media(self):
        """Método responsável pelo cálculo da média da mídia com base nas notas atribuídas"""
    pass
#      Método substituido por um property "média"

    def atualizar_status(self):
        """Método responsável pela atualização do registro de visualização da série"""
        pass

    def __str__(self):
        """Método responsável por representar de forme legível a exibição do filme"""
        return f"{self.titulo} ({self.ano}) - {self.tipo}"
        
    def __eq__(self, midia2):
        """Método responsável pela comparação de mídias para conferência de duplicidade"""
        if isinstance(midia2, Midia):
            return self.titulo == midia2.titulo and self.tipo == midia2.tipo
        else:
            return False

    def __lt__(self, midia2):
        """Método responsável por ordenação em notas médias para organização das mídias"""
        if isinstance(midia2, Midia):
            return self.media < midia2.media
        
    def gerar_dicionario(self):
        return{
            "id": self.id,
            "titulo": self.titulo,
            "tipo": self.tipo,
            "genero": self.genero,
            "ano": self.ano,
            "duracao_minutos": self.duracao_minutos,
            "classificacao_indicativa": self.classificacao_indicativa,
            "elenco": self.elenco,
            "status": self.status,
            "notas": self.notas,
            "media": self.media
        }
    
    
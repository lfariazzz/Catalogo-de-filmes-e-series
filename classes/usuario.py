class Usuario:
    """Classe responsável pelo controle de configurações e dados individuais do usuário"""
    def __init__(self, id, nome, email, listas = None, historico = None):
        """Método responsável pela inicialização da classe"""
        self.id = id
        self._nome = None
        self.nome = nome
        self.email = email
        self.listas = listas if listas is not None else []
        self.historico = historico if historico is not None else None

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, valor):
        if valor is None or valor.strip() == "":
            raise ValueError("O nome não pode ser vazio.")
        else:
            self._nome = valor

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, valor):
        if valor is None or valor.strip() == "":
            raise ValueError("O e-mail não pode ser vazio.")
        elif valor.count("@") != 1:
            raise ValueError("Digite um e-mail válido.")
        else:
             self._email = valor

    def avaliar_midia(self, midia, nota):
        """Método responsável pelo recebimento de notas acerca da opinião do usuário sobre alguma instância de mídia"""
        pass

    def criar_lista(self, id_lista, nome, descricao):
        """Método responsável pela criação de listas personalizadas e individuais de mídias para cada usuário"""
        pass
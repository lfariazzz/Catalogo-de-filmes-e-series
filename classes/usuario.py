class Usuario:
    """Classe responsável pelo controle de configurações e dados individuais do usuário"""
    def __init__(self, id, nome, email, listas = None, historico = None):
        """Método responsável pela inicialização da classe"""
        self.id = id
        self.nome = nome
        self.email = email
        self.listas = listas if listas is not None else []
        self.historico = historico if historico is not None else None
    
    def avaliar_midia(self, midia, nota):
        """Método responsável pelo recebimento de notas acerca da opinião do usuário sobre alguma instância de mídia"""
        pass

    def criar_lista(self, id_lista, nome, descricao):
        """Método responsável pela criação de listas personalizadas e individuais de mídias para cada usuário"""
        pass
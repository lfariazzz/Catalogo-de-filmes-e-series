class Usuario:
    def __init__(self, id, nome, email, listas = None, historico = None):
        self.id = id
        self.nome = nome
        self.email = email
        self.listas = listas if listas is not None else []
        self.historico = historico if historico is not None else None
    
    def avaliar_midia(self, midia, nota):
        pass

    def criar_lista(self, id_lista, nome, descricao):
        pass
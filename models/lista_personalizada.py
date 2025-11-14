class ListaPersonalizada:
    def __init__(self, id_lista, nome, descricao, data_criacao, midias = None):
        self.id_lista = id_lista
        self.nome = nome
        self.descricao = descricao
        self.data_criacao = data_criacao
        self.midias = midias if midias is not None else []

    def editar_lista(self):
        pass
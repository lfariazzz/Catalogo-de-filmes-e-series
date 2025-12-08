from classes.midia import Midia

class ListaPersonalizada:
    """Classe responsável pelo armazenamento dos dados das listas personalizadas do usuário"""
    def __init__(self, id_lista, nome, descricao, data_criacao, midias = None):
        """Método responsável por inicializar a classe"""
        self.id_lista = id_lista
        self.nome = nome
        self.descricao = descricao
        self.data_criacao = data_criacao
        self.midias = midias if midias is not None else []

    def adicionar_midia(self, valor):
        if isinstance(valor, Midia):
            for midia in self.midias:
                if valor == midia:
                    raise ValueError("Essa mídia já está na lista")
                else:
                    self.midias.append(valor)
        else:
            raise TypeError("Você não inseriu uma mídia.")


    def editar_lista(self):
        """Método responsável por alterar dados dos parâmetros da classe"""
        pass
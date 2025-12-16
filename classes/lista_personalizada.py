from classes.midia import Midia
from datetime import date

class ListaPersonalizada:
    """Classe responsável pelo armazenamento dos dados das listas personalizadas do usuário"""
    def __init__(self, id_lista, nome, descricao, data_criacao, midias = None):
        """Método responsável por inicializar a classe"""
        self.id_lista = id_lista
        self.nome = nome
        self.descricao = descricao
        self.data_criacao = data_criacao if isinstance(data_criacao, date) else date.today()
        self.midias = midias if midias is not None else []

    def adicionar_midia(self, midia):
        """Adiciona uma mídia se ela não existir. Retorna True se funcionou."""
        if not isinstance(midia, Midia):
            return False
            
        if midia in self.midias:
            return False 
        
        self.midias.append(midia)
        return True 

    def remover_midia(self, midia):
        """Remove uma mídia da lista. Retorna True se funcionou."""
        if midia in self.midias:
            self.midias.remove(midia)
            return True
        return False

    def editar_lista(self, novo_nome=None, nova_descricao=None):
        """Método responsável por alterar dados dos parâmetros da classe"""
        if novo_nome:
            self.nome = novo_nome
        if nova_descricao:
            self.descricao = nova_descricao

    def criar_dicionario(self):
        lista_titulos = []
        for midia in self.midias:
             lista_titulos.append(midia.titulo)
        
        return {
             "id": self.id_lista,
             "nome": self.nome,
             "descricao": self.descricao,
             "data_criacao": self.data_criacao.isoformat(),
             "midias": lista_titulos
        }
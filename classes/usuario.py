from classes.lista_personalizada import ListaPersonalizada
from classes.historico import Historico # <--- Importante!
from datetime import date

class Usuario:
    """Classe responsável pelo controle de configurações e dados individuais do usuário"""
    def __init__(self, id, nome, email, config_sistema, listas = None, historico = None):
        """Método responsável pela inicialização da classe"""
        self.id = id
        self._nome = None
        self.nome = nome
        self.email = email
        self.config = config_sistema
        self.listas = listas if listas is not None else []
        self.historico = historico if historico is not None else Historico()

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

    def criar_lista(self, nome, descricao):
        """Método responsável pela criação de listas personalizadas"""
        id_lista = len(self.listas) + 1
        data_criacao = date.today()
        nova_lista = ListaPersonalizada(id_lista, nome, descricao, data_criacao)
        self.listas.append(nova_lista)
        return nova_lista

    def registrar_visualizacao(self, midia, nota=0):
        """Registra que uma mídia foi concluída (Wrapper para o Historico)"""
        self.historico.registrar_conclusao(midia, nota)
        print(f"'{midia.titulo}' registrado no histórico!")

    def criar_dicionario(self):
        """Prepara o usuário para ser salvo"""
        listas_convertidas = []
        for lista in self.listas:
            listas_convertidas.append(lista.criar_dicionario())
        historico_convertido = self.historico.criar_dicionario()

        return {
            "id": self.id,
            "nome": self.nome, 
            "email": self.email, 
            "listas": listas_convertidas,
            "historico": historico_convertido
        }
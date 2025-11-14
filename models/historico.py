from registro_visualizacao import RegistroVisualizacao

class Historico:
    def __init__(self, id_historico, registros = None):
        self.id_historico = id_historico
        self.registros = registros if registros is not None else []
        
    def registrar_conclusao(self):
        pass

    def gerar_relatorio(self):
        pass
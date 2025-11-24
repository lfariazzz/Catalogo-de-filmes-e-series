from classes.registro_visualizacao import RegistroVisualizacao

class Historico:
    """Classe responsável por receber registros de conclusão de visualização das mídias"""
    def __init__(self, id_historico, registros = None):
        """Método que inicializa a classe"""
        self.id_historico = id_historico
        self.registros = registros if registros is not None else []
        
    def registrar_conclusao(self, midia, data_visualizacao, nota_atribuida):
        """Método responsável pelo registro da mídia como assistida à partir de instância da classe registro"""
        pass

    def gerar_relatorio(self):
        """Método responsável por gerar dados estatísticos acerca da atividade do usuário"""
        pass
from classes.registro_visualizacao import RegistroVisualizacao
from datetime import date

class Historico:
    """Classe responsável por receber registros de conclusão de visualização das mídias"""
    def __init__(self, id_historico, registros = None):
        """Método que inicializa a classe"""
        self.id_historico = id_historico
        self.registros = registros if registros is not None else []
        
    def registrar_conclusao(self, midia, data_visualizacao, nota_atribuida):
        novo_registro = RegistroVisualizacao(midia, data_visualizacao, "ASSISTIDO", nota_atribuida)
        self.registros.append(novo_registro)
    
    def calcular_tempo_assistido(self, data_inicio, data_fim):
        total_minutos = 0
        for registro in self.registros:
            if data_inicio <= registro.data_visualizacao and data_fim >= registro.data_visualizacao:
                total_minutos += registro.midia.duracao_minutos
        return total_minutos


    def gerar_relatorio(self):
        """Método responsável por gerar dados estatísticos acerca da atividade do usuário"""
        pass
from classes.registro_visualizacao import RegistroVisualizacao
from classes.filme import Filme
from classes.serie import Serie
from datetime import datetime
from classes.midia import Midia

class Historico:
    """Classe responsável por receber registros de conclusão de visualização das mídias"""
    contador_IDS = 0
    def __init__(self, id_historico = None, registros = None):
        """Método que inicializa a classe"""
        if id_historico is None:
            Historico.contador_IDS += 1
            self.id_historico = Historico.contador_IDS
        else:
            self.id_historico = id_historico
        self.registros = registros if registros is not None else []
        
    def registrar_conclusao(self, midia, nota_atribuida, data_visualizacao = None):
        if data_visualizacao is None:
            data_visualizacao = datetime.now()
        novo_registro = RegistroVisualizacao(midia, "ASSISTIDO", nota_atribuida, data_visualizacao)
        self.registros.append(novo_registro)
        midia.status = "ASSISTIDO"
    
    def calcular_tempo_assistido(self, data_inicio, data_fim):
        total_minutos = 0
        for registro in self.registros:
            if data_inicio <= registro.data_visualizacao and data_fim >= registro.data_visualizacao:
                total_minutos += registro.midia.tempo_assistido
        return total_minutos
    
    def media_catalogo(self, catalogo):
        midia_totais = 0
        notas_midias = 0
        for midia in catalogo:
            if midia.media > 0:
                midia_totais += 1
                notas_midias += midia.media
        if midia_totais > 0:
            return notas_midias / midia_totais
        else:
            return 0.0


    def gerar_relatorio(self):
        """Método responsável por gerar dados estatísticos acerca da atividade do usuário"""
        pass
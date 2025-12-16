from classes.registro_visualizacao import RegistroVisualizacao
from datetime import datetime, date

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
            data_reg = registro.data_visualizacao
            if isinstance(data_reg, datetime):
                data_reg = data_reg.date()
            if data_inicio <= data_reg and data_fim >= data_reg:
                total_minutos += registro.midia.duracao_minutos
        return total_minutos

    def media_catalogo(self, catalogo):
        midia_totais = 0
        notas_midias = 0
        for midia in catalogo:
            media_atual = 0
            if hasattr(midia, 'calcular_media'):
                valor = midia.calcular_media()
                media_atual = valor if valor is not None else 0
            
            elif hasattr(midia, 'media'):
                valor = midia.media
                media_atual = valor if valor is not None else 0

            if media_atual > 0:
                midia_totais += 1
                notas_midias += media_atual
        
        if midia_totais > 0:
            return notas_midias / midia_totais
        else:
            return 0.0

    def criar_dicionario(self):
        """Gera o dicionário para salvar no JSON (NOVO!)"""
        lista_registros_json = []
        for registro in self.registros:
            data_formatada = registro.data_visualizacao.isoformat()
            
            lista_registros_json.append({
                "midia_titulo": registro.midia.titulo,
                "status": registro.status,
                "nota": registro.nota,
                "data": data_formatada
            })
            
        return {
            "id": self.id_historico,
            "registros": lista_registros_json
        }
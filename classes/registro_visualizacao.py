from datetime import date, datetime

class RegistroVisualizacao:
    """Classe que representa um item individual do histórico"""
    def __init__(self, midia, status, nota, data_visualizacao):
        self.midia = midia
        self.status = status
        self.nota = nota
        # Garante que a data seja salva corretamente no objeto
        self.data_visualizacao = data_visualizacao

    def to_dict(self):
        """(Opcional) Método auxiliar para converter em dicionário"""
        return {
            "midia_titulo": self.midia.titulo,
            "status": self.status,
            "nota": self.nota,
            "data_visualizacao": self.data_visualizacao.isoformat()
        }
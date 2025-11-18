class RegistroVisualizacao:
    """Classe responsável por registrar mídias como assistidas para adicioná-las à histórico"""
    def __init__(self, midia, data_visualizacao, progresso, nota_atribuida):
        """Método responsável por inicializar a classe"""
        self.midia = midia
        self.data_visualizacao = data_visualizacao
        self.progresso = progresso
        self.nota_atribuida = nota_atribuida
import json

class Configuracao:
    """Classe responsável pelo controle de algumas configurações de limite e estado do sistema"""
    def __init__(self, caminho_arquivo = "data/settings.json"):
        """Método responsável por definir os parâmetros das configurações a partir da leitura do json settings"""
        with open(caminho_arquivo, 'r', encoding='UTF-8') as arquivo:
            dados_configuracoes = json.load(arquivo)

            self.nota_recomendada = dados_configuracoes["nota_recomendacao"]
            self.limite_listas = dados_configuracoes["limite_listas"]
            self.conversao_horas = dados_configuracoes["conversao_horas"]
            self.casas_arredondadas_configuraveis = dados_configuracoes["casas_arredondadas_configuraveis"]
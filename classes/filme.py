from classes.midia import Midia

class Filme(Midia):
    """Classe que herda de mídia responsável pelo controle das mídias classificadas como filme"""
    def __init__(self, id, titulo, genero, ano, duracao_minutos, classificacao_indicativa, elenco, status, notas):
        """Método responsável por inicializar a classe"""
        super().__init__(id, titulo, "FILME", genero, ano, duracao_minutos, classificacao_indicativa, elenco, status, notas)
        #Método para definição dos parâmetros que herdam da classe mídia
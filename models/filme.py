from midia import Midia

class Filme(Midia):
    def __init__(self, id, titulo, genero, ano, duracao_minutos, classificacao_indicativa, elenco, status, notas):
        super().__init__(id, titulo, "FILME", genero, ano, duracao_minutos, classificacao_indicativa, elenco, status, notas)

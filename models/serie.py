from midia import Midia

class Serie(Midia):
    def __init__(self, id, titulo, genero, ano, duracao_minutos, classificacao_indicativa, elenco, status, notas, temporadas=None):
        super().__init__(id, titulo, "SÉRIE", genero, ano, duracao_minutos, classificacao_indicativa, elenco, status, notas)
        self.temporadas = temporadas if temporadas is not None else []
        self.nota_media = 0.0
    def __len__(self):
        pass
from classes.midia import Midia
from classes.temporada import Temporada
from typing import List

class Serie(Midia):
    """Classe que herda de mídia responsável pelo controle das mídias classificadas como série"""
    def __init__(self, id, titulo, genero, ano, duracao_minutos, classificacao_indicativa, elenco, status, notas, temporadas=None):
        """Método responsável por inicializar a classe"""
        super().__init__(id, titulo, "SÉRIE", genero, ano, duracao_minutos, classificacao_indicativa, elenco, status, notas)
        #Método para definição dos parâmetros que herdam da classe mídia
        self.temporadas: List[Temporada] = temporadas if temporadas is not None else []
        self.nota_media = 0.0

    def __len__(self):
        """Método responsável pela soma da quantidade de instâncias de episódios em uma temporada"""
        total_episodios = 0
        for temporada in self.temporadas:
            total_episodios += len(temporada.episodios)
        return total_episodios
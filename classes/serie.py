from classes.midia import Midia
from classes.temporada import Temporada
from typing import List

class Serie(Midia):
    """Classe que herda de mídia responsável pelo controle das mídias classificadas como série"""
    def __init__(self, id, titulo, genero, ano, duracao_minutos, classificacao_indicativa, elenco, status, notas, temporadas=None):
        """Método responsável por inicializar a classe"""
        super().__init__(id, titulo, "SÉRIE", genero, ano, duracao_minutos, classificacao_indicativa, elenco, status, notas)
        #Método para definição dos parâmetros que herdam da classe mídia
        self._temporadas = []
        self.temporadas: List[Temporada] = temporadas if temporadas is not None else []
        self.nota_media = 0.0

    @property
    def temporadas(self):
        return self._temporadas
    
    @temporadas.setter
    def temporadas(self, valores):
        if isinstance(valores, list):
            for valor in valores:
                if not isinstance(valor,Temporada):
                    raise TypeError("Insira temporadas válidas.")
            self._temporadas = valores
        else:
            raise TypeError("Informe suma lista de temporadas.")

    def __len__(self):
        """Método responsável pela soma da quantidade de instâncias de episódios em uma temporada"""
        total_episodios = 0
        for temporada in self.temporadas:
            total_episodios += len(temporada.episodios)
        return total_episodios
    
    def gerar_dicionario(self):      
        dicionario_base = super().gerar_dicionario()
        dicionario_base["temporadas"] = [temporada.gerar_dicionario() for temporada in self.temporadas]
        return dicionario_base
    
    def verificar_status_automatico(self):
        episodios_totais = 0
        episodios_assistidos = 0

        for temporada in self.temporadas:
            for episodio in temporada.episodios:
                episodios_totais += 1
                if episodio.status == "ASSISTIDO":
                    episodios_assistidos += 1
        if episodios_assistidos == 0:
            self.status = "NÃO ASSISTIDO"
        elif episodios_assistidos > 0 and episodios_assistidos < episodios_totais:
            self.status = "ASSISTINDO"
        elif episodios_totais == episodios_assistidos:
            self.status = "ASSISTIDO"
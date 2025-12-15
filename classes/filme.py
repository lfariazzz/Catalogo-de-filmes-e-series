from classes.midia import Midia

class Filme(Midia):
    """Classe que herda de mídia responsável pelo controle das mídias classificadas como filme"""
    def __init__(self, id, titulo, genero, ano, duracao_minutos, classificacao_indicativa, elenco, status, notas = None):
        """Método responsável por inicializar a classe"""
        super().__init__(id, titulo, "FILME", genero, ano, duracao_minutos, classificacao_indicativa, elenco, status, notas)
        #Método para definição dos parâmetros que herdam da classe mídia
    
    def avaliar_filme(self, nota):
        if isinstance(nota, (int,float)):
            if nota > 10 or nota < 0:
                raise ValueError("A nota deve estar entre 0 e .")
            else:
                print("Avaliação adicionada com sucesso!")
                self._notas.append(nota)
        else:
            raise TypeError("A nota deve ser um número.")
        
    @property
    def tempo_assistido(self):
        tempo_assistido = 0.0
        if self.status == "ASSISTIDO":
            tempo_assistido = self.duracao_minutos
        return tempo_assistido
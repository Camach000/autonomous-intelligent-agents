from ecr.estimulo import Estimulo
from sae.ambiente.elemento import Elemento

class EstimuloAlvo(Estimulo):
    """
    A classe "EstimuloAlvo" implementa um "Estimulo" que detecta a presença de um
    "Elemento.ALVO" numa direção específica da percepção do agente.
    A intensidade do estímulo detectado é inversamente proporcional à distância
    ao alvo (usando um fator de decaimento gama).
    """

    def __init__(self, direccao, gama = 0.9):
        self.__gama = gama
        self.__direccao = direccao

    def detectar(self, percepcao):
        """
        Detecta um alvo na "percepcao" para a "direccao" configurada.
        A "percepcao" é esperada ser um dicionário ou objeto que pode ser indexado
        pela "direccao" para obter informações sobre o elemento, distância, etc.
        Retorna a intensidade calculada se um "Elemento.ALVO" for encontrado,
        caso contrário, retorna 0.
        """
        elemento, distancia, _ = percepcao[self.__direccao]
        intensidade = self.__gama**distancia if elemento == Elemento.ALVO else 0
        return intensidade
        # utilização de um operador ternário para simplificar a utilização desta condição

from ecr.comportamento import Comportamento
import random

from sae import Avancar
from sae import Rodar
from sae import Direccao

class Explorar(Comportamento):
    """
    A classe "Explorar" implementa um comportamento simples de exploração aleatória.
    Com uma certa probabilidade, o agente roda para uma direção aleatória;
    caso contrário, avança na direção atual.
    Este é um comportamento de baixo nível, tipicamente usado quando não há
    objetivos mais específicos (como aproximar de um alvo ou evitar um obstáculo).
    Este comportamento é um dos sub-comportamentos do "Recolher".
    """

    def __init__(self, prob_rotacao = 0.7): #o list(Direccao) é utilizado para converter o enum numa lista de valores
        self.__prob_rotacao = prob_rotacao
        self.__direcoes = list(Direccao)

    def activar(self, percepcao):
        """
        Ativa o comportamento de exploração.
        Gera uma ação aleatória de "Rodar" ou "Avancar".
        """
        acao = random.random() #gera um número aleatório entre 0 e 1
        if acao < self.__prob_rotacao: #se o número gerado for menor que a probabilidade de rotação é executada a ação de rodar
            direcao = random.choice(self.__direcoes) #utilizando o random.choice é escolhido um valor aleatório da lista fornecida
            accao = Rodar(direcao) #retorna a ação de rodar com a direção escolhida aleatoriamente
        else:
            accao = Avancar() #caso contrário é executada a ação de avançar
        return accao
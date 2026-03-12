from ecr.comportamento import Comportamento
from sae.agente.avancar import Avancar

class ExplorarComMemoria(Comportamento):
    """
    A classe "ExplorarComMemoria" implementa um comportamento de exploração que tenta
    evitar revisitar combinações de (posição, direção) recentes.
    Mantém uma memória das últimas N situações (posição, direção) e só avança se
    a situação atual não estiver na memória recente.

    Este é um exemplo de um agente reativo com estado (memória), como discutido
    nos slides 5 a 10 da apresentação "ARQUITECTURA DE AGENTES REACTIVOS (Parte 3)".
    O slide 6 ("AGENTES REACTIVOS COM ESTADO - Exemplo") descreve o comportamento
    "Evitar o Passado", que é similar à lógica aqui.
    Este comportamento é mais sofisticado que a exploração puramente aleatória.
    """

    def __init__(self, dimensao_maxima = 100):
        self.__dimensao_maxima = dimensao_maxima
        self.__memoria = []

    def activar(self, percepcao):
        """
        Ativa o comportamento de exploração com memória.
        "percepcao": A percepção atual do ambiente, contendo a "posicao" e "direccao" do agente.

        Verifica se a situação atual (posição, direção) já está na memória recente.
        Se não estiver, adiciona-a à memória (removendo a mais antiga se a memória
        estiver cheia) e retorna uma ação de "Avancar".
        Se a situação já estiver na memória, não retorna nenhuma ação (None),
        o que permite que outros comportamentos de menor prioridade (como o Explorar aleatório)
        possam ser ativados.
        """
        situacao = (percepcao.posicao, percepcao.direccao)
        if situacao not in self.__memoria:
            self.__memoria.append(situacao)
            if len(self.__memoria) == self.__dimensao_maxima:
                self.__memoria.pop(0)
            return Avancar()
from abc import ABC
from contagem.modelo.estado_contagem import EstadoContagem
from contagem.modelo.operador_incremento import OperadorIncremento
from mod.problema import Problema

class ProblemaContagem(Problema):
    """
    A classe "ProblemaContagem" define a formulação do problema de contagem para ser
    resolvido por um mecanismo de procura.
    Encapsula o estado inicial, os operadores aplicáveis (incrementos) e a condição
    de objetivo (atingir ou ultrapassar um valor final).
    """

    def __init__(self, valor_inicial, valor_final, incrementos):
        super().__init__(EstadoContagem(valor_inicial), 
                         [OperadorIncremento(incremento) for incremento in incrementos])
        self.__valor_final = valor_final

    def objetivo(self, estado):
        """
        Verifica se um dado "estado" (do tipo "EstadoContagem") satisfaz a condição de objetivo.
        O objetivo é alcançado se o "estado.valor" for maior ou igual ao "__valor_final".
        """
        return estado.valor >= self.__valor_final
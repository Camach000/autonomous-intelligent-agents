from abc import ABC
from contagem.modelo.estado_contagem import EstadoContagem
from mod.operador import Operador

# Define a classe OperadorIncremento, que representa uma ação no problema de contagem.
# Herda da classe base Operador. Cada instância representa um incremento específico.
# (retirado de documento 10-pee-1, p. 4, 29; P3-iasa-proj.pdf, p. 3)
class OperadorIncremento(Operador):
    # Construtor. Recebe o valor do incremento que este operador representa.
    def __init__(self, incremento): # Adiciona type hint
        # Armazena o valor do incremento num atributo privado.
        self.__incremento = incremento

    # Implementa o método 'aplicar' da interface Operador.
    # Define a transição de estado: calcula o novo valor adicionando o incremento
    # ao valor do estado atual e retorna um novo objeto EstadoContagem.
    # (retirado de documento 10-pee-1, p. 4, 16; P3-iasa-proj.pdf, p. 3)
    def aplicar(self, estado): # Adiciona type hints
        # Calcula o novo valor.
        novo_valor = estado.valor + self.__incremento
        # Retorna um novo estado com o valor resultante.
        return EstadoContagem(novo_valor)

    # Implementa o método 'custo' da interface Operador.
    # Define o custo associado à aplicação deste operador.
    # Neste caso, o custo é definido como o quadrado do valor do incremento.
    # (retirado de documento 10-pee-1, p. 4, 16; P3-iasa-proj.pdf, p. 3)
    # O método na classe base pode esperar estado e estado_suc, ajustando assinatura.
    def custo(self, estado, estado_suc): # Assinatura completa
        # Retorna o quadrado do incremento associado a este operador.
        # O custo é independente dos estados inicial e final da transição neste caso.
        return self.__incremento ** 2
    
# Importa a classe base para respostas
from ecr.resposta import Resposta
# Importa a classe base para ações, especificando a intenção de agir numa direção
from sae.agente.accao import Accao

# Representa uma resposta simples que gera uma ação de movimento numa direção específica.
# Esta resposta é tipicamente associada a estímulos que indicam a desejabilidade
# de mover naquela direção (e.g., detetar um alvo).
class RespostaMover(Resposta):
    # Construtor da classe RespostaMover.
    # direccao: A direção na qual a ação de mover deve ser gerada.
    def __init__(self, direccao):
        # Inicializa a superclasse Resposta.
        # A ação associada a esta resposta é uma Accao (genérica) que encapsula
        # a direção alvo do movimento. A interpretação desta Accao (se é para
        # avançar ou rodar para essa direção) pode depender do contexto ou
        # da implementação do método _actuar do agente. Frequentemente, Accao(direccao)
        # implica avançar se já estiver virado para essa direção, ou rodar primeiro.
        # Aqui, simplesmente define a intenção de agir em relação a essa 'direccao'.
        super().__init__(Accao(direccao))

        # Comentários originais:
        # associa accao
        # que é uma accao com direccao
        # instanciamos accao nessa direccao
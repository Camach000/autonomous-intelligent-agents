# Importa a classe que define o estímulo para detetar alvos numa direção
from agente.controlo_react.reacoes.aproximar.estimulo_alvo import EstimuloAlvo
# Importa a classe que define a resposta de mover-se numa direção
from agente.controlo_react.reacoes.resposta.resposta_mover import RespostaMover
# Importa a classe base para uma reação simples
from ecr.reacao import Reaccao


# Representa uma reação simples (Estímulo-Resposta) para aproximar de um alvo
# numa direção específica.
# Uma reação é a unidade fundamental de um comportamento reativo, associando
# diretamente uma percepção (estímulo) a uma ação (resposta).
# Ver p.10 de 06-arq-react-1.pdf para a definição de Reação.
class AproximarDir(Reaccao):
    # Construtor da classe AproximarDir.
    # direccao: A direção específica na qual esta reação irá operar (e.g., Direccao.NORTE).
    def __init__(self, direccao):
        # Inicializa a superclasse Reaccao.
        # Uma Reaccao é composta por um Estímulo e uma Resposta.
        # Aqui, associa um EstimuloAlvo (para detetar alvos na 'direccao' dada)
        # com uma RespostaMover (para gerar a ação de mover nessa 'direccao').
        # Esta ligação direta é a essência da arquitetura reativa simples.
        super().__init__(
            EstimuloAlvo(direccao), # O componente que deteta a condição (alvo na direção)
            RespostaMover(direccao) # O componente que gera a ação (mover na direção)
        )
        #self.direcao = direcao
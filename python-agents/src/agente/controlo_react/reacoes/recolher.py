# Importa o comportamento composto para aproximar alvos (baseado em prioridade)
from agente.controlo_react.reacoes.aproximar.aproximar_alvo import AproximarAlvo
# Importa o comportamento composto para evitar obstáculos (baseado em hierarquia)
from agente.controlo_react.reacoes.evitar.evitar_obst import EvitarObst
# Importa o comportamento simples de exploração aleatória sem memória
from agente.controlo_react.reacoes.explorar.explorar import Explorar
# Importa o comportamento de exploração com memória

# Importa a classe base para comportamentos compostos hierárquicos (subsunção)
from agente.controlo_react.reacoes.explorar.explorar_com_memoria import ExplorarComMemoria
from ecr.hierarquia import Hierarquia

# Representa o comportamento global de nível mais alto do agente, "Recolher".
# Este comportamento coordena sub-comportamentos (Aproximar, Evitar, Explorar)
# usando uma arquitetura hierárquica (subsunção).
# O objetivo final (Recolher) é alcançado através da ativação priorizada destes
# sub-comportamentos que implementam sub-objetivos (p.14 de 08-arq-react-3.pdf).
# A classe Hierarquia gere a lógica de supressão/inibição entre as camadas.
# (ver p.11, p.12, p.15, p.17 de 07-arq-react-2.pdf).
class Recolher(Hierarquia):
    # Construtor da classe Recolher.
    def __init__(self):
        # Inicializa a superclasse Hierarquia com uma lista ordenada de comportamentos.
        # A ordem na lista define a hierarquia/prioridade:
        # 1. AproximarAlvo: Maior prioridade. Se um alvo é detetado e pode ser aproximado,
        #    esta camada tentará controlar o agente.
        # 2. EvitarObst: Prioridade intermédia. Se AproximarAlvo não estiver ativo (ou for
        #    suprimido por um obstáculo detetado por EvitarObst), esta camada tentará
        #    evitar colisões. Pode suprimir a exploração.
        # 3. ExplorarMemoria: Tenta explorar evitando estados recentes.
        # 4. Explorar: Menor prioridade (base). Ativado se nenhuma camada superior gerar
        #    uma ação (e.g., nenhum alvo visível, nenhum obstáculo iminente, e estado atual
        #    já na memória de ExplorarMemoria). Realiza movimento aleatório.
        # A classe Hierarquia implementa a lógica de como um comportamento de nível superior
        # pode suprimir a saída (ação) de um comportamento de nível inferior.
        super().__init__(
            [
                AproximarAlvo(),      # Nível 1 (Mais prioritário)
                EvitarObst(),         # Nível 2
                ExplorarComMemoria(),    # Nível 3 (Exploração com estado)
                Explorar()            # Nível 4 (Menos prioritário - Exploração sem estado)
            ]
        )
        
        #Alterado em relação a entrega anterior para melhor apresentação de comentários
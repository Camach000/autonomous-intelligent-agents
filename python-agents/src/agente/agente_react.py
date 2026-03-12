# A classe AgenteReactivo define um tipo de agente que opera com base no paradigma reativo.
# Agentes reativos tomam decisões com base em associações diretas entre as percepções atuais
# do ambiente e as ações a serem executadas, sem um planeamento deliberativo complexo ou
# uma representação interna extensa do mundo.
# Documentos Teóricos de Referência:
# - "06-arq-react-1.pdf" (Arquitetura de Agentes Reativos - Parte 1) - Introdução geral.
# - "07-arq-react-2.pdf" (Arquitetura de Agentes Reativos - Parte 2) - Mecanismos de reação, comportamentos.
# - "agentes_reactivos.pdf" (documento teórico do relatório original, equivalente ao 06-arq-react-1 e 07-arq-react-2) - Slides 2 e 6 sobre o modelo reativo.
# - "introd-ia.pdf" (documento teórico do relatório original) - Página 25 ("Modelo Reativo").

from agente.controlo_react.controlo_react import ControloReact
from agente.controlo_react.reacoes.recolher import Recolher
from sae.agente.agente import Agente # Classe base para todos os agentes da plataforma SAE

class AgenteReact(Agente):
    """
    AgenteReactivo é uma especialização da classe Agente da biblioteca SAE.
    Implementa um agente cujo comportamento é determinado por um ciclo de
    percepção-ação, mediado por um ControloReact. Este controlo ativa
    comportamentos (simples ou compostos) baseados diretamente na percepção atual.
    Este tipo de agente é adequado para ambientes dinâmicos onde respostas rápidas
    são mais importantes do que planos ótimos a longo prazo.
    """
    def __init__(self):
        """
        Construtor do AgenteReactivo.
        Inicializa o agente e configura o seu comportamento reativo principal.
        Neste caso, o comportamento padrão é `Recolher`, que é uma estrutura hierárquica
        de sub-comportamentos (AproximarAlvo, EvitarObst, Explorar).
        O `ControloReact` é responsável por ligar as percepções a este comportamento.
        """
        # Chama o construtor da classe base Agente da SAE.
        super().__init__()

        # Define o comportamento principal do agente.
        # A classe `Recolher` implementa uma arquitetura de subsunção (hierárquica)
        # onde comportamentos mais específicos (como aproximar de um alvo) têm prioridade
        # sobre comportamentos mais genéricos (como explorar).
        # Documento Teórico: "07-arq-react-2.pdf" - Slides 13-17 (Exemplo Tarefa de Prospecção);
        #                     "agentes_reativos_memoria.pdf" - Slides 15-17 (mesmo exemplo).
        comportamento = Recolher()

        # Instanciação do ControloReact, que faz a ponte entre a percepção
        # e a ativação do comportamento definido.
        # Documento Teórico: "07-arq-react-2.pdf" - Slide 11 (Agente com Controlo Reativo);
        #                     "agentes_reativos_memoria.pdf" - Slide 11.
        self.__controlo = ControloReact(comportamento)
    
    def executar(self):
        """
        Executa um ciclo de processamento do agente reativo.
        O ciclo consiste em:
        1. Percecionar o ambiente.
        2. Processar a perceção através do `ControloReact` para ativar o comportamento apropriado.
        3. Atuar no ambiente com a ação resultante.
        Este ciclo é direto e não envolve deliberação ou planeamento complexo.
        Documento Teórico: "06-arq-react-1.pdf" - Slide 6 (Ciclo Percepção-Reação-Acção).
        """
        # 1. Percecionar o ambiente.
        # Utiliza o método herdado da classe Agente (SAE) que, por sua vez, usa o Transdutor.
        percepcao = self._percepcionar()

        # 2. Processar a perceção.
        # O ControloReact ativa o comportamento principal (`Recolher`) com a percepção atual,
        # e este comportamento (sendo hierárquico) selecionará a ação mais apropriada
        # dos seus sub-comportamentos.
        accao = self.__controlo.processar(percepcao)

        # 3. Atuar no ambiente.
        # Executa a ação determinada pelo controlo reativo.
        self._actuar(accao)
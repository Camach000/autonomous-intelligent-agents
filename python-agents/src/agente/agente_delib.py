# A classe AgenteDelib representa um agente deliberativo.
# Um agente deliberativo é caracterizado pela sua capacidade de manter um modelo interno do mundo,
# deliberar sobre objetivos e planear sequências de ações para os alcançar.
# Esta abordagem contrasta com agentes puramente reativos, que respondem diretamente a estímulos.
# Documentos Teóricos de Referência:
# - "13-arq-delib.pdf" (Arquitetura de Agentes Deliberativos) - Slides 7, 8, 16 (arquitetura geral e ciclo de processamento)
# - "P4-iasa-proj.pdf" - Slides 3 (diagrama do ControloDelib)

from agente.controlo_delib.controlo_delib import ControloDelib
from plan.plan_pee.planeador_pee import PlaneadorPEE
from sae.agente.agente import Agente # Classe base para todos os agentes da plataforma SAE


class AgenteDelib(Agente):
    """
    AgenteDelib é uma especialização da classe Agente da biblioteca SAE.
    Implementa um agente com capacidade de deliberação e planeamento,
    utilizando um modelo interno do mundo e um planeador para tomar decisões.
    A sua inteligência reside na capacidade de raciocinar sobre os seus fins (objetivos)
    e os meios (planos) para os atingir.
    """

    def __init__(self):
        """
        Construtor do AgenteDelib.
        Inicializa os componentes internos do agente, incluindo o planeador
        e o módulo de controlo deliberativo.
        O planeador utilizado por defeito é o PlaneadorPee, que recorre à
        Procura em Espaço de Estados.
        O controlo deliberativo (ControloDelib) orquestra o ciclo de percepção,
        assimilação, deliberação, planeamento e execução.
        """
        super().__init__() # Chama o construtor da classe base Agente da SAE

        # Instanciação do PlaneadorPee. Este planeador é responsável por gerar planos
        # utilizando algoritmos de procura em espaço de estados, como A*.
        # Documento Teórico: "14-plan-pee.pdf"; "P4-iasa-proj.pdf" - Slide 9 (Planeador com Base em PEE)
        planeador = PlaneadorPEE()

        # Instanciação do ControloDelib, que encapsula a lógica principal do agente deliberativo.
        # Este controlo recebe o planeador como argumento e é responsável por:
        # 1. Manter e atualizar o ModeloMundo.
        # 2. Utilizar o MecDelib para definir objetivos.
        # 3. Utilizar o Planeador para gerar planos para esses objetivos.
        # Documento Teórico: "13-arq-delib.pdf" - Slides 13, 16; "P4-iasa-proj.pdf" - Slide 3
        self.__controlo = ControloDelib(planeador)

    def executar(self):
        """
        Executa um ciclo de processamento do agente deliberativo.
        Este ciclo é tipicamente composto por:
        1. Percecionar o ambiente para obter a informação mais recente.
        2. Processar essa perceção através do controlo deliberativo, que pode envolver:
           - Assimilar a nova informação no ModeloMundo.
           - Reconsiderar os objetivos e/ou o plano atual.
           - Deliberar novos objetivos (MecDelib).
           - Planear uma sequência de ações (Planeador).
        3. Visualizar o estado interno do agente (opcional, para depuração).
        4. Atuar no ambiente, executando a próxima ação do plano.
        Este ciclo de perceção-deliberação-ação é central na arquitetura deliberativa.
        Documento Teórico: "13-arq-delib.pdf" - Slide 13 ("Processo Geral de Tomada de Decisão e Acção")
                            e Slide 16 (Diagrama do Controlo Deliberativo).
        """
        # 1. Observar o ambiente: obtém a percepção atual através do transdutor.
        # O transdutor é um componente da classe Agente (SAE) responsável pela interface sensorial.
        percepcao = self._percepcionar()

        # 2. Deliberar e Planear: o controlo deliberativo processa a percepção.
        # Internamente, o ControloDelib irá atualizar o ModeloMundo,
        # deliberar sobre objetivos (MecDelib), e planear (Planeador) se necessário.
        # Retorna a ação a ser executada no passo atual.
        accao = self.__controlo.processar(percepcao)

        # (Opcional) Mostrar o estado do modelo do mundo na vista associada.
        # A vista (`self.vista`) é um atributo da classe Agente (SAE) que pode ser
        # utilizado para visualização e depuração do estado interno do agente.
        if self.vista: # Verifica se uma vista foi configurada para este agente
            self.__controlo.mostrar(self.vista)

        # 3. Executar a ação: atua no ambiente com base na ação decidida.
        # O método _actuar é da classe Agente (SAE) e utiliza o transdutor para
        # efetivar a ação no ambiente simulado.
        self._actuar(accao)
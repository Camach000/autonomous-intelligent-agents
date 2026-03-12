# A classe ControloReact implementa a lógica de controlo para um agente reativo.
# Num agente reativo, as ações são geradas como uma resposta direta às percepções
# do ambiente, sem um processo de deliberação ou planeamento a longo prazo.
# Este controlo recebe um comportamento (que pode ser simples ou composto) e
# ativa-o com a percepção atual para obter uma ação.
# Documentos Teóricos de Referência:
# - "07-arq-react-2.pdf" - Slide 11 (Diagrama "Agente com Controlo Reativo")
# - "agentes_reativos_memoria.pdf" - Slide 11 (Mesmo diagrama)
# - "P2-iasa-proj.pdf" - Contexto da Parte 2, focada em agentes reativos.

# (Nota: As docstrings originais já eram bastante descritivas e alinhadas com a teoria.
#  Mantive a estrutura, adicionando referências explícitas.)

class ControloReact:
    """
    O ControloReact é o componente de um agente reativo que faz a ponte
    entre as percepções do ambiente e o comportamento do agente.
    Ele não realiza planeamento complexo; em vez disso, ativa um comportamento
    pré-definido (que pode ser uma reação simples ou um conjunto hierárquico/prioritário
    de reações) com base na percepção atual para gerar uma ação imediata.
    A sua função é central no ciclo percepção-ação de um agente reativo.
    (Ref: "06-arq-react-1.pdf", Slide 6, "Arquitetura de Agentes Reativos";
          "introd-ia.pdf" do relatório anterior, pág. 25, "Modelo Reativo")
    """
    def __init__(self, comportamento):
        """
        Construtor do ControloReact.
        @param comportamento: O comportamento (instância de uma subclasse de `Comportamento` da lib ECR)
                             que será ativado para processar as percepções. Pode ser um comportamento
                             simples (e.g., `Explorar`) ou composto (e.g., `Recolher`, que é uma `Hierarquia`).
        """
        self.__comportamento = comportamento

    def processar(self, percepcao):
        """
        Processa uma dada percepção e retorna a ação resultante.
        Este método é o núcleo do ciclo de decisão do agente reativo.
        Ele simplesmente delega a decisão de qual ação tomar ao `comportamento`
        associado, passando a `percepcao` atual.
        @param percepcao: A percepção atual do ambiente, obtida pelo agente.
        @return: A ação determinada pelo comportamento ativado.
        (Ref: "07-arq-react-2.pdf", Slide 11, o fluxo do "Processar" no Controlo Reativo)
        """
        # Ativa o comportamento principal do agente com a percepção atual.
        # O método `activar` do comportamento é responsável por determinar a ação apropriada.
        accao = self.__comportamento.activar(percepcao)
        return accao
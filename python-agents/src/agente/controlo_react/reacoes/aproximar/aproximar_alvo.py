# Importa a classe base para a reação de aproximação direcional
from agente.controlo_react.reacoes.aproximar.aproximar_dir import AproximarDir
# Importa a classe base para comportamentos compostos baseados em prioridade
from ecr.prioridade import Prioridade
# Importa o enum Direccao para iterar sobre as direções possíveis
from sae import Direccao

# Representa um comportamento composto para aproximar-se de um alvo.
# Este comportamento agrega múltiplas reações direcionais (AproximarDir)
# e utiliza um mecanismo de seleção de ação baseado em prioridade.
# A reação direcional com maior prioridade (determinada pela intensidade
# do estímulo, que por sua vez depende da proximidade do alvo) será selecionada.
# Refere-se à coordenação de comportamentos/reações num comportamento composto,
# especificamente usando seleção por prioridade (ver p.7, p.9 de 08-arq-react-3.pdf).
class AproximarAlvo(Prioridade):
    # Construtor da classe AproximarAlvo.
    def __init__(self):
        # Inicializa a superclasse Prioridade.
        # A Prioridade requer uma lista de comportamentos/reações que ela irá gerir.
        # Cria uma instância de AproximarDir para cada direção possível (NORTE, SUL, ESTE, OESTE).
        # Cada AproximarDir é uma reação simples que tenta mover o agente numa direção específica se um alvo for detectado.
        # A classe Prioridade selecionará a ação da instância AproximarDir que reportar a maior intensidade/prioridade.
        # Esta é uma forma de implementar o sub-objetivo "Aproximar Alvo" (p.14 de 08-arq-react-3.pdf)
        # agregando reações mais simples.
        super().__init__(
            # A list comprehension cria eficientemente as 4 instâncias de AproximarDir.
            [AproximarDir(direccao) for direccao in Direccao]
        )
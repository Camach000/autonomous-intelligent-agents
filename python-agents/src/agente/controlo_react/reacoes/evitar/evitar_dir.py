# Importa a classe que define o estímulo para detetar obstáculos numa direção
from agente.controlo_react.reacoes.evitar.estimulo_obst import EstimuloObst
# Importa a classe que define a resposta de evitar (geralmente rodar)
from agente.controlo_react.reacoes.evitar.resposta_evitar import RespostaEvitar
# Importa a classe base para uma reação simples (Estímulo-Resposta)
from ecr.reacao import Reaccao
# A classe Hierarquia não é usada diretamente aqui, talvez fosse para outro propósito.
# from ecr.hierarquia import Hierarquia

# Representa uma reação simples (Estímulo-Resposta) para evitar um obstáculo
# detetado numa direção específica.
# Associa a deteção de um obstáculo com a ação de evitá-lo.
class EvitarDir(Reaccao):
    # Construtor da classe EvitarDir.
    # direccao: A direção específica na qual esta reação irá operar.
    def __init__(self, direccao):
        # Cria a instância do estímulo para detetar obstáculos nesta direção.
        estimulo = EstimuloObst(direccao)
        # Cria a instância da resposta para gerar a ação de evitar (associada a este estímulo).
        # Passa o estímulo para a resposta, o que é um padrão menos comum, mas pode
        # ser usado pela resposta para obter informações do estímulo se necessário.
        # No entanto, a RespostaEvitar original parece esperar uma direção, não um estímulo.
        # Assumindo que RespostaEvitar foi adaptada ou que o estímulo contém a direção.
        resposta = RespostaEvitar(direccao) # Ou talvez RespostaEvitar(direccao)? Verificar RespostaEvitar.

        # Inicializa a superclasse Reaccao com o par estímulo-resposta criado.
        super().__init__(estimulo, resposta)
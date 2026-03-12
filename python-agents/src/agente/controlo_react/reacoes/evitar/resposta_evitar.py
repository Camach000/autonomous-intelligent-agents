from ecr.resposta import Resposta
from sae.agente.accao import Accao
from sae.agente.rodar import Rodar

class RespostaEvitar(Resposta):
    """
    A classe "RespostaEvitar" implementa uma "Resposta" específica para gerar uma
    ação de evitar um obstáculo. Quando ativada, e se um obstáculo for detectado
    na direção atual da percepção, esta resposta gera uma ação de "Rodar" para
    uma nova direção.
    Esta resposta é usada pelo comportamento "EvitarDir".
    """
    
    def __init__(self, direccao):
        super().__init__(Accao(direccao))

    def activar(self, percepcao, intensidade):
        """
        Ativa a resposta para evitar um obstáculo.
        "percepcao": A percepção atual do ambiente.
        "intensidade": A intensidade do estímulo de obstáculo (geralmente 1 se detectado).

        Se houver contacto com um obstáculo na direção atual da percepção,
        a resposta calcula uma nova direção rodando a partir da direção atual
        e define a "_accao" como um "Rodar" para essa nova direção.
        Depois, chama o "activar" da superclasse para definir a prioridade e retornar a ação.
        """
        direccao_atual = percepcao.direccao
        if percepcao.contacto_obst(direccao_atual):
            nova_direccao = direccao_atual.rodar()
            self._accao = Rodar(nova_direccao)
            return super().activar(percepcao, intensidade)

            
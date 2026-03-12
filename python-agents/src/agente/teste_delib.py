from agente.controlo_delib.mec_delib import MecDelib
from mod.estado_agente import EstadoAgente
from mod.modelo_mundo import ModeloMundo
from plan.plan_pee.planeador_pee import PlaneadorPEE
from sae.ambiente.ambiente import Ambiente
from sae.agente.transdutor import Transdutor
from sae.defamb import DEF_AMB

def obter_percepcao():
    num_ambiente = 4
    ambiente = Ambiente(DEF_AMB[num_ambiente])
    transdutor = Transdutor()
    transdutor.iniciar(ambiente)
    return transdutor.percepcionar()

def actualizar_modelo_mundo():
    """
    Teste de actualização do modelo do mundo

    >>> modelo_mundo = actualizar_modelo_mundo()
    >>> modelo_mundo.alterado
    True

    >>> estado = modelo_mundo.obter_estado()
    >>> estado.posicao
    (0, 0)

    >>> estados = modelo_mundo.obter_estados()
    >>> len(estados)
    671

    >>> operadores = modelo_mundo.obter_operadores()
    >>> len(operadores)
    4

    >>> estado = EstadoAgente((28, 9))
    >>> modelo_mundo.obter_elemento(estado)
    <Elemento.ALVO: 'A'>
    """
    percepcao = obter_percepcao()
    modelo_mundo = ModeloMundo()
    modelo_mundo.actualizar(percepcao)
    return modelo_mundo

def gerar_objetivos():
    """
    >>> objetivos = gerar_objetivos()
    >>> len(objetivos)
    3
    """
    modelo_mundo = actualizar_modelo_mundo()
    mec_delib = MecDelib(modelo_mundo)
    return mec_delib.deliberar()

def gerar_plano():
    """
    >>> plano = gerar_plano()
    >>> plano.dimensao
    37
    """
    planeador = PlaneadorPEE()
    modelo_mundo = actualizar_modelo_mundo()
    objetivos = gerar_objetivos()
    return planeador.planear(modelo_mundo, objetivos)

#Executar teste
if __name__ == "__main__":
    import doctest
    doctest.testmod()
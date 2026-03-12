"""
A classe "MecDelib" (Mecanismo de Deliberação) é responsável pela componente de deliberação
do agente. A sua função é "decidir o que fazer", ou seja, gerar e selecionar os objetivos
que o agente deve perseguir. Este conceito é apresentado no slide 11 da apresentação
"ARQUITECTURA DE AGENTES DELIBERATIVOS" sob "RACIOCÍNIO SOBRE FINS (DELIBERAÇÃO)".

No contexto do "Projecto - Parte 4", o slide 3 ("CONTROLO DELIBERATIVO") mostra
"MecDelib" interagindo com o "ModeloMundo" para obter a informação necessária para deliberar.
Mais especificamente, no "EXEMPLO: AGENTE DE RECOLHA DE ALVOS" (slide 1 e 2),
o mecanismo deliberativo gera objetivos (estados a atingir) com base nos alvos
presentes no "Modelo do Mundo" e na sua distância ao agente.
"""

from sae.ambiente.elemento import Elemento

class MecDelib():

    def __init__(self, modelo_mundo):
        """
        Inicializa o mecanismo de deliberação.
        Recebe uma referência ao "modelo_mundo" para poder aceder à informação
        sobre o estado atual do ambiente e do agente.
        """
        self.__modelo_mundo = modelo_mundo
    
    def deliberar(self):
        """
        Processo principal de deliberação.
        Primeiro, gera um conjunto de potenciais objetivos (todos os alvos no mundo).
        Depois, seleciona e ordena esses objetivos.
        Retorna uma lista de objetivos ordenada (por exemplo, por proximidade) ou "None"
        se não houverem objetivos.
        Isto corresponde a "Gerar objectivos: estados que devem ser atingidos"
        (Slide 1 da apresentação "EXEMPLO: AGENTE DE RECOLHA DE ALVOS").
        """
        objetivos = self.__gerar_objetivos()
        if objetivos:
            return self.__selecionar_objetivos(objetivos)
        else:
            return None

    def __gerar_objetivos(self):
        """
        Gera uma lista de todos os estados que são "ALVO" no modelo do mundo.
        Estes são os potenciais objetivos que o agente pode perseguir.
        """
        return [estado for estado in self.__modelo_mundo.obter_estados() 
                if self.__modelo_mundo.obter_elemento(estado) == Elemento.ALVO]

    def __selecionar_objetivos(self, conjunto_objetivos):
        """
        Seleciona e ordena os objetivos. Neste caso, ordena os objetivos
        pela distância ao agente (do mais próximo ao mais distante),
        utilizando o método "distancia" do "modelo_mundo".
        A ordenação é uma forma de priorizar os objetivos.
        (Slide 1 da apresentação "EXEMPLO: AGENTE DE RECOLHA DE ALVOS" menciona "Distância
        entre um estado e o estado actual do agente").
        """
        conjunto_objetivos.sort(key = self.__modelo_mundo.distancia)
        return conjunto_objetivos
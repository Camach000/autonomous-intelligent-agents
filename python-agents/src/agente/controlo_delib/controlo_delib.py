"""
Esta classe, "ControloDelib", representa o ciclo de controlo deliberativo de um agente autónomo,
tal como ilustrado no slide 3 ("CONTROLO DELIBERATIVO") da apresentação "Projecto - Parte 4".
Ela orquestra as interações entre o "ModeloMundo", o "MecDelib" (Mecanismo de Deliberação)
e o "Planeador".

O método principal, "processar", implementa o ciclo de tomada de decisão e ação que um agente
deliberativo executa. Este ciclo é detalhado no slide 6 ("CONTROLO DELIBERATIVO: PROCESSAR")
da apresentação "Projecto - Parte 4", e também nos slides 13 e 15 da apresentação
"ARQUITECTURA DE AGENTES DELIBERATIVOS". O ciclo envolve:
1.  "Assimilar" a percepção, que corresponde a "Observar" o mundo e "Actualizar" o modelo interno.
2.  "Reconsiderar" se é necessário reavaliar os objetivos e o plano. Esta etapa é crucial
    devido ao dinamismo do ambiente ou limitações de recursos, como explicado no slide 14
    da apresentação "ARQUITECTURA DE AGENTES DELIBERATIVOS" sobre "RECONSIDERAÇÃO (DE OPÇÕES)".
3.  Se a reconsideração for positiva, o agente vai "Deliberar" para definir novos objetivos
    e "Planear" para encontrar uma sequência de ações para atingi-los.
4.  Finalmente, "Executar" a próxima ação do plano.

A arquitetura modular, com um "Controlo Deliberativo" central que gere o "Modelo do Mundo",
o "Mecanismo de Deliberação" e o "Planeador", é também visível no slide 16 da apresentação
"ARQUITECTURA DE AGENTES DELIBERATIVOS".
"""

from agente.controlo_delib.mec_delib import MecDelib
from mod.modelo_mundo import ModeloMundo
from plan.planeador import Planeador

class ControloDelib():

    def __init__(self, planeador):
        """
        Inicializa o controlo deliberativo.
        Recebe uma instância de um "Planeador".
        Internamente, cria e mantém instâncias do "ModeloMundo" e do "MecDelib".
        Esta composição reflete a estrutura mostrada no diagrama de classes do slide 3
        ("CONTROLO DELIBERATIVO") da apresentação "Projecto - Parte 4".
        """
        self.__modelo_mundo = ModeloMundo()
        self.__mec_delib = MecDelib(self.__modelo_mundo)
        self.__planeador = planeador
        self.__objetivos = None
        self.__plano = None

    def processar(self, percepcao):
        """
        Método central que executa um ciclo do processo deliberativo.
        Corresponde ao diagrama de atividade do slide 6 ("CONTROLO DELIBERATIVO: PROCESSAR")
        da apresentação "Projecto - Parte 4".
        Recebe uma "percepcao" do ambiente.
        Retorna uma "Accao" a ser executada no ambiente.
        """
        self.__assimilar(percepcao)
        if self.__reconsiderar():
            self.__deliberar()
            self.__planear()
        return self.__executar()

    def __assimilar(self, percepcao):
        """
        Assimila a percepção, atualizando o modelo do mundo.
        Esta é a fase de "Actualizar o modelo do mundo" do ciclo de decisão
        (slide 13 e 15 da apresentação "ARQUITECTURA DE AGENTES DELIBERATIVOS").
        """
        self.__modelo_mundo.actualizar(percepcao)

    def __reconsiderar(self):
        """
        Verifica se é necessário reconsiderar os objetivos e o plano.
        A reconsideração ocorre se o modelo do mundo foi alterado pela percepção mais
        recente ou se não existe um plano ativo.
        Este passo é fundamental para a adaptação do agente a ambientes dinâmicos
        (slide 14 e 15 da apresentação "ARQUITECTURA DE AGENTES DELIBERATIVOS").
        """
        return self.__modelo_mundo.alterado or self.__plano is None

    def __deliberar(self):
        """
        Invoca o mecanismo de deliberação ("MecDelib") para definir os objetivos atuais.
        A deliberação foca-se em "decidir o que fazer", gerando um conjunto de objetivos.
        (Slide 11 da apresentação "ARQUITECTURA DE AGENTES DELIBERATIVOS" sobre
        "RACIOCÍNIO SOBRE FINS (DELIBERAÇÃO)").
        No "Projecto - Parte 4", slide 3, o "MecDelib" é o componente responsável por esta tarefa.
        """
        self.__objetivos = self.__mec_delib.deliberar()

    def __planear(self):
        """
        Invoca o planeador para gerar um plano para atingir os objetivos definidos.
        Se existirem objetivos, o "Planeador" utiliza o "ModeloMundo" (que implementa
        a interface "ModeloPlan") para encontrar uma sequência de ações.
        (Slide 11 da apresentação "ARQUITECTURA DE AGENTES DELIBERATIVOS" sobre
        "RACIOCÍNIO SOBRE MEIOS (PLANEAMENTO)").
        (Slide 7 da apresentação "Projecto - Parte 4" sobre "PLANEAMENTO AUTOMÁTICO").
        """
        if self.__objetivos:
            self.__plano = self.__planeador.planear(self.__modelo_mundo, self.__objetivos)
        else:
            self.__plano = None

    def __executar(self):
        """
        Executa a próxima ação do plano.
        Obtém a ação apropriada do plano com base no estado atual do agente
        (retirado do "ModeloMundo").
        Se não houver plano ou ação, nada é retornado.
        (Slide 13 e 15 da apresentação "ARQUITECTURA DE AGENTES DELIBERATIVOS").
        """
        if self.__plano:
            estado = self.__modelo_mundo.obter_estado()
            operador = self.__plano.obter_accao(estado)
            if operador:
                return operador.accao
            else:
                self.__plano = None

    def mostrar(self, vista):
        """
        Utilizado para visualização do estado interno do agente e do seu processo.
        Mostra o "ModeloMundo", o "Plano" (se existir) e os "Objetivos".
        """
        vista.limpar()
        self.__modelo_mundo.mostrar(vista)
        if self.__plano:
            self.__plano.mostrar(vista)
        if self.__objetivos:
            for objetivo in self.__objetivos:
                vista.marcar_posicao(objetivo.posicao)
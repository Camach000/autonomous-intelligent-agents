#import sys

#print ("...")
#print (sys.path)
#print ("...")

from agente.agente_delib import AgenteDelib
from agente.agente_delib_pdm import AgenteDelibPDM
from agente.agente_react import AgenteReact
from sae import Simulador

#agente = AgenteReact()
#simulador = Simulador(1, None)
#simulador = Simulador(1, agente)
#simulador.executar()

#Activação do Agente
agente = AgenteDelibPDM()
simulador = Simulador(4, agente, vista_modelo = True)
simulador.executar()
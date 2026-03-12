

from agente.controlo_delib.controlo_delib import ControloDelib
from plan.plan_pdm.planeador_pdm import PlaneadorPDM
from sae import Agente

class AgenteDelibPDM(Agente):
    
    def __init__(self):
        super().__init__()
        planeador = PlaneadorPDM()
        self.__controlo = ControloDelib(planeador)
        
    def executar(self):
        percepcao = self._percepcionar()
        accao = self.__controlo.processar(percepcao)
        self.__controlo.mostrar(self.vista)
        self._actuar(accao)
        
    
        
    
         
         
    
       




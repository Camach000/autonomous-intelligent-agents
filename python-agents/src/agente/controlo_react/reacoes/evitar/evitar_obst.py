# Importa a classe para a reação de evitar direcional
from agente.controlo_react.reacoes.evitar.evitar_dir import EvitarDir
# Importa a classe base para comportamentos compostos hierárquicos (subsunção)
from ecr.hierarquia import Hierarquia
# Importa o enum Direccao para iterar sobre as direções possíveis
from sae.ambiente.direccao import Direccao

# Representa um comportamento composto para evitar obstáculos.
# Agrega múltiplas reações direcionais (EvitarDir) numa estrutura hierárquica.
# Na arquitetura de subsunção, comportamentos como "Evitar Obstáculos" formam
# camadas de competência que podem suprimir ou inibir camadas inferiores (como "Explorar").
# Ver p.11, p.15, p.17 de 07-arq-react-2.pdf. A classe Hierarquia implementa essa lógica.
class EvitarObst(Hierarquia):
    # Construtor da classe EvitarObst.
    def __init__(self):
        # Inicializa a superclasse Hierarquia.
        # A Hierarquia requer uma lista de comportamentos/reações ordenados por prioridade
        # (ou nível de competência). Neste caso, agrega reações EvitarDir para todas as direções.
        # A lógica interna da Hierarquia determinará qual, se alguma, destas reações
        # deve ser ativada e possivelmente suprimir outras de níveis inferiores.
        # A ordem dentro desta lista pode não importar se todas as EvitarDir tiverem
        # a mesma prioridade dentro desta camada hierárquica.
        super().__init__(
            # Cria uma instância de EvitarDir para cada direção possível.
            [EvitarDir(direccao) for direccao in Direccao]
        )
        
        #codigo anterior possivel causa de erro:
        # self.__comportamentos = [[EvitarDir(direccao) for direccao in Direccao]]
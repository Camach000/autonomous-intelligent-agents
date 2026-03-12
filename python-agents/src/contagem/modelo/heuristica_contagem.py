from contagem.modelo.estado_contagem import EstadoContagem
from contagem.modelo.problema_contagem import ProblemaContagem
from pee.melhor_prim.heuristica import Heuristica

# Define a classe HeuristicaContagem, que implementa uma função heurística h(n)
# específica para o ProblemaContagem. Herda da classe base Heuristica.
# Uma heurística estima o custo do estado atual até o objetivo, guiando procuras informadas.
# (retirado de documento 12-pee-3, p. 15, 16; P3-iasa-proj.pdf, p. 14)
class HeuristicaContagem(Heuristica):
    # Construtor. Recebe a instância do problema para poder aceder ao estado final.
    def __init__(self, valor_final):
        self._valor_final = valor_final

    # Implementa o método 'h' da interface Heuristica.
    # Calcula a estimativa de custo do 'estado' atual até o objetivo.
    # (retirado de documento 12-pee-3, p. 15)
    def h(self, estado):
        # A heurística implementada é a diferença absoluta entre o valor do estado atual
        # e o valor final definido no problema. Esta é uma estimativa da "distância" restante.
        # Para ser admissível em A*, h(n) <= h*(n). Aqui, h*(n) seria o custo real mínimo
        # para ir de estado.valor até problema._ProblemaContagem__valor_final.
        # Se os custos dos operadores fossem 1, esta heurística seria a distância de Manhattan unidimensional,
        # que é admissível e consistente. Com custo = incremento**2, a admissibilidade depende.
        # Ex: estado=10, final=20, inc=[5]. h(10)=10. Custo real é 5**2 = 25. h <= h* OK.
        # Ex: estado=18, final=20, inc=[2]. h(18)=2. Custo real é 2**2 = 4. h <= h* OK.
        # Parece admissível para operadores de incremento.
        # (retirado de documento 12-pee-3, p. 20, 27 - Admissibilidade, Consistência)
        return abs(self._valor_final - estado.valor) # Acesso ao atributo privado do problema
    
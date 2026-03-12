
from pee.melhor_prim.aval.avaliador_sof import AvaliadorSof
from pee.melhor_prim.procura_custo_uniforme import ProcuraCustoUnif
from pee.melhor_prim.procura_sofrega import ProcuraSofrega
from pee.prof.procura_prof_iter import ProcuraProfIter
from pee.prof.procura_prof_lim import ProcuraProfLim
from pee.prof.procura_profundidade import ProcuraProfundidade
from pee.larg.procura_largura import ProcuraLargura
from contagem.modelo.problema_contagem import ProblemaContagem

valor_inicial = 0
valor_final = 9
incrementos = [1, 2, -1]

problema = ProblemaContagem(valor_inicial, 
                            valor_final, 
                            incrementos)

"""mecanismo_procura_prof = ProcuraProfundidade()"""
"""mecanismo_procura_larg = ProcuraLargura()"""
"""mecanismo_procura_prof_lim = ProcuraProfLim()"""
"""mecanismo_procura_prof_iter = ProcuraProfIter()"""
mecanismo_procura_custo_unif = ProcuraCustoUnif()
"""solucao_prof = mecanismo_procura_prof.procurar(problema)"""
"""solucao_larg = mecanismo_procura_larg.procurar(problema)"""
"""solucao_prof_lim = mecanismo_procura_prof_lim.procurar(problema)"""
"""solucao_prof_iter = mecanismo_procura_prof_iter.procurar(problema)"""
solucao_custo_unif = mecanismo_procura_custo_unif.procurar(problema)

def imprimir_solucao(solucao, tipo_procura):
    if solucao:
        print(f"--- Solução ({tipo_procura}) ---")
        print(f"Dimensão da solução: {solucao.dimensao}")
        print(f"Custo da solução: {solucao.custo}")
        print("Passos")
        for passo in solucao:
            print(f"Estado: {passo.estado.valor}")
            print(f"Operador: {passo.operador.incremento}")

"""imprimir_solucao(solucao_prof, "Profundidade")
print(f"Nós processados: {mecanismo_procura_prof.nos_processados}") # valor apresentado = 16
print(f"Nós em memória: {mecanismo_procura_prof.nos_em_memoria}") # valor apresentado = 16"""

"""imprimir_solucao(solucao_larg, "Largura")
print(f"Nós processados: {mecanismo_procura_larg.nos_processados}") # valor apresentado = 484
print(f"Max nós em memória: {mecanismo_procura_larg.nos_em_memoria}") # valor apresentado = 484, valor igual
porque os nós mesmo depois de serem expandidos não são elimidados porque os nós sucessores tem uma referância
para o antecessor, e isto repete-se para toda a árvore
Dimensão = 5, a procura em largura exige que a solução seja atendida com o número mínimo de passos
Custo = 17, o número 
"""

"""imprimir_solucao(solucao_prof_lim, "Profundidade com Limite")
print(f"Nós processados: {mecanismo_procura_prof_lim.nos_processados}") # valor apresentado = 190
print(f"Max nós em memória: {mecanismo_procura_prof_lim.nos_em_memoria}") # valor apresentado = 14 (errado, devia ser 17), 
a procura em profundidade segue por um ramo e aprofunda-o, neste caso está limitado a 5, o que faz com que 5*3 (operadores) = 15,
+ 1 que é o nó raiz = 16, e o 17 tem que ver com o algoritmo (o nó a mais corresponde a um nó que está ser processado, e que por
isso não foi apagado)
Dimensão  = 5
Custo = 20, 5 * 4 = 20, o custo é o número de passos multiplicado pelo número de incrementos
"""

"""imprimir_solucao(solucao_prof_iter, "Profundidade Iterativa")
print(f"Nós processados: {mecanismo_procura_prof_iter.nos_processados}") # valor apresentado = 190
print(f"Max nós em memória: {mecanismo_procura_prof_iter.nos_em_memoria}") # valor apresentado = 14 (errado, devia ser 17), 
a procura em profundidade segue por um ramo e aprofunda-o, neste caso está limitado a 5, o que faz com que 5*3 (operadores) = 15,
+ 1 que é o nó raiz = 16, e o 17 tem que ver com o algoritmo (o nó a mais corresponde a um nó que está ser processado, e que por
isso não foi apagado)
Dimensão  = 5
Custo = 20, 5 * 4 = 20, o custo é o número de passos multiplicado pelo número de incrementos
"""

imprimir_solucao(solucao_custo_unif, "Custo Uniforme")
print(f"Nós processados: {mecanismo_procura_custo_unif.nos_processados}") 
print(f"Max nós em memória: {mecanismo_procura_custo_unif.nos_em_memoria}")
# esta linha de código foi implementada a pedido do professor, durante a aula de 06/05/2025
# e serve para exatamente verificar o numero de estados repetidos que foram processados
# só é aplicável às procuras do tipo melhor primeiro
# as alterações feitas ao código para este cálculo foram feitas na classe "ProcuraMelhorPrim"
print(f"Número de estados repetidos: {mecanismo_procura_custo_unif.estados_repetidos}")


# NOTA: A implementação para a procura sofrega e AA ainda não funciona, pelo que não foi feito o teste


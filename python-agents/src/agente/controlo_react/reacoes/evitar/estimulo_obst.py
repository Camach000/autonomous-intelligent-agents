# Importa a classe base para estímulos
from ecr.estimulo import Estimulo

# Representa o estímulo para detetar um obstáculo adjacente numa direção específica.
# Este é um estímulo binário (presente/ausente), retornando uma intensidade fixa se ativado.
# Faz parte da reação de evitar obstáculos.
# Nota: O comentário original indicava falta de herança, mas o código herda de Estimulo.
class EstimuloObst(Estimulo):
    # Construtor da classe EstimuloObst.
    # direccao: A direção específica a ser verificada na percepção.
    # intensidade: A intensidade a ser retornada se o obstáculo for detetado (default 1).
    #              Como é binário, geralmente é 1 ou 0.
    def __init__(self, direccao,  intensidade = 1):
        # Nota: O comentário original mencionava 'private' removido, o atributo é público.
        self.__direccao = direccao
        self.__intensidade = intensidade # Intensidade é privada

    # Método para detetar o estímulo numa dada percepção.
    # percepcao: Objeto contendo a informação sensorial atual do agente.
    # Retorna: A intensidade definida no construtor se houver contacto com obstáculo
    #          na direção especificada, caso contrário retorna 0.
    def detectar(self, percepcao):
        # Utiliza um método da percepção para verificar contacto direto com obstáculo.
        # Nota: O comentário original corrigia percepcao.direccao para self.direccao, o que está correto.
        if percepcao.contacto_obst(percepcao.direccao):
            # Obstáculo detetado, retorna a intensidade configurada.
            return self.__intensidade
        else:
            # Nenhum obstáculo em contacto, retorna 0.
            # O comentário original tinha 'return 0' comentado, mas o else é necessário.
            return 0
        
        #código anterior estava a gerar erro:
        #def detectar(self, percepcao):
        #elemento, distancia = percepcao[self.__direcao]
        #return self.__intensidade if percepcao.contacto_obst(self.__direcao) else 0.0
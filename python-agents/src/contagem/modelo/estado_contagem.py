from mod.estado import Estado

# Define a classe EstadoContagem, que representa um estado no problema de contagem.
# Herda da classe base Estado, fornecendo uma implementação concreta.
# Um estado neste problema é caracterizado unicamente pelo valor numérico atual do contador.
# (retirado de documento 10-pee-1, p. 4, 29; P3-iasa-proj.pdf, p. 3)
class EstadoContagem(Estado):
    # Construtor. Recebe o valor inicial do contador para este estado.
    def __init__(self, valor):
        # Armazena o valor do contador num atributo privado.
        self.__valor = valor

    # Método para gerar um identificador único (hash) para o estado.
    # Essencial para utilizar o estado como chave em dicionários ou conjuntos,
    # como na memória de explorados da ProcuraGrafo, permitindo verificar
    # eficientemente se um estado já foi visitado. A identificação deve ser
    # baseada no valor que define o estado.
    # (retirado de documento P3-iasa-proj.pdf, p. 3 - id_valor(); 10-pee-1, p. 27)
    def id_valor(self):
        # Retorna o hash do valor numérico do contador.
        # Estados com o mesmo valor terão o mesmo hash.
        return self.__valor

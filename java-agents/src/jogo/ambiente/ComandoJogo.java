package jogo.ambiente;

import ambiente.Comando;

/**
 * Enumeração que define os possíveis comandos do jogo.
 * Esta enumeração implementa a interface {@link Comando} e representa
 * as ações que o agente pode executar no ambiente do jogo.
 * A utilização de uma enumeração garante que os comandos são definidos
 * de forma consistente e que não existem valores inválidos.
 *
 * O uso de um enum garante a unicidade e a imutabilidade dos comandos,
 * promovendo a segurança e a previsibilidade do sistema.
 */
public enum ComandoJogo implements Comando {
    PROCURAR,    // Comando para procurar
    APROXIMAR,   // Comando para aproximar
    OBSERVAR,    // Comando para observar
    FOTOGRAFAR;  // Comando para fotografar

    /**
     * Exibe o comando atual na consola.  Este método implementa a interface
     * {@link Comando} e permite exibir informações sobre o comando.
     */
    @Override
    public void mostrar() {
        System.out.printf("\nAccao: %s\n", this); //imprimir na consola o nome do comando
    }
}
package agente;

import ambiente.Comando;

/**
 * A classe `Accao` representa uma ação concreta que um agente pode realizar no ambiente.
 * Ela encapsula um {@link Comando}, definindo a operação específica a ser executada.
 * No contexto de arquiteturas de software baseadas em agentes, a separação entre `Accao` e `Comando`
 * é fundamental para promover a modularidade e a reutilização.  Esta separação adere ao
 * princípio da responsabilidade única (SRP), onde `Accao` representa a intenção do agente,
 * enquanto `Comando` representa a implementação da ação no ambiente.
 *
 * Esta classe atua como um intermediário entre o agente e o ambiente, garantindo que
 * as ações sejam executadas de forma controlada e consistente.
 */
public class Accao {
    /**
     * O {@link Comando} específico associado a esta ação, representando a operação
     * a ser executada no ambiente. Segundo o princípio da abstração, este atributo representa o
     * essencial da ação a ser tomada pelo agente, ocultando os detalhes de implementação.
     *
     * Este atributo é imutável após a criação da instância, garantindo a integridade
     * da ação.
     */
    private Comando comando;

    /**
     * Construtor da classe `Accao`.
     *
     * @param comando O {@link Comando} associado à ação. Este parâmetro é essencial
     *                para definir a ação que será executada no ambiente.
     */
    public Accao(Comando comando) {
        this.comando = comando;
    }

    /**
     * Retorna o {@link Comando} associado a esta ação.
     *
     * @return O {@link Comando} que representa a ação a ser executada.  Este método
     *         permite que o ambiente execute o comando apropriado.
     */
    public Comando getComando() {
        return comando;
    }
}
package agente;

import ambiente.Evento;

/**
 * A classe `Percepcao` representa a percepção do agente sobre o ambiente.
 * Encapsula um {@link Evento}, que representa um evento ocorrido no ambiente.
 * Percepções são utilizadas pelo módulo de controle ({@link Controlo}) para tomar decisões
 * sobre qual ação executar.  Esta classe atua como um "sensor" do agente,
 * fornecendo informações sobre o estado do ambiente.
 */
public class Percepcao {
    /**
     * {@link Evento} captado do ambiente que será interpretado pelo agente.
     * Este atributo representa a informação que o agente recebe do ambiente e,
     * com base nela, o agente pode tomar decisões.
     */
    private Evento evento;

    /**
     * Construtor da classe `Percepcao`.
     *
     * @param evento O {@link Evento} percebido.
     */
    public Percepcao(Evento evento) {
        this.evento = evento;
    }

    /**
     * Retorna o {@link Evento} percebido.
     *
     * @return O {@link Evento} que representa a percepção do agente sobre o ambiente.
     */
    public Evento getEvento() {
        return evento;
    }
}
package ambiente;

/**
 * Interface que representa um evento ocorrido no ambiente.
 * Eventos são observações do estado atual do ambiente.
 * Abstraindo a implementação do evento, a classe permite a flexibilidade
 * na observação do ambiente para diferentes tipos de agentes.
 *
 * A interface `Evento` desacopla o agente da implementação específica de como
 * os eventos são representados, permitindo que diferentes tipos de eventos
 * sejam utilizados sem modificar o código do agente.
 */
public interface Evento {
    /**
     * Exibe informações sobre o evento.
     */
    void mostrar();
}
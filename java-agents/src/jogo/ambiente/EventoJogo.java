package jogo.ambiente;

import ambiente.Evento;

/**
 * Enumeração que define os possíveis eventos do jogo.
 * Esta enumeração implementa a interface {@link Evento} e representa
 * as observações que o agente pode fazer do ambiente do jogo.
 * A utilização de uma enumeração garante que os eventos são definidos
 * de forma consistente e que não existem valores inválidos.
 *
 * O uso de um enum garante a unicidade e a imutabilidade dos eventos,
 * promovendo a segurança e a previsibilidade do sistema.
 */
public enum EventoJogo implements Evento { //criação de um enumerado (pelo estereótipo) pública (por omissão) que implementa "Ambiente"
    SILENCIO,   // Evento de silêncio
    RUIDO,      // Evento de ruído
    ANIMAL,     // Evento de presença de animal
    FUGA,       // Evento de fuga
    FOTOGRAFIA, // Evento de fotografia
    TERMINAR;   // Evento de término do jogo

    /**
     * Exibe o evento atual no console.  Este método implementa a interface
     * {@link Evento} e permite exibir informações sobre o evento.
     */
    @Override
    public void mostrar() { //método público (+), do tipo "void"
        System.out.printf("\nEvento: %s\n", this); //imprimir na consola o nome do evento
    }
}
package maqest;

import agente.Accao;

/**
 * A classe `Transicao` representa uma transição entre estados na máquina de estados finitos.
 * Cada transição tem um estado sucessor e uma ação associada.
 * Em termos de diagrama de transição de estados, esta classe representa uma seta
 * que liga dois estados. Uma transição é disparada por um evento e resulta
 * na mudança do estado atual para o estado sucessor.
 */
public class Transicao {
    /**
     * Ação associada à transição.
     * Este atributo representa a ação a ser executada quando a transição é tomada.
     */
    private final Accao accao;

    /**
     * Estado sucessor da transição.
     * Este atributo representa o próximo estado na máquina de estados.
     */
    private final Estado estadoSucessor;

    /**
     * Construtor da classe `Transicao`.
     * @param estadoSucessor O estado sucessor.
     * @param accao A ação associada à transição.
     */
    public Transicao(Estado estadoSucessor, Accao accao) {
        this.accao = accao;
        this.estadoSucessor = estadoSucessor;
    }

    /**
     * Retorna a ação associada à transição.
     * @return A ação associada à transição.
     */
    public Accao getAccao() {
        return accao;
    }

    /**
     * Retorna o estado sucessor.
     * @return O estado sucessor.
     */
    public Estado getEstadoSucessor() {
        return estadoSucessor;
    }
}
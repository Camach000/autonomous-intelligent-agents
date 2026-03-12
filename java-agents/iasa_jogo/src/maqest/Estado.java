package maqest;

import agente.Accao;
import ambiente.Evento;

import java.util.HashMap;
import java.util.Map;

/**
 * A classe `Estado` representa um estado na máquina de estados finitos.
 * Cada estado tem um nome e pode ter uma transição associada para um estado sucessor
 * com base em um evento.
 *
 * Em termos de modelo formal de computação, esta classe representa um elemento
 * do conjunto Q de estados possíveis. Um estado encapsula informações sobre
 * o comportamento do sistema em um determinado momento.
 */
public class Estado {
    /**
     * Nome do estado (read only).
     * Este atributo (read only) permite identificar o estado de forma única.
     */
    private final String nome;

    /**
     * Estado sucessor para uma transição específica.
     * Este atributo representa o próximo estado na transição.
     */
    private Estado estadoSucessor;

    /**
     * Ação associada a uma transição específica.
     * Este atributo representa a ação a ser executada durante a transição.
     */
    private Accao accao;

    /**
     * Mapa de transições associadas ao estado.
     * Este atributo associa eventos a transições, permitindo que o estado reaja
     * a diferentes eventos de forma diferente. A estrutura de dados Map permite
     * uma pesquisa eficiente das transições com base no evento.
     */
    private Map<Evento, Transicao> transicoes;

    /**
     * Construtor da classe `Estado`.
     * @param nome O nome do estado.
     */
    public Estado(String nome) {
        this.nome = nome;
        this.transicoes = new HashMap<Evento, Transicao>();
    }

    /**
     * Construtor da classe `Estado`.
     * @param nome O nome do estado.
     * @param estadoSucessor O estado sucessor.
     * @param accao A ação associada à transição.
     */
    public Estado(String nome, Estado estadoSucessor, Accao accao) {
        this.nome = nome;
        this.estadoSucessor = estadoSucessor;
        this.accao = accao;
    }

    /**
     * Processa um evento e retorna a transição associada.
     * Este método implementa a *função de transição de estado (δ)* do modelo formal de computação.
     * A função δ define como a máquina de estados muda de um estado para outro em resposta
     * a um evento de entrada. Matematicamente, δ: Q x Σ -> Q, onde Q é o conjunto de estados
     * e Σ é o conjunto de eventos de entrada.
     * @param evento O evento a ser processado.
     * @return A transição associada ao evento.
     */
    public Transicao processar(Evento evento) {
        return transicoes.get(evento);
    }

    /**
     * Define uma transição para um estado sucessor sem ação.
     * @param evento O evento que dispara a transição.
     * @param estadoSucessor O estado sucessor.
     * @return null.
     */
    public Estado transicao(Evento evento, Estado estadoSucessor) {
        return null;
    }

    /**
     * Define uma transição para um estado sucessor com ação.
     * Este método permite definir a *função de saída (λ)* do modelo formal de computação.
     * A função λ define qual ação é executada quando uma transição ocorre.
     * Matematicamente, λ: Q x Σ -> Γ, onde Γ é o conjunto de ações possíveis.
     * Neste caso, a função de saída está combinada com a função de transição,
     * pois a ação é definida juntamente com o estado sucessor.
     * @param evento O evento que dispara a transição.
     * @param estadoSucessor O estado sucessor.
     * @param accao A ação associada à transição.
     * @return O estado atual.
     */
    public Estado transicao(Evento evento,Estado estadoSucessor, Accao accao) {
        transicoes.put(evento, new Transicao(estadoSucessor, accao));
        return this;
    }

    /**
     * Retorna o nome do estado.
     * @return O nome do estado.
     */
    public String getNome() {
        return nome;
    }

    /**
     * Retorna o estado sucessor.
     * @return O estado sucessor.
     */
    public Estado getEstadoSucessor() {
        return estadoSucessor;
    }

    /**
     * Retorna a ação associada à transição.
     * @return A ação associada à transição.
     */
    public Accao getAccao() {
        return accao;
    }

    /**
     * Retorna o mapa de transições.
     * @return O mapa de transições.
     */
    public Map<Evento, Transicao> getTransicoes() {
        return transicoes;
    }
}
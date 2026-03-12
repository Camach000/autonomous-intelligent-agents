package maqest;

import agente.Accao;
import ambiente.Evento;

/**
 * A classe `MaquinaEstados` representa uma máquina de estados finitos.
 * Ela mantém o estado atual e implementa a lógica para processar eventos
 * e transitar entre estados.
 *
 * Em termos de modelo formal de computação, esta classe implementa a lógica
 * para simular a evolução do sistema computacional. A *máquina de estados finitos*
 * (MEF), também conhecida como autômato de estados finitos, é um modelo
 * matemático de computação que consiste em:
 *
 * 1.  Um conjunto finito de estados (Q):** Representados pela classe {@link Estado}. Cada estado
 *     representa uma configuração possível do sistema.
 * 2.  Um conjunto finito de eventos de entrada (Σ):** Representados pela interface {@link Evento}.
 *     Os eventos de entrada são estímulos externos que podem causar uma transição de estado.
 * 3.  Um conjunto de transições (δ):** Representado pela classe {@link Transicao} e pela função
 *     {@link Estado#processar(Evento)}. Uma transição define como a máquina de estados
 *     muda de um estado para outro em resposta a um evento de entrada. A função de transição
 *     δ: Q x Σ -> Q mapeia um estado atual e um evento de entrada para um próximo estado.
 * 4.  Um estado inicial (q0):** Representado pelo atributo `estado` no construtor. O estado
 *     inicial é o estado em que a máquina de estados começa.
 * 5.  Um conjunto de estados finais (F):**  Embora não explicitamente representado nesta
 *     implementação, um conjunto de estados finais poderia ser adicionado para definir
 *     condições de término ou aceitação.
 *
 *  A máquina de estados é utilizada para modelar o comportamento de sistemas que podem estar
 *  em um número finito de estados e que mudam de estado em resposta a eventos externos.
 *  Neste contexto, a MEF é usada para modelar o comportamento do personagem do jogo,
 *  onde os estados representam diferentes atividades do personagem e os eventos representam
 *  as percepções do ambiente.
 *
 * A função de transição (δ) e a função de saída (λ) são implementadas de forma combinada
 * na classe {@link Estado}. A função δ é implementada pelo método {@link Estado#processar(Evento)},
 * que determina o próximo estado com base no estado atual e no evento de entrada.
 * A função λ é implementada pelo método {@link Estado#transicao(Evento, Estado, Accao)},
 * que define a ação a ser executada durante a transição.
 */
public class MaquinaEstados {
    /**
     * Estado atual da máquina de estados.
     * Este atributo representa a configuração interna do sistema num dado momento.
     */
    public Estado estado;

    /**
     * Construtor da classe `MaquinaEstados`.
     * @param estadoInicial O estado inicial da máquina de estados.
     */
    public MaquinaEstados(Estado estadoInicial) {
        this.estado = estadoInicial;
    }

    /**
     * Processa um evento e retorna a ação associada à transição.
     * Este método implementa a função de transformação do modelo formal de computação.
     * @param evento O evento a ser processado.
     * @return A ação associada à transição.
     */
    public Accao processar(Evento evento) {
        Transicao transicao = estado.processar(evento);

        if (transicao != null) {
            Estado estadoSucessor = transicao.getEstadoSucessor();
            Accao accao = transicao.getAccao();
            this.estado = estadoSucessor;
            return accao;
        } else {
            return null;
        }
    }

    /**
     * Retorna o estado atual da máquina de estados.
     * @return O estado atual da máquina de estados.
     */
    public Estado getEstado() {
        return estado;
    }
}
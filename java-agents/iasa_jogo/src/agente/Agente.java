package agente;

import ambiente.Ambiente;
import ambiente.Evento;

/**
 * A classe abstrata `Agente` define o comportamento genérico de um agente num ambiente.
 * Agentes são entidades autônomas que interagem com o ambiente, percebendo-o através de
 * percepções ({@link Percepcao}) e agindo sobre ele através de ações ({@link Accao}).
 * Esta classe encapsula a referência ao ambiente e ao módulo de controle ({@link Controlo}),
 * promovendo a modularidade e a separação de responsabilidades (SRP). A utilização de uma
 * classe abstrata permite definir uma estrutura base para diferentes tipos de agentes,
 * permitindo a especialização do comportamento em classes filhas.
 *
 * De acordo com os princípios da engenharia de software, a modularização da arquitetura
 * facilita a manutenção e a evolução do agente.  A separação de responsabilidades
 * permite que cada componente seja desenvolvido e testado independentemente,
 * reduzindo a complexidade do sistema como um todo.
 *
 * O ciclo de vida básico de um agente é:
 * 1.  Perceber o ambiente ({@link #percepcionar()}).
 * 2.  Processar a percepção para decidir a ação ({@link Controlo#processar(Percepcao)}).
 * 3.  Atuar no ambiente ({@link #actuar(Accao)}).
 */
public abstract class Agente {
    /**
     * Referência ao ambiente onde o agente atua, necessária para a interação com o mesmo.
     * Este atributo representa o contexto em que o agente opera e, através dele, o agente pode
     * perceber e modificar o ambiente.  A interface {@link Ambiente} define o contrato
     * para interação com o ambiente, permitindo que diferentes tipos de ambientes
     * sejam utilizados sem modificar o código do agente.
     */
    private Ambiente ambiente;

    /**
     * Módulo de controle ({@link Controlo}) que implementa a lógica de decisão do agente.
     * Este atributo representa o "cérebro" do agente, responsável por processar as percepções
     * e decidir qual ação executar.  A utilização de uma interface ({@link Controlo})
     * permite que diferentes estratégias de controle sejam implementadas e utilizadas
     * sem modificar o código do agente.
     */
    private Controlo controlo;

    /**
     * Construtor da classe `Agente`.
     *
     * @param ambiente O ambiente ({@link Ambiente}) em que o agente atua.
     * @param controlo O módulo de controle ({@link Controlo}) do agente.
     */
    public Agente(Ambiente ambiente, Controlo controlo) {
        this.ambiente = ambiente;
        this.controlo = controlo;
    }

    /**
     * Executa um ciclo de vida do agente: percepciona, processa e atua.
     * Este método encapsula o comportamento básico do agente e define o fluxo
     * de execução.
     */
    public void executar() {
        Percepcao percepcao = percepcionar();
        Accao accao = controlo.processar(percepcao);
        actuar(accao);
    }

    /**
     * Percebe o ambiente e cria uma {@link Percepcao}.
     *
     * @return Uma nova instância de {@link Percepcao} com o evento observado do ambiente.
     */
    protected Percepcao percepcionar() {
        Evento evento = ambiente.observar();
        return new Percepcao(evento);
    }

    /**
     * Atua no ambiente, executando a {@link Accao} especificada.
     *
     * @param accao A {@link Accao} a ser executada no ambiente.
     */
    protected void actuar(Accao accao) {
        if (accao != null) {
            ambiente.executar(accao.getComando());
        }
    }
}
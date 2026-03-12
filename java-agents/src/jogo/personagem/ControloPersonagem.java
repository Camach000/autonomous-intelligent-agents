package jogo.personagem;

import agente.Accao;
import agente.Controlo;
import agente.Percepcao;
import ambiente.Evento;
import jogo.ambiente.ComandoJogo;
import jogo.ambiente.EventoJogo;
import maqest.Estado;
import maqest.MaquinaEstados;

/**
 * Classe responsável pelo controle do personagem no jogo.
 * Implementa a interface {@link Controlo} que define o comportamento básico do agente.
 * Esta classe representa o "cérebro" do personagem, responsável por tomar decisões
 * com base nas percepções do ambiente.
 * O `ControloPersonagem` utiliza uma máquina de estados finitos ({@link MaquinaEstados})
 * para implementar a lógica de decisão do personagem. A máquina de estados define
 * as possíveis transições entre estados com base nos eventos do ambiente.
 */
public class ControloPersonagem implements Controlo {
    private MaquinaEstados maqEst;
    /**
     * Construtor padrão da classe.
     * Inicializa a máquina de estados com os estados e transições definidos.
     */
    public ControloPersonagem() {
        // Conjunto de estados que caracterizam a personagem
        Estado procura = new Estado("Procura");
        Estado inspeccao = new Estado("Inspeccao");
        Estado observacao = new Estado("Observacao");
        Estado registo = new Estado("Registo");

        // Conjunto de símbolos de saída (o alfabeto de saída)
        Accao procurar = new Accao(ComandoJogo.PROCURAR);
        Accao aproximar = new Accao(ComandoJogo.APROXIMAR);
        Accao observar = new Accao(ComandoJogo.OBSERVAR);
        Accao fotografar = new Accao(ComandoJogo.FOTOGRAFAR);


        procura.transicao(EventoJogo.RUIDO, inspeccao, aproximar);
        procura.transicao(EventoJogo.ANIMAL, observacao, aproximar);
        procura.transicao(EventoJogo.SILENCIO, procura, procurar);

        inspeccao.transicao(EventoJogo.ANIMAL, observacao, aproximar);
        inspeccao.transicao(EventoJogo.RUIDO, inspeccao, procurar);
        inspeccao.transicao(EventoJogo.SILENCIO, procura, null);

        observacao.transicao(EventoJogo.FUGA, inspeccao, null);
        observacao.transicao(EventoJogo.ANIMAL, registo, observar);

        registo.transicao(EventoJogo.ANIMAL, registo, fotografar);
        registo.transicao(EventoJogo.FUGA, procura, null);
        registo.transicao(EventoJogo.FOTOGRAFIA, procura, null);

        maqEst = new MaquinaEstados(procura);
    }

    /**
     * Método responsável por processar a percepção do ambiente e determinar a próxima ação.
     * Este método implementa a interface {@link Controlo} e recebe uma {@link Percepcao}
     * do ambiente. A percepção é utilizada para determinar a próxima ação do personagem
     * com base na máquina de estados.
     * @param percepcao Informações do ambiente que o personagem pode perceber.
     * @return Accao A ação que o personagem deve executar.
     */
    public Accao processar(Percepcao percepcao) {
        Evento evento = percepcao.getEvento();
        Accao accao = maqEst.processar(evento);
        mostrar();
        return accao;
    }

    /**
     * Método para exibir informações sobre o estado do controle do personagem.
     * Exibe o estado atual da máquina de estados.
     */
    public void mostrar() {
        System.out.printf("\nEstado: %s\n", getEstado().getNome());
    }

    /**
     * Retorna o estado atual da máquina de estados.
     * @return O estado atual da máquina de estados.
     */
    public Estado getEstado() {
        return maqEst.getEstado();
    }
}
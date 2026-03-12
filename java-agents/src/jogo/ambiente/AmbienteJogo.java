package jogo.ambiente;

import ambiente.Ambiente;
import ambiente.Comando;
import ambiente.Evento;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

/**
 * A classe `AmbienteJogo` implementa a interface {@link Ambiente} e representa
 * o ambiente específico do jogo. Define como o ambiente evolui, como é observado
 * e como os comandos são executados.
 * Esta classe demonstra o princípio de especialização, onde a interface `Ambiente`
 * é implementada de forma concreta para um contexto específico (o jogo).
 *
 * Esta classe é responsável por gerenciar o estado do jogo, receber a entrada do usuário
 * e gerar eventos com base nessa entrada.
 */
public class AmbienteJogo implements Ambiente { //criação de uma classe pública que implementa "Ambiente" (definida pelo tipo de seta que as liga)

    /**
     * Evento atual do ambiente.
     * Este atributo representa o estado atual do ambiente do jogo.
     */
    private EventoJogo evento;

    /**
     * Mapeamento entre códigos de entrada e eventos do jogo.
     * Este atributo associa códigos de entrada do usuário a eventos específicos do jogo,
     * permitindo que o ambiente reaja a ações do usuário.
     */
    private Map<String, EventoJogo> eventos;

    /**
     * Scanner para leitura de entrada do usuário.
     * Este atributo permite que o ambiente receba comandos do usuário.
     */
    private Scanner scanner = new Scanner(System.in);

    /**
     * Construtor que inicializa o mapa de eventos com seus respectivos códigos de entrada:
     * s - SILENCIO
     * r - RUIDO
     * a - ANIMAL
     * f - FUGA
     * o - FOTOGRAFIA
     * t - TERMINAR
     */
    public AmbienteJogo() { //construtor da classe público (+)
        eventos = new HashMap(); //inicialização do HashMap de eventos
        eventos.put("s", EventoJogo.SILENCIO);
        eventos.put("r", EventoJogo.RUIDO);
        eventos.put("a", EventoJogo.ANIMAL);
        eventos.put("f", EventoJogo.FUGA);
        eventos.put("o", EventoJogo.FOTOGRAFIA);
        eventos.put("t", EventoJogo.TERMINAR);
    }

    /**
     * Evolui o estado do ambiente gerando um novo evento.  A evolução do ambiente
     * é baseada na entrada do usuário.
     */
    @Override
    public void evoluir() { //método com @override da interface implementada
        evento = gerarEvento();
    }

    /**
     * Retorna o evento atual e o exibe no console.  Este método permite que o agente
     * perceba o estado atual do jogo.
     * @return O evento atual do ambiente
     */
    @Override
    public Evento observar() { //método com @override da interface implementada
        if (evento != null) {
            evento.mostrar();
        }
        return evento;
    }

    /**
     * Executa um comando no ambiente.  Atualmente, apenas exibe o comando no console.
     * @param comando Comando a ser executado
     */
    @Override
    public void executar(Comando comando) { //método com @override da interface implementada
        System.out.println(comando);
    }

    /**
     * Solicita e processa a entrada do usuário para gerar um novo evento.
     * @return O evento correspondente ao código inserido pelo usuário
     */
    private EventoJogo gerarEvento() { //método privado (por ser -) que retorna um valor do tipo "EventoJogo"
        System.out.print("\nEvento? "); //pedir os dados ao utilizador
        String codigoEvento = scanner.next(); //ler os dados com o scanner
        return eventos.get(codigoEvento); //retornar o evento correspondente ao evento inserido pelo utilizador que corresponderá ao elemento do HashMap
    }

    /**
     * Retorna o evento atual do ambiente.
     * @return O evento atual
     */
    public Evento getEvento() { //criação de um getter para a função de read only do atributo "evento" (público porque um getter assim o deve ser)
        return evento;
    }
}
package jogo;

import jogo.ambiente.AmbienteJogo;
import jogo.ambiente.EventoJogo;
import jogo.personagem.Personagem;

/**
 * A classe `Jogo` é a classe principal que inicializa e executa o jogo.
 * Ela cria o ambiente do jogo e o personagem, e define o ciclo de vida do jogo.
 * A classe Jogo demonstra o conceito de modularidade, onde diferentes componentes
 * (ambiente e personagem) são combinados para criar um sistema completo.
 * Esta classe segue o padrão de projeto Singleton, garantindo que apenas uma instância
 * do jogo seja criada. O método `main` é o ponto de entrada da aplicação e é
 * responsável por inicializar o jogo e iniciar o ciclo de vida.
 */
public class Jogo {
    /**
     * Criação de um atributo static privado(-) do tipo "AmbienteJogo".
     * Representa o ambiente do jogo onde a personagem atua.
     */
    private static AmbienteJogo ambiente;

    /**
     * Criação de um atributo static privado(-) do tipo "Personagem".
     * Representa o personagem principal do jogo que interage com o ambiente.
     */
    private static Personagem personagem;

    /**
     * De acordo com o diagrama (pag9 P1-iasa-proj.pdf) a função main é responsável por criar
     * um novo ambiente e um novo personagem.
     * Este método é o ponto de entrada da aplicação e é responsável por inicializar
     * o ambiente e o personagem do jogo, e iniciar o ciclo de vida do jogo.
     * @param args Argumentos da linha de comando (não utilizados).
     */
    public static void main(String[] args) { //método público(+), estático pois métodos numa função estática devem ser estáticos
        ambiente = new AmbienteJogo();
        personagem = new Personagem(ambiente);
        executar();
    }

    /**
     * Esta função é responsável por manter o jogo a correr (enquanto este estiver de acordo ao que é definido no loop).
     * Método privado(-), estático pois métodos numa função estática devem ser estáticos.
     * Este método implementa o ciclo de vida do jogo, que envolve a evolução do ambiente
     * e a execução das ações do personagem.
     */
    private static void executar() {
        do {
            ambiente.evoluir();
            personagem.executar();
        }
        while(ambiente.observar() != EventoJogo.TERMINAR); //loop para os métodos evoluir() e executar(), pág9 P1-iasa-proj.pdf
    }
}
package jogo.personagem;

import agente.Agente;
import jogo.ambiente.AmbienteJogo;

/**
 * Classe que representa o personagem do jogo.
 * Herda da classe {@link Agente}, implementando o comportamento básico de um agente no ambiente.
 * A classe Personagem representa o ator principal do jogo e interage com o ambiente
 * através de percepções e ações.
 * O princípio de herança permite que a classe Personagem reutilize o código da classe Agente,
 * evitando a duplicação de código e promovendo a modularidade. A classe Personagem
 * especializa o comportamento do agente, definindo o seu próprio módulo de controle
 * ({@link ControloPersonagem}).
 */
public class Personagem extends Agente {

    /**
     * Construtor da classe `Personagem`.
     * @param ambiente Referência para o ambiente do jogo onde o personagem irá atuar.
     * Inicializa o agente com o ambiente fornecido e uma nova instância de `ControloPersonagem`.
     */
    public Personagem(AmbienteJogo ambiente) {
        super(ambiente, new ControloPersonagem());
    }
}
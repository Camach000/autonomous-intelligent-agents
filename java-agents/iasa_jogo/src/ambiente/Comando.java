package ambiente;

/**
 * Interface que representa um comando que pode ser executado em um ambiente.
 * Comandos são ações que podem modificar o estado do ambiente.
 * Como um dos princípios da arquitetura de software, esta interface permite
 * a abstração da forma como o comando é executado no ambiente.
 *
 * A interface `Comando` permite a criação de um sistema flexível e extensível,
 * onde novos comandos podem ser adicionados sem modificar o código do ambiente.
 * Isto está alinhado com o princípio aberto/fechado (OCP).
 */
public interface Comando {
    /**
     * Exibe informações sobre o comando.
     */
    void mostrar();
}
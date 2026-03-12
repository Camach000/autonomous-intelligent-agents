package ambiente;

/**
 * Interface que representa um ambiente genérico que pode evoluir ao longo do tempo,
 * ser observado e receber comandos. Esta interface define o contrato para ambientes,
 * permitindo que diferentes tipos de ambientes sejam utilizados com os mesmos agentes.
 * O principio de modularização aplicado ao ambiente do agente permite criar
 * modelos mais robustos e flexíveis que reagem aos comandos do agente.
 *
 * A interface `Ambiente` abstrai a complexidade do mundo em que o agente atua,
 * permitindo que diferentes implementações de ambientes sejam utilizadas sem
 * modificar o código do agente (aderindo ao princípio da inversão de dependência).
 */
public interface Ambiente {

    /**
     * Faz o ambiente evoluir para seu próximo estado.
     * Este método simula a passagem do tempo no ambiente.
     */
    void evoluir();

    /**
     * Retorna um evento que representa o estado atual do ambiente.
     * Este método permite que o agente perceba o estado do ambiente.
     * @return Evento atual do ambiente
     */
    Evento observar();

    /**
     * Executa um comando no ambiente, potencialmente alterando seu estado.
     * Este método permite que o agente interaja com o ambiente.
     * @param comando O comando a ser executado
     */
    void executar(Comando comando);
}
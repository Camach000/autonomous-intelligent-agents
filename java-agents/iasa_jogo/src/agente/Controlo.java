package agente;

/**
 * A interface `Controlo` define o contrato para módulos de controle de agentes.
 * Módulos de controle são responsáveis por processar percepções ({@link Percepcao}) do ambiente
 * e decidir qual ação ({@link Accao}) o agente deve executar.  Esta interface define o "cérebro"
 * do agente.
 * Segundo o princípio de inversão de dependência (DIP) do SOLID, esta interface permite
 * a flexibilidade e a substituição de diferentes estratégias de controle sem alterar o resto
 * da arquitetura.  Classes de alto nível (como `Agente`) dependem de abstrações (como
 * `Controlo`), e não de implementações concretas.
 */
public interface Controlo {
    /**
     * Processa a percepção e decide a ação a ser tomada.
     *
     * @param percepcao A percepção ({@link Percepcao}) do ambiente.
     * @return A ação ({@link Accao}) a ser executada.
     */
    Accao processar(Percepcao percepcao);
}
  UC01: Manter Veículo

Ator: Utilizador.

Descrição: Permite ao utilizador registar, editar ou eliminar as informações de um veículo (matrícula, marca, modelo).

  UC02: Registar Evento de Manutenção/Abastecimento

Ator: Utilizador.

Descrição: O sistema permite inserir dados relativos a uma despesa, seja ela combustível ou reparação, associando-a a um veículo específico.

  UC03: Consultar Histórico de Gastos

Ator: Utilizador.

Descrição: O sistema apresenta uma lista detalhada de todos os registos efetuados, permitindo filtrar ou ordenar por data.

  UC04: Gerir Alertas de Prazos

Ator: Utilizador.

Descrição: O utilizador define datas críticas (IPO, Seguro) e o sistema gera avisos visuais no painel principal.

  UC05: Visualizar Dashboard de Estatísticas

Ator: Utilizador.

Descrição: O sistema processa os dados da base de dados e apresenta resumos gráficos ou numéricos dos gastos mensais.

```mermaid
flowchart LR
    U((Utilizador))
    
    subgraph AutoTracker
        direction TB
        UC1([UC01: Manter Veículos])
        UC2([UC02: Registar Despesas])
        UC3([UC03: Consultar Histórico])
        UC4([UC04: Gerir Alertas])
        UC5([UC05: Visualizar Dashboard])
    end

    U --> UC1
    U --> UC2
    U --> UC3
    U --> UC4
    U --> UC5

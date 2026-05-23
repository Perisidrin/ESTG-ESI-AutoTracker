# Modelo de Classes - AutoTracker

Abaixo apresenta-se o Diagrama de Classes UML do sistema AutoTracker. Este modelo define a estrutura de dados principal, as entidades do sistema e os seus respetivos relacionamentos, servindo de base para a futura criação da base de dados relacional.

```mermaid
classDiagram
    class Veiculo {
        +int id
        +String matricula
        +String marca
        +String modelo
    }
    
    class Despesa {
        +int id
        +Date data
        +float valor
        +String tipo
        +String descricao
    }
    
    class Alerta {
        +int id
        +String tipo_alerta
        +Date data_limite
        +boolean ativo
    }

    Veiculo "1" -- "*" Despesa : possui
    Veiculo "1" -- "*" Alerta : tem

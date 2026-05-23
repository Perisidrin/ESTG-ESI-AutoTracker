# Documento de Visão - AutoTracker

### (a) Objetivo
O AutoTracker tem como principal objetivo facilitar a gestão e manutenção de veículos pessoais. O sistema permitirá aos utilizadores registar e monitorizar, de forma centralizada, todas as despesas recorrentes associadas às suas viaturas, incluindo abastecimentos de combustível, manutenções periódicas, pagamentos de seguros e datas de inspeção obrigatória.

### (b) Escopo
O sistema é concebido para uso pessoal e doméstico, podendo ser utilizado por qualquer proprietário de um veículo automóvel ou motociclo que deseje ter um controlo financeiro e mecânico mais rigoroso sobre o seu meio de transporte.

### (c) Partes Interessadas (Stakeholders)
* **Utilizadores Finais (Proprietários de Veículos):** São os utilizadores principais do sistema, que irão inserir os dados e beneficiar do histórico e dos alertas gerados.
* **Profissionais de Manutenção (Indiretamente):** Mecânicos e oficinas podem beneficiar da organização do histórico do veículo, caso o proprietário partilhe as informações geradas pelo sistema.

### (d) Equipa do Projeto
* **Desenvolvedor Único:** Pedro Meneses (Nº 60029) - Responsável pelo levantamento de requisitos, design, implementação e testes da aplicação.

### (e) Características do Sistema (Lista de Funcionalidades)
* Gestão do perfil do veículo (Matrícula, Marca, Modelo).
* Registo detalhado de abastecimentos (Data, Litros, Valor).
* Registo de manutenções e idas à oficina (Data, Tipo de Serviço, Valor).
* Sistema de alertas para prazos importantes (Inspeção Periódica e Seguro).
* Dashboard analítico com resumo de gastos mensais e filtros por veículo.
* Consulta de histórico cronológico de todas as intervenções.

### (f) Arquitetura de Referência
O sistema seguirá uma arquitetura Client-Server típica de aplicações WEB:
* **Frontend (Client):** Interface de utilizador desenvolvida com HTML, CSS e JavaScript (podendo incluir bibliotecas de estilização).
* **Backend (Server):** Servidor local responsável pelo processamento da lógica de negócio.
* **Base de Dados:** Sistema de armazenamento relacional (ex: MySQL ou SQLite) para persistência dos dados dos veículos e registos.

### (g) Restrições do Produto
* O sistema requer um navegador Web atualizado para funcionar corretamente.
* Para ser executado, o ambiente local (localhost) deve ter o servidor web e o motor de base de dados devidamente configurados e a correr.
* O sistema não recolherá dados de telemetria dos veículos em tempo real (não há integração via OBD2).

### (h) Integração LLM
Nesta versão inicial do sistema (MVP), optou-se por **não incluir** uma integração com LLM, focando o esforço de desenvolvimento na robustez das funcionalidades centrais de gestão de base de dados e estabilidade da interface de utilizador. Uma futura atualização poderá explorar a utilização de um LLM local (ex: Ollama) para analisar as descrições das faturas mecânicas e categorizar automaticamente os gastos.

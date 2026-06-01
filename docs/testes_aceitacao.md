# Testes de Aceitação - AutoTracker

Este documento valida a implementação do sistema AutoTracker, garantindo que o Produto Mínimo Viável (MVP) cumpre os requisitos estabelecidos na fase de planeamento através das User Stories.

### Resultados dos Testes

**✅ US01 - Gestão de Veículos**
* **Critério de Aceitação:** O utilizador consegue ver os seus veículos registados no sistema.
* **Passos do Teste:** Aceder à página inicial (`/`). Verificar a secção "A Minha Garagem".
* **Resultado:** SUCESSO. O sistema carrega com sucesso os dados do veículo (ex: Renault Clio, AA-00-BB) diretamente da base de dados (Tabela `Veiculo`).

**✅ US02 e US03 - Registo de Abastecimentos e Manutenções**
* **Critério de Aceitação:** O utilizador consegue inserir novos gastos de combustível ou idas à oficina.
* **Passos do Teste:** Clicar nos botões de "Novo Registo". Preencher o formulário na rota `/novo_registo`. Submeter.
* **Resultado:** SUCESSO. O formulário HTML (com proteção de dados `required` e tipagem) envia os dados via método POST para o backend em Flask, que os insere com sucesso na Tabela `Despesa` usando uma query parametrizada (evitando falhas de segurança).

**✅ US04 - Gestão de Prazos (Alertas)**
* **Critério de Aceitação:** O utilizador é avisado de datas limite como IPO e Seguro.
* **Passos do Teste:** Aceder ao painel principal. Verificar a área de Alertas.
* **Resultado:** SUCESSO. O servidor efetua uma query à Tabela `Alerta` filtrando por `ativo = 1` e a interface Jinja2 renderiza o bloco HTML condicional do aviso em vermelho.

**✅ US05 - Consulta de Histórico**
* **Critério de Aceitação:** O utilizador tem acesso cronológico a todas as despesas.
* **Passos do Teste:** Consultar a tabela "Últimos Registos" no painel principal.
* **Resultado:** SUCESSO. A tabela é populada dinamicamente através de um ciclo `{% for %}`, ordenando as despesas inseridas pela sua ordem de registo (ID descendente).

**✅ US06 - Dashboard (Painel de Resumo)**
* **Critério de Aceitação:** Visualizar o total de gastos atualizado automaticamente.
* **Passos do Teste:** Registar uma nova despesa e verificar os cartões de "Visão Geral".
* **Resultado:** SUCESSO. O Flask executa queries com a função agregadora `SUM()` do SQLite. A soma do "Combustível" e "Manutenção" é calculada em tempo real no servidor (backend) e processada no ecrã sem necessidade de cálculos manuais.

---
**Conclusão:** O MVP passou em 100% dos cenários de teste definidos pelas User Stories primárias. A arquitetura Client-Server provou ser funcional, com a ligação base de dados/backend a responder perfeitamente aos inputs do frontend.

import sqlite3

# Ligar à base de dados (cria o ficheiro se não existir)
connection = sqlite3.connect('database.db')

with open('schema.sql', 'w') as f:
    pass # Apenas para garantir que o ficheiro é criado limpo, mas vamos executar direto abaixo

cur = connection.cursor()

# 1. Criar as Tabelas
cur.execute('''
    CREATE TABLE IF NOT EXISTS Veiculo (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        matricula TEXT NOT NULL,
        marca TEXT NOT NULL,
        modelo TEXT NOT NULL
    )
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS Despesa (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        veiculo_id INTEGER,
        data_registo TEXT NOT NULL,
        valor REAL NOT NULL,
        tipo TEXT NOT NULL,
        descricao TEXT,
        FOREIGN KEY (veiculo_id) REFERENCES Veiculo (id)
    )
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS Alerta (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        veiculo_id INTEGER,
        tipo_alerta TEXT NOT NULL,
        data_limite TEXT NOT NULL,
        ativo BOOLEAN NOT NULL,
        FOREIGN KEY (veiculo_id) REFERENCES Veiculo (id)
    )
''')

# 2. Inserir Dados de Teste (Seed)
# Inserir o teu carro
cur.execute("INSERT INTO Veiculo (matricula, marca, modelo) VALUES (?, ?, ?)", ('AA-00-BB', 'Renault', 'Clio'))

# Inserir despesas de teste
cur.execute("INSERT INTO Despesa (veiculo_id, data_registo, valor, tipo, descricao) VALUES (?, ?, ?, ?, ?)", (1, '12/05/2026', 60.00, 'Oficina', 'Mudança de Óleo e Filtros'))
cur.execute("INSERT INTO Despesa (veiculo_id, data_registo, valor, tipo, descricao) VALUES (?, ?, ?, ?, ?)", (1, '02/05/2026', 85.20, 'Combustível', 'Gasolina 95 (45 Litros)'))
cur.execute("INSERT INTO Despesa (veiculo_id, data_registo, valor, tipo, descricao) VALUES (?, ?, ?, ?, ?)", (1, '14/03/2026', 40.00, 'Combustível', 'Abastecimento - Caxias/Algés'))

# Inserir um alerta
cur.execute("INSERT INTO Alerta (veiculo_id, tipo_alerta, data_limite, ativo) VALUES (?, ?, ?, ?)", (1, 'Inspeção Periódica (IPO)', '20/05/2026', True))

connection.commit()
connection.close()

print("Base de dados criada e populada com sucesso!")
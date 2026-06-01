import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row 
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    veiculos = conn.execute('SELECT * FROM Veiculo').fetchall()
    despesas = conn.execute('SELECT * FROM Despesa ORDER BY id DESC').fetchall()
    alertas = conn.execute('SELECT * FROM Alerta WHERE ativo = 1').fetchall()
    
    total_combustivel = conn.execute("SELECT SUM(valor) FROM Despesa WHERE tipo = 'Combustível'").fetchone()[0] or 0
    total_manutencao = conn.execute("SELECT SUM(valor) FROM Despesa WHERE tipo = 'Oficina'").fetchone()[0] or 0
    gasto_total = total_combustivel + total_manutencao
    
    conn.close()
    
    return render_template('dashboard.html', 
                           veiculos=veiculos, 
                           despesas=despesas, 
                           alertas=alertas,
                           gasto_total=f"{gasto_total:.2f}".replace('.', ','),
                           total_combustivel=f"{total_combustivel:.2f}".replace('.', ','),
                           total_manutencao=f"{total_manutencao:.2f}".replace('.', ','))

# NOVA ROTA: Formulário para adicionar despesas
@app.route('/novo_registo', methods=('GET', 'POST'))
def novo_registo():
    if request.method == 'POST':
        try:
            tipo = request.form['tipo']
            data_registo = request.form['data']
            # Converter a string do HTML para float no Python previne muitos erros
            valor = float(request.form['valor'].replace(',', '.')) 
            descricao = request.form['descricao']
            veiculo_id = 1 

            conn = get_db_connection()
            conn.execute('INSERT INTO Despesa (veiculo_id, data_registo, valor, tipo, descricao) VALUES (?, ?, ?, ?, ?)',
                         (veiculo_id, data_registo, valor, tipo, descricao))
            conn.commit()
            conn.close()
            
            return redirect(url_for('index'))
            
        except ValueError:
            # Se a conversão do número falhar (alguém tentou injetar texto)
            return "Erro: O valor inserido não é um número válido.", 400
        except sqlite3.Error as e:
            # Se a base de dados falhar
            return f"Erro na base de dados: {e}", 500
            
    tipo_predefinido = request.args.get('tipo', 'Combustível')
    return render_template('novo_registo.html', tipo=tipo_predefinido)

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

# Função para conectar ao banco de dados SQLite
def get_db_connection():
    conn = sqlite3.connect('db.sqlite3')
    conn.row_factory = sqlite3.Row  # Para acessar colunas pelo nome
    return conn

# Página inicial que renderiza o formulário de login
@app.route('/')
def login_form():
    return render_template('login.html')

# Rota para processar o login
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Conectar ao banco de dados e verificar o login
    conn = get_db_connection()
    cursor = conn.cursor()

    # Aqui estamos supondo que você tenha uma tabela chamada "users"
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = cursor.fetchone()

    if user:
        return f'Login bem-sucedido! Bem-vindo, {username}.'
    else:
        return 'Usuário ou senha incorretos. Tente novamente.'

if __name__ == '__main__':
    app.run(debug=True)

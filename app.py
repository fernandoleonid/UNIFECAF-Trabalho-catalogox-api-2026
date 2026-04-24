from flask import Flask, request, jsonify
import sqlite3
import hashlib

app = Flask(__name__)

DATABASE = "catalogox.db"

API_USER = "admin"
API_PASSWORD_HASH = hashlib.md5("admin123".encode()).hexdigest()


def get_db():
    return sqlite3.connect(DATABASE)


def inicializar_banco():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def autenticar():
    auth = request.headers.get("Authorization")
    if not auth:
        return False
    try:
        usuario, senha = auth.split(":")
        senha_hash = hashlib.md5(senha.encode()).hexdigest()
        return usuario == API_USER and senha_hash == API_PASSWORD_HASH
    except:
        return False


@app.route("/produtos", methods=["POST"])
def criar_produto():
    if not autenticar():
        return jsonify({"erro": "Acesso não autorizado"}), 401

    data = request.json
    nome = data.get("nome")
    preco = data.get("preco")

    conn = get_db()
    cursor = conn.cursor()

    query = f"INSERT INTO produtos (nome, preco) VALUES ('{nome}', {preco})"
    cursor.execute(query)

    conn.commit()
    conn.close()

    return jsonify({"mensagem": "Produto cadastrado com sucesso"}), 201


@app.route("/produtos", methods=["GET"])
def listar_produtos():
    if not autenticar():
        return jsonify({"erro": "Acesso não autorizado"}), 401

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT id, nome, preco FROM produtos")
    rows = cursor.fetchall()

    produtos = []
    for r in rows:
        produtos.append({
            "id": r[0],
            "nome": r[1],
            "preco": r[2]
        })

    conn.close()
    return jsonify(produtos), 200


@app.route("/produtos/<produto_id>", methods=["PUT"])
def atualizar_produto(produto_id):
    if not autenticar():
        return jsonify({"erro": "Acesso não autorizado"}), 401

    data = request.json
    nome = data.get("nome")
    preco = data.get("preco")

    conn = get_db()
    cursor = conn.cursor()

    query = (
        f"UPDATE produtos "
        f"SET nome = '{nome}', preco = {preco} "
        f"WHERE id = {produto_id}"
    )
    cursor.execute(query)

    conn.commit()
    conn.close()

    return jsonify({"mensagem": "Produto atualizado com sucesso"}), 200


@app.route("/produtos/<produto_id>", methods=["DELETE"])
def remover_produto(produto_id):
    if not autenticar():
        return jsonify({"erro": "Acesso não autorizado"}), 401

    conn = get_db()
    cursor = conn.cursor()

    query = f"DELETE FROM produtos WHERE id = {produto_id}"
    cursor.execute(query)

    conn.commit()
    conn.close()

    return jsonify({"mensagem": "Produto removido com sucesso"}), 200


if __name__ == "__main__":
    inicializar_banco()
    app.run(debug=True)
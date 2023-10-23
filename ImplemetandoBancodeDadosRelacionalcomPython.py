import sqlite3

class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class Conta:
    def __init__(self, cliente_id, saldo):
        self.cliente_id = cliente_id
        self.saldo = saldo
        
        def criar_tabela_clientes():
    conn = sqlite3.connect("banco_de_dados.db")
    cursor = conn.cursor()
    cursor.execute
    ('''CREATE TABLE IF NOT EXISTS clientes (
                      id INTEGER PRIMARY KEY,
                      nome TEXT,
                      email TEXT)'')
import sqlite3

#conexão com o bando de dados
conn = sqlite3.connect("chamados.db")
cursor = conn.cursor()
STATUS_VALIDOS = ["Aberto", "Em Andamento", "Resolvido"]

#Criar a tabela de chamados
cursor.execute("""
CREATE TABLE IF NOT EXISTS chamados (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente TEXT,
    problema TEXT,
    status TEXT
)
""")
conn.commit()
import sqlite3
def conectar_db():
    return sqlite3.connect("alici.db")

def criar_tabela():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS conversas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pergunta TEXT,
        resposta TEXT,
        embedding TEXT,
        data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')
    conn.commit()
    conn.close()

def salvar_conversa(pergunta, resposta, embedding):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO conversas (pergunta, resposta, embedding) VALUES (?, ?, ?)",
                   (pergunta, resposta, ','.join(map(str, embedding))))
    conn.commit()
    conn.close()

def obter_todas_conversas():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("SELECT pergunta, resposta, embedding FROM conversas")
    resultados = cursor.fetchall()
    conn.close()
    return resultados

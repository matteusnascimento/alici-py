# database.py

import psycopg2
from psycopg2.extras import RealDictCursor

DB_URL = "postgresql://neondb_owner:npg_YA5DVX0fvWrg@ep-frosty-shape-a8fhb2m2-pooler.eastus2.azure.neon.tech/neondb?sslmode=require"

def conectar():
    return psycopg2.connect(DB_URL, cursor_factory=RealDictCursor)

def buscar_resposta(pergunta):
    conn = conectar()
    cur = conn.cursor()
    cur.execute("SELECT resposta FROM respostas WHERE pergunta ILIKE %s LIMIT 1", (f"%{pergunta}%",))
    resultado = cur.fetchone()
    cur.close()
    conn.close()
    return resultado["resposta"] if resultado else None

def salvar_conversa(pergunta, resposta):
    conn = conectar()
    cur = conn.cursor()
    cur.execute("INSERT INTO respostas (pergunta, resposta) VALUES (%s, %s)", (pergunta, resposta))
    conn.commit()
    cur.close()
    conn.close()

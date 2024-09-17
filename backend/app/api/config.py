import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from fastapi import FastAPI, HTTPException
from app.database.config import get_connection

app = FastAPI()

@app.get("/")
def index():
    return {"message": "API de Controle de Cortinas"}

@app.get("/cortina")
def listar_cortinas():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM cortina")  # Ajuste o nome da tabela
        dados = cursor.fetchall()
        conn.close()
        return dados
    except Exception as e:
        return print(e)

# Exemplo de rota para buscar cortina por ID
@app.get("/bobina/{id_lote}")
def buscar_cortina(id_lote: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bobina WHERE id_lote = %s", (id_lote,))
    dados = cursor.fetchone()
    conn.close()
    if dados:
        return dados
    else:
        raise HTTPException(status_code=404, detail="Cortina não encontrada")
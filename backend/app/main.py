import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from backend.app.models.bobina import Bobina
from backend.app.models.estoque import Estoque
from backend.app.models.cortina import Cortina
from backend.app.models.historico import Historico
from datetime import datetime

app = FastAPI(
    title="App_Cortinas",
    summary="API para controle de bobinas.",
    version="1.0",
)

estoque = Estoque()

class BobinaCreate(BaseModel):
    endereco: str
    codigo: str
    lote: str
    metragem: float
    data_entrada: datetime = datetime.now().strftime("%Y-%m-%d")
    
@app.post(
          path="/bobina/",
          description="Cadastro de Bobinas",
          name="Cadastrar de Bobinas",
          tags=["Bobina"]
          )
def criar_bobina(bobina: BobinaCreate):
    try:
        nova_bobina = Bobina(
            endereco=bobina.endereco,
            codigo=bobina.codigo,
            lote=bobina.lote,
            metragem=bobina.metragem,
            data_entrada=bobina.data_entrada
        )
        estoque.adicionar_bobina(nova_bobina)
        return {"message": "Bobina criada com sucesso"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@app.get(
        path="/bobina/lote/{lote}",
        name="Buscar Bobina",
        description="Buscar Bobina por Lote"
        )
def buscar_bobina(lote: str):
    bobina = Bobina.buscar_bobina(lote)
    if not bobina:
        raise HTTPException(status_code=404, detail="Bobina não encontrada")
    return bobina.__dict__

@app.delete("/bobina/codigo/f{codigo}")
def deletar_bobina(codigo: str):
    try:
        estoque.remover_bobina(codigo)
        return {"message": "Bobina removida com sucesso"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.put("/bobina/{codigo}/mover")
def mover_bobina(codigo: str, novo_endereco: str):
    try:
        estoque.mover_bobina(codigo, novo_endereco)
        return {"message": "Bobina movida com sucesso"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.put("/bobina/{codigo}/produzir")
def mover_para_producao(codigo: str):
    try:
        estoque.mover_para_producao(codigo)
        return {"message": "Bobina movida para produção com sucesso"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.get("/bobina/{codigo}/historico")
def obter_historico(codigo: str):
    historico = estoque.obter_historico(codigo)
    if not historico:
        raise HTTPException(status_code=404, detail="Histórico não encontrado")
    return {"historico": [vars(h) for h in historico]}
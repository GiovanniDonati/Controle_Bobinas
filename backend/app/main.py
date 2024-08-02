from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .models.bobina import Bobina
from .models.estoque import Estoque
from .models.cortina import Movimentacao
from .models.historico import Historico
from datetime import datetime

app = FastAPI()

estoque = Estoque()

class BobinaCreate(BaseModel):
    endereco: str
    codigo: str
    descricao: str
    lote: str
    metragem: float
    data_entrada: datetime

@app.post("/bobinas/")
def criar_bobina(bobina: BobinaCreate):
    try:
        nova_bobina = Bobina(
            endereco=bobina.endereco,
            codigo=bobina.codigo,
            descricao=bobina.descricao,
            lote=bobina.lote,
            metragem=bobina.metragem,
            data_entrada=bobina.data_entrada
        )
        estoque.adicionar_bobina(nova_bobina)
        return {"message": "Bobina criada com sucesso"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.delete("/bobinas/{codigo}")
def deletar_bobina(codigo: str):
    try:
        estoque.remover_bobina(codigo)
        return {"message": "Bobina removida com sucesso"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.put("/bobinas/{codigo}/mover")
def mover_bobina(codigo: str, novo_endereco: str):
    try:
        estoque.mover_bobina(codigo, novo_endereco)
        return {"message": "Bobina movida com sucesso"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.put("/bobinas/{codigo}/produzir")
def mover_para_producao(codigo: str):
    try:
        estoque.mover_para_producao(codigo)
        return {"message": "Bobina movida para produção com sucesso"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.get("/bobinas/{codigo}/historico")
def obter_historico(codigo: str):
    historico = estoque.obter_historico(codigo)
    if not historico:
        raise HTTPException(status_code=404, detail="Histórico não encontrado")
    return {"historico": [vars(h) for h in historico]}
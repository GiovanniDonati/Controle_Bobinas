from fastapi import FastAPI, HTTPException

from backend.app.controller.schemas import BobinaCreate
from backend.app.models.bobina import Bobina

app = FastAPI(
    title="App_Cortinas",
    summary="API para controle de bobinas.",
    version="1.0",
)

@app.post(
          path="/bobina/",
          description="Cadastro de Bobinas",
          name="Cadastrar de Bobinas",
          tags=["Bobina"]
          )
def criar_bobina(bobina: BobinaCreate):
    pass
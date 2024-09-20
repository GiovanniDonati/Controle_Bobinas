from fastapi import FastAPI, HTTPException
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from backend.app.API.schemas.schemas import BobinaCreate
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

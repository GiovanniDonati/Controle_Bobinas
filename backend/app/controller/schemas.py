from pydantic import BaseModel
from datetime import datetime

class BobinaCreator(BaseModel):
    endereco: str
    codigo: str
    lote: str
    metragem: float
    data_entrada: datetime = datetime.now().strftime("%Y-%m-%d")
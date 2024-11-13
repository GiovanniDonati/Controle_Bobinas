from typing import Annotated
from app.database.config import Base

class Cortina(Base):
    id_codigo = Annotated[int]
    descricao = Annotated[str]
    
    def __init__(self, id_codigo, descricao):
        self.id_codigo = id_codigo
        self.descricao = descricao
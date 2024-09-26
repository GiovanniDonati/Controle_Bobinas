from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base

from app.database.config import Base

class Cortina(Base):
    __tablename__ = 'cortina'
    
    id_codigo = Column(Integer, primary_key=True)
    descricao = Column(String)
    
    def __init__(self, id_codigo, descricao):
        self.id_codigo = id_codigo
        self.descricao = descricao
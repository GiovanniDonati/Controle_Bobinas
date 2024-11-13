from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey

from app.database.config import Base

class Endereco(Base):
    __tablename__ = 'endereco'
    
    id_endereco = Column(Integer, primary_key=True)
    tipo_endereco = Column(String)
    espaco = Column(String)
    
    def __init__(self, id_endereco, tipo_endereco, espaco):
        self.id_endereco = id_endereco
        self.tipo_endereco = tipo_endereco
        self.espaco = espaco
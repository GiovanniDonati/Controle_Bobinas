from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey

from app.database.config import Base

class Historico(Base):
    __tablename__ = 'historico'
    
    id_historico = Column(Integer, primary_key=True)
    bobina_id_lote = Column(Integer)
    endereco_antigo = Column(String)
    endereco_novo = Column(String)
    data_cadastro = Column(DateTime)
    data_mov = Column(DateTime)
    tipo_mov = Column(String)
    metragem_antiga = Column(Float)
    metragem_nova = Column(Float)
    user_id_user = Column(Integer)
    
    def __init__(self, id_historico, cortina_id_codigo, endereco_id_endereco, data_cadastro, metragem):
        self.id_historico = id_historico
        self.bobina_id_lote = cortina_id_codigo
        self.endereco_antigo = endereco_id_endereco
        self.endereco_novo = endereco_id_endereco
        self.data_cadastro = data_cadastro
        self.metragem = metragem
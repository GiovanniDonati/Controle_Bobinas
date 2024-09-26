from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import Session

from app.database.config import Base

class Bobina(Base):
    __tablename__ = 'bobina'
    
    id_lote = Column(Integer, primary_key=True)
    cortina_id_codigo = Column(Integer, ForeignKey('cortina.id_codigo'))
    endereco_id_endereco = Column(Integer, ForeignKey('endereco.id_endereco'))
    data_cadastro = Column(DateTime)
    metragem = Column(Float)
    
    def __init__(self, id_lote, cortina_id_codigo, endereco_id_endereco, data_cadastro, metragem):
        self.id_lote = id_lote
        self.cortina_id_codigo = cortina_id_codigo
        self.endereco_id_endereco = endereco_id_endereco
        self.data_cadastro = data_cadastro
        self.metragem = metragem
        
    def create_bobina(db: Session, id_lote, cortina_id_codigo, endereco_id_endereco, data_cadastro, metragem):
        new_bobina = Bobina(id_lote=id_lote, cortina_id_codigo=cortina_id_codigo, endereco_id_endereco=endereco_id_endereco, data_cadastro=data_cadastro, metragem=metragem)
        db.add(new_bobina)
        db.commit()
        db.refresh(new_bobina)
        return new_bobina
        
    def buscar_lote(db: Session, id_lote):
        return db.query(Bobina).filter(Bobina.id_lote == id_lote).first()
        
    def buscar_todas(db: Session):
        return db.query(Bobina).all()
        
    def atualizar_bobina(db: Session, id_lote, data):
        bobina = db.query(Bobina).filter(Bobina.id_lote == id_lote).first()
        if bobina:
            for key, value in data.items():
                setattr(bobina, key, value)
            db.commit()
            db.refresh(bobina)
            return bobina
        else:
            return None
        
    def deletar_bobina(db: Session, id_lote):
        bobina = db.query(Bobina).filter(Bobina.id_lote == id_lote).first()
        if bobina:
            db.delete(bobina)
            db.commit()
            return True
        else:
            return False
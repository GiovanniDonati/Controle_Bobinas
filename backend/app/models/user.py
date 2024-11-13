from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import Session

from app.database.config import Base

class User(Base):
    __tablename__ = 'user'
    
    id_user = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    
    def __init__(self, id_user, username, password):
        self.id_user = id_user
        self.username = username
        self.password = password
        
    def criar_user(db: Session,  username, password):
        new_user = User(username=username, password=password)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    
    def atulizar_user(db: Session, username, password):
        db.query(User).filter(User.username == username).update({'password': password})
        db.commit()
        return
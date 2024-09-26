from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey

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
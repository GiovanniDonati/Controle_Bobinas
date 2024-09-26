from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DB_URL = "mysql://root:Libertyme_007@localhost/app_cortinas"

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=SQLALCHEMY_DB_URL)
db = create_engine(SQLALCHEMY_DB_URL)

Session = sessionmaker(bind=db)
session = Session()
Base = declarative_base()

def conn_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
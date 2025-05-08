import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Carregar variáveis de ambiente do .env
load_dotenv()

# Obter a URI de conexão
DATABASE_URL = os.getenv('DB_URI')

# Criar a engine de conexão
engine = create_engine(DATABASE_URL)

# Criar a base do modelo
Base = declarative_base()

# Criar a sessão
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

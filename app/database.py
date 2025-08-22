# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

# ---------------- Base de données unique ----------------
DATABASE_URL = os.getenv("DATABASE_BIBLIO")  # Une seule URL

# Création du moteur
engine = create_engine(DATABASE_URL)

# Session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base déclarative
BaseLib = declarative_base()

# Dépendance pour obtenir une session
def get_db_lib():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

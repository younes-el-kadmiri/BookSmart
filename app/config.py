# app/config.py
from dotenv import load_dotenv
import os

load_dotenv()

# JWT
SECRET_KEY = os.getenv("SECRET_KEY", "super_secret_key_123")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

# Bases de données
DATABASE_LIB = os.getenv("DATABASE_BIBLIO")
DATABASE_SCRAP = os.getenv("DATABASE_SCRAP")

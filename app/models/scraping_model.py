# app/models/scraping_model.py
from sqlalchemy import Column, Integer, String
from app.database import BaseScrap  # ← utiliser BaseScrap pour scraping

class ScrapData(BaseScrap):
    __tablename__ = "scrap_data"

    id = Column(Integer, primary_key=True, index=True)
    titre = Column(String(200))
    auteur = Column(String(100))

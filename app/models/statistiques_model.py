from sqlalchemy import Column, Integer, String, Float
from app.database import BaseLib  # ✅ Base de la bibliothèque

class Statistiques(BaseLib):
    __tablename__ = "statistiques"
    id = Column(Integer, primary_key=True, index=True)
    livre_id = Column(Integer)
    nb_emprunts = Column(Integer, default=0)
    nb_reservations = Column(Integer, default=0)
    note_moyenne = Column(Float, default=0.0)

from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.database import BaseLib  # ✅ Base de la bibliothèque

class Recommandation(BaseLib):
    __tablename__ = "recommandations"
    id = Column(Integer, primary_key=True, index=True)
    lid_livre = Column(Integer, ForeignKey('livres.id_livre'))
    score = Column(Float, nullable=False)

    livre = relationship("Livre")


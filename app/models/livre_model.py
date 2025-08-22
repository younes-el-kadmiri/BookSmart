from sqlalchemy import Column, Integer, String, Boolean, Numeric, Text
from sqlalchemy.orm import relationship
from app.database import BaseLib  # ← utiliser BaseLib

class Livre(BaseLib):
    __tablename__ = "livres"

    id_livre = Column(Integer, primary_key=True, index=True)
    titre = Column(String(200), unique=True, index=True)
    auteur = Column(String(100), nullable=False)
    categorie = Column(String(50))
    genre = Column(String(50))
    disponible = Column(Boolean, default=True)
    prix = Column(Numeric(10, 2))
    description = Column(Text)  # ← nouvelle colonne pour la description

    emprunts = relationship("Emprunt", back_populates="livre")
    reservations = relationship("Reservation", back_populates="livre")

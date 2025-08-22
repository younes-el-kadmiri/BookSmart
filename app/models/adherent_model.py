from sqlalchemy import Column, Integer, ForeignKey, String
from app.database import BaseLib  # ← bibliothèque
from sqlalchemy.orm import relationship

class Adherent(BaseLib):

    __tablename__ = "adherents"

    id_adherent = Column(Integer, primary_key=True, index=True)
    id_utilisateur = Column(Integer, ForeignKey("utilisateurs.id_utilisateur"), unique=True)
    numero_carte = Column(String(50), unique=True)

    utilisateur = relationship("Utilisateur", back_populates="adherent")
    emprunts = relationship("Emprunt", back_populates="adherent")
    reservations = relationship("Reservation", back_populates="adherent")

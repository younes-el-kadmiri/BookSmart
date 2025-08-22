from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import BaseLib  # ← Utiliser la base de la bibliothèque

class Utilisateur(BaseLib):
    __tablename__ = "utilisateurs"

    id_utilisateur = Column(Integer, primary_key=True, index=True)
    nom = Column(String(100), nullable=False)
    prenom = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    mot_de_passe = Column(String(255), nullable=False)
    role = Column(String(50), nullable=False)  # "admin" ou "adherent"

    adherent = relationship("Adherent", back_populates="utilisateur", uselist=False)

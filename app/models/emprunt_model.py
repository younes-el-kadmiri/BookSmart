from sqlalchemy import Column, Integer, ForeignKey, Date
from app.database import BaseLib  # ✅ Base de la bibliothèque
from sqlalchemy.orm import relationship

class Emprunt(BaseLib):
    __tablename__ = "emprunts"

    id_emprunt = Column(Integer, primary_key=True, index=True)
    id_livre = Column(Integer, ForeignKey("livres.id_livre"))
    id_adherent = Column(Integer, ForeignKey("adherents.id_adherent"))
    date_emprunt = Column(Date)
    date_retour = Column(Date)

    livre = relationship("Livre", back_populates="emprunts")
    adherent = relationship("Adherent", back_populates="emprunts")

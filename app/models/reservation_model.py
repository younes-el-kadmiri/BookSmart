from sqlalchemy import Column, Integer, ForeignKey, Date
from app.database import BaseLib  # ✅ Base de la bibliothèque
from sqlalchemy.orm import relationship

class Reservation(BaseLib):
    __tablename__ = "reservations"

    id_reservation = Column(Integer, primary_key=True, index=True)
    id_livre = Column(Integer, ForeignKey("livres.id_livre"))
    id_adherent = Column(Integer, ForeignKey("adherents.id_adherent"))
    date_reservation = Column(Date)

    livre = relationship("Livre", back_populates="reservations")
    adherent = relationship("Adherent", back_populates="reservations")

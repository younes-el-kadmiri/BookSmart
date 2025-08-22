from sqlalchemy.orm import Session
from app.models.reservation_model import Reservation
from app.schemas.reservation import ReservationCreate

class ReservationService:

    def __init__(self, db: Session):
        self.db = db

    def create_reservation(self, reservation: ReservationCreate):
        db_res = Reservation(**reservation.dict())
        self.db.add(db_res)
        self.db.commit()
        self.db.refresh(db_res)
        return db_res

    def get_reservations(self, skip: int = 0, limit: int = 10):
        return self.db.query(Reservation).offset(skip).limit(limit).all()

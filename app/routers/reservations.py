from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db_lib
from app.services.reservation_service import ReservationService
from app.schemas.reservation import ReservationCreate, ReservationResponse

router = APIRouter(prefix="/reservations", tags=["Reservations"])

@router.get("/", response_model=list[ReservationResponse])
def get_reservations(db: Session = Depends(get_db_lib)):
    return ReservationService.get_all_reservations(db)

@router.post("/", response_model=ReservationResponse)
def create_reservation(reservation: ReservationCreate, db: Session = Depends(get_db_lib)):
    return ReservationService.create_reservation(db, reservation)

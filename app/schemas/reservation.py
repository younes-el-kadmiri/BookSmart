from pydantic import BaseModel
from datetime import datetime

class ReservationBase(BaseModel):
    livre_id: int
    adherent_id: int
    date_reservation: datetime | None = None

class ReservationCreate(ReservationBase):
    pass

class ReservationResponse(ReservationBase):
    id: int
    class Config:
        orm_mode = True

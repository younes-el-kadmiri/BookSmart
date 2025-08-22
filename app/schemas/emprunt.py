from pydantic import BaseModel
from datetime import datetime

class EmpruntBase(BaseModel):
    livre_id: int
    adherent_id: int
    date_emprunt: datetime | None = None
    date_retour: datetime | None = None

class EmpruntCreate(EmpruntBase):
    pass

class EmpruntResponse(EmpruntBase):
    id: int
    class Config:
        orm_mode = True

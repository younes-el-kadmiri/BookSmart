from pydantic import BaseModel

class StatistiquesBase(BaseModel):
    livre_id: int
    nb_emprunts: int = 0
    nb_reservations: int = 0
    note_moyenne: float = 0.0

class StatistiquesResponse(StatistiquesBase):
    id: int
    class Config:
        orm_mode = True

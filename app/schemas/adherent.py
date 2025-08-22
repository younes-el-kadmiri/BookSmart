from pydantic import BaseModel, EmailStr

class AdherentBase(BaseModel):
    nom: str
    prenom: str
    email: EmailStr
    telephone: str | None = None

class AdherentCreate(AdherentBase):
    pass

class AdherentResponse(AdherentBase):
    id: int
    class Config:
        orm_mode = True

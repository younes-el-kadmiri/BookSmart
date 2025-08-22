from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db_lib  # <-- Base bibliothèque
from app.services.user_service import UserService
from app.schemas.adherent import AdherentCreate, AdherentResponse

router = APIRouter(prefix="/adherents", tags=["Adherents"])

@router.get("/", response_model=list[AdherentResponse])
def get_all_adherents(db: Session = Depends(get_db_lib)):
    return UserService.get_all_users(db)

@router.post("/", response_model=AdherentResponse)
def create_adherent(adherent: AdherentCreate, db: Session = Depends(get_db_lib)):
    return UserService.create_user(db, adherent)

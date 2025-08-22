from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db_lib
from app.services.emprunt_service import EmpruntService
from app.schemas.emprunt import EmpruntCreate, EmpruntResponse

router = APIRouter(prefix="/emprunts", tags=["Emprunts"])

@router.get("/", response_model=list[EmpruntResponse])
def get_emprunts(db: Session = Depends(get_db_lib)):
    return EmpruntService.get_all_emprunts(db)

@router.post("/", response_model=EmpruntResponse)
def create_emprunt(emprunt: EmpruntCreate, db: Session = Depends(get_db_lib)):
    return EmpruntService.create_emprunt(db, emprunt)

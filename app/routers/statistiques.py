from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db_lib
from app.services.statistique_service import StatistiqueService

router = APIRouter(prefix="/statistiques", tags=["Statistiques"])

@router.get("/")
def get_stats(db: Session = Depends(get_db_lib)):
    return StatistiqueService.get_all_stats(db)

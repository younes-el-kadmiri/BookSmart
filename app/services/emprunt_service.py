from sqlalchemy.orm import Session
from app.models.emprunt_model import Emprunt
from app.schemas.emprunt import EmpruntCreate

class EmpruntService:

    def __init__(self, db: Session):
        self.db = db

    def create_emprunt(self, emprunt: EmpruntCreate):
        db_emprunt = Emprunt(**emprunt.dict())
        self.db.add(db_emprunt)
        self.db.commit()
        self.db.refresh(db_emprunt)
        return db_emprunt

    def get_emprunts(self, skip: int = 0, limit: int = 10):
        return self.db.query(Emprunt).offset(skip).limit(limit).all()

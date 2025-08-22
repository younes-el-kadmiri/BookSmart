from sqlalchemy.orm import Session
from app.models.adherent_model import Adherent
from app.schemas.adherent import AdherentCreate

class UserService:

    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user: AdherentCreate):
        db_user = Adherent(**user.dict())
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def get_users(self, skip: int = 0, limit: int = 10):
        return self.db.query(Adherent).offset(skip).limit(limit).all()

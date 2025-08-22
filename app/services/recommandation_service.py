from app.ml.recommender import Recommender
from app.models.recommandation_model import Recommandation
from sqlalchemy.orm import Session

class RecommandationService:

    def __init__(self, db: Session):
        self.db = db
        self.recommender = Recommender()

    def get_recommendations_for_user(self, user_id: int):
        recs = self.recommender.recommend(user_id)
        return recs

    def save_recommendations(self, user_id: int):
        recs = self.get_recommendations_for_user(user_id)
        for rec in recs:
            r = Recommandation(user_id=user_id, livre_id=rec["book_index"], score=rec["score"])
            self.db.add(r)
        self.db.commit()

from pydantic import BaseModel

class RecommandationBase(BaseModel):
    livre_id: int
    score: float

class RecommandationCreate(RecommandationBase):
    pass

class RecommandationResponse(RecommandationBase):
    id: int
    class Config:
        orm_mode = True

from pydantic import BaseModel

class LivreBase(BaseModel):
    titre: str
    auteur: str
    categorie: str | None = None
    genre: str | None = None
    disponible: bool = True
    prix: float
    description: str | None = None  # ← ajouté

class LivreCreate(LivreBase):
    pass

class LivreSchema(LivreBase):
    id_livre: int

    class Config:
        from_attributes = True  # anciennement orm_mode

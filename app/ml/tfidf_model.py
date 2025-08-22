# app/ml/tfidf_model.py
import os
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

MODEL_PATH = os.getenv("RECO_MODEL_PATH", "app/ml/model.pkl")

def build_tfidf_model(livres):
    """
    livres: liste de dicts contenant 'texte' et 'titre'
    Sauvegarde {vectorizer, matrix, livres} dans MODEL_PATH.
    """
    corpus = [b["texte"] if b["texte"] else (b["titre"] or "") for b in livres]
    vectorizer = TfidfVectorizer(stop_words="english", max_features=5000)
    tfidf_matrix = vectorizer.fit_transform(corpus)

    with open(MODEL_PATH, "wb") as f:
        pickle.dump(
            {"vectorizer": vectorizer, "matrix": tfidf_matrix, "livres": livres},
            f
        )
    return True

def load_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Modèle introuvable: {MODEL_PATH}")
    with open(MODEL_PATH, "rb") as f:
        return pickle.load(f)

# app/ml/recommender.py
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from app.ml.tfidf_model import load_model

def _top_indices(scores_row, top_n=5, exclude_index=None):
    # Trie décroissant, récupère indices
    order = np.argsort(scores_row)[::-1]
    results = []
    for idx in order:
        if exclude_index is not None and idx == exclude_index:
            continue
        results.append(int(idx))
        if len(results) >= top_n:
            break
    return results

def recommend_by_title(title: str, top_n: int = 5):
    data = load_model()
    livres = data["livres"]
    matrix = data["matrix"]

    # Trouver index du livre
    idx = next((i for i, l in enumerate(livres) if l["titre"].lower() == title.lower()), None)
    if idx is None:
        return []

    scores = cosine_similarity(matrix[idx:idx+1], matrix)[0]
    top_idx = _top_indices(scores, top_n=top_n, exclude_index=idx)
    return [livres[i] for i in top_idx]

def recommend_by_description(description: str, top_n: int = 5):
    data = load_model()
    vectorizer = data["vectorizer"]
    matrix = data["matrix"]
    livres = data["livres"]

    query_vec = vectorizer.transform([description])
    scores = cosine_similarity(query_vec, matrix)[0]
    top_idx = _top_indices(scores, top_n=top_n)
    return [livres[i] for i in top_idx]

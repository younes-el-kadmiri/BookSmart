import pickle
from sklearn.metrics.pairwise import cosine_similarity

class Similarity:

    @staticmethod
    def load_similarity_matrix(path: str = "data/recommandations/similarity_matrix.pkl"):
        with open(path, "rb") as f:
            return pickle.load(f)

    @staticmethod
    def compute_similarity(matrix, item_index):
        sim_scores = list(enumerate(cosine_similarity(matrix[item_index:item_index+1], matrix)[0]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        return sim_scores[1:6]  # top 5 similaires

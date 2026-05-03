import pickle
from sklearn.neighbors import NearestNeighbors

features = pickle.load(open("model/features.pkl", "rb"))
filenames = pickle.load(open("model/filenames.pkl", "rb"))

neighbors = NearestNeighbors(n_neighbors=6, algorithm='brute', metric='euclidean')
neighbors.fit(features)

def get_neighbors(query_features):
    dist, indices = neighbors.kneighbors([query_features])
    return indices[0], filenames
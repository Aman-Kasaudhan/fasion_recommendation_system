import pickle
from sklearn.neighbors import NearestNeighbors
import streamlit as st
@st.cache_resource
def load_file():
    with open("model/filenames.pkl", "rb") as f:
        return pickle.load(f)

filenames = load_file()

def load_feature():
    with open("model/features.pkl", "rb") as f:
        return pickle.load(f)

features = load_feature()

# features = pickle.load(open("model/features.pkl", "rb"))
# filenames = pickle.load(open("model/filenames.pkl", "rb"))

neighbors = NearestNeighbors(n_neighbors=6, algorithm='brute', metric='euclidean')
neighbors.fit(features)

def get_neighbors(query_features):
    dist, indices = neighbors.kneighbors([query_features])
    return indices[0], filenames
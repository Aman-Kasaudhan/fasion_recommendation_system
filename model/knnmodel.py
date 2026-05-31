import pickle
from sklearn.neighbors import NearestNeighbors
import streamlit as st
import numpy as np



filenames = pickle.load(open("model/filenames1.pkl","rb"))


features = np.load("model/features1.npy")
# filenames = pickle.load(open("model/filenames.pkl", "rb"))

neighbors = NearestNeighbors(n_neighbors=6, algorithm='brute', metric='euclidean')
neighbors.fit(features)

def get_neighbors(query_features):
    dist, indices = neighbors.kneighbors([query_features])
    return indices[0], filenames
import numpy as np
import pickle
from numpy.linalg import norm
import tensorflow
from tensorflow.keras.preprocessing import image
# from tensorflow.keras.layers import GlobalMaxPooling2D
from tensorflow.keras.applications.resnet50 import ResNet50,preprocess_input
# import matplotlib.pyplot as plt
import os
import streamlit as st
@st.cache_resource
def load_model():
    with open("model/modelfashion.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()
# model=pickle.load(open('model/modelfashion.pkl','rb'))
# C:\projects\fashion\model\modelfashion.pkl

def extract_feature(img_path):
    img=image.load_img(img_path,target_size=(224,224))
    img_array=image.img_to_array(img)
    expand_img_array=np.expand_dims(img_array,axis=0)
    preprocessed_img=preprocess_input(expand_img_array)
    result=model.predict(preprocessed_img).flatten()
    return result/norm(result)
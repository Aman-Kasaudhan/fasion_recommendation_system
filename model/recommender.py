import numpy as np
import pickle
from numpy.linalg import norm
import tensorflow
from tensorflow.keras.preprocessing import image
from tensorflow.keras.layers import GlobalMaxPooling2D
from tensorflow.keras.applications.resnet50 import ResNet50,preprocess_input
import matplotlib.pyplot as plt
import os
import streamlit as st
model=ResNet50(weights="imagenet",include_top=False,input_shape=(224,224,3))
model.trainable=False
model=tensorflow.keras.Sequential([
    model,
    GlobalMaxPooling2D() # our top layer
])
# model.summary()
# model=pickle.load(open('model/modelfashion.pkl','rb'))
# C:\projects\fashion\model\modelfashion.pkl

def extract_feature(img_path):
    img=image.load_img(img_path,target_size=(224,224))
    img_array=image.img_to_array(img)
    expand_img_array=np.expand_dims(img_array,axis=0)
    preprocessed_img=preprocess_input(expand_img_array)
    result=model.predict(preprocessed_img).flatten()
    return result/norm(result)
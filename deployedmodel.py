import streamlit as st
import tensorflow as tf

@st.cache_data()
def load_model():
  model=tf.keras.models.load_model('model.h5')
  return model
model=load_model()
st.title("""
# Pistachio species identifier"""
)

st.subheader('Please upload a square image e.g. 100x100, 60x60.')
st.subheader('To avoid error, please ensure that the color depth is set to 24 bit.')

file=st.file_uploader("Choose plant photo from computer",type=["jpg","png"])

import cv2
from PIL import Image,ImageOps
import numpy as np
def import_and_predict(image_data,model):
    size=(64,64)
    image=ImageOps.fit(image_data,size,Image.LANCZOS)
    img=np.asarray(image)
    img_reshape=img[np.newaxis,...]
    prediction=model.predict(img_reshape)
    prediction = (prediction > 0.5).astype(int)[0][0]
    return prediction
if file is None:
    st.text("Please upload an image file")
else:
    image=Image.open(file)
    st.image(image,use_column_width=True)
    prediction=import_and_predict(image,model)
    class_names=['kirmizi','siirt']
    string="OUTPUT : "+class_names[prediction]
    st.success(string)

import streamlit as st
import tensorflow as tf

@st.cache_resource
def load_model():
  model=tf.keras.models.load_model('model.h5')
  return model
model=load_model()
st.write("""
# Pistachio species identifier"""
)
st.divider()
st.image('pexels-pixabay-52521.jpg',width=700)
st.divider()
st.write('To avoid error, please ensure that the color depth is set to 24 bit & to upload a square image e.g. 100x100, 60x60.')
st.divider()

if 'checkbox_1_selected' not in st.session_state:
    st.session_state.checkbox_1_selected = False

if 'checkbox_2_selected' not in st.session_state:
    st.session_state.checkbox_2_selected = False

st.write('The picture that I am uploading:')
st.session_state.checkbox_1_selected = st.checkbox("has a square aspect ratio.", key="checkbox_1")
st.session_state.checkbox_2_selected = st.checkbox("has a 24-bit color depth.", key="checkbox_2")

both_checkboxes_selected = st.session_state.checkbox_1_selected and st.session_state.checkbox_2_selected

upload_button_disabled = not both_checkboxes_selected
uploaded_file = st.file_uploader("Choose plant photo from computer",type=["jpg","png"], disabled=upload_button_disabled)



st.sidebar.write('This model aims to classify the species \n of the uploaded image.')
st.sidebar.caption('Kindly tick all the checkbox to proceed')

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
if uploaded_file is None:
    st.caption("Please upload an image file")
else:
    image=Image.open(uploaded_file)
    st.image(image,use_column_width=True)
    prediction=import_and_predict(image,model)
    class_names=['kirmizi','siirt']
    string="This is a "+class_names[prediction]+" nut."
    st.info(string)

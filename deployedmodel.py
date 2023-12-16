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



if 'checkbox_selected' not in st.session_state:
    st.session_state.checkbox_selected = False

# Checkbox buttons to select options
selected_options = st.checkbox("Option 1", key="checkbox_1")
selected_options |= st.checkbox("Option 2", key="checkbox_2")
selected_options |= st.checkbox("Option 3", key="checkbox_3")

# Update session state based on checkbox button selection
st.session_state.checkbox_selected = selected_options

# Upload button that is disabled until at least one checkbox is selected
upload_button_disabled = not st.session_state.checkbox_selected
uploaded_file = st.file_uploader("Upload a file", key="file_uploader", disabled=upload_button_disabled)

# Display uploaded file content if available
if uploaded_file is not None:
    st.write("File content:")
    st.write(uploaded_file.read())


# file=st.file_uploader("Choose plant photo from computer",type=["jpg","png"])
st.sidebar.write('This model aims to classify the species of the uploaded image.')
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
    st.caption("Please upload an image file")
else:
    image=Image.open(file)
    st.image(image,use_column_width=True)
    prediction=import_and_predict(image,model)
    class_names=['kirmizi','siirt']
    string="OUTPUT : "+class_names[prediction]
    st.info(string)

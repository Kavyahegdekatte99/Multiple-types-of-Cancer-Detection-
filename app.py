import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
from keras.models import load_model
import streamlit as st
from PIL import Image
import base64
from gtts import gTTS
import subprocess
# Function to get base64 encoding of a file
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Function to set the background of the Streamlit app
def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/jpeg;base64,%s");
    background-position: center;
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown('<style>h1 { color: Black ; }</style>', unsafe_allow_html=True)
    st.markdown('<style>p { color: Black; }</style>', unsafe_allow_html=True)
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background('background/6.webp')

# Streamlit app title
st.title("Project : Multiple Types of Cancer Classification Using CT/MRI Images Based on Learning without Forgetting Powered Deep Learning Models")


# Buttons for user interaction
if st.button('Brain Cancer Detection '):
    st.write('Running Brain Cancer  Detection ...')
    subprocess.run(["streamlit", "run", "brainapp.py"], shell=True)
elif st.button(' Breast Cancer  Detection'):
    st.write('Running Breast Cancer  Detection ...')
    subprocess.run(["streamlit", "run", "breastapp.py"], shell=True)
elif st.button(' Kidney Cancer Detection '):
    st.write('Running Kidney Cancer  Detection ...')
    subprocess.run(["streamlit", "run", "kidneyapp.py"], shell=True)
elif st.button(' Lung Cancer Detection'):
    st.write('Running  Lung Cancer  Detection ...')
    subprocess.run(["streamlit", "run", "lungapp.py"], shell=True)
elif st.button(' Oral Cancer Detection'):
    st.write('Running Oral Cancer Detection ...')
    subprocess.run(["streamlit", "run", "Oralapp.py"], shell=True)    
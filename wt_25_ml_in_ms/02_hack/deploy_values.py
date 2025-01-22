# In VSCode on Coder
# Make sure you are in the right directory. Paths are with respect to the directory where you are. 
# Check your directory with `pwd` in the terminal

# Run streamlit server with `uv run streamlit run streamlit.py`; usually automatically opens the website in the browser
# CTRL + C to stop the server

# If this is not working, use the "PORTS" tab in VScode  (CTRL+shit+P, then type "Ports" and select "Focus on ports view") 
# to forward the port to localhost and view it your local browser 

# OR use preview browser in VScode

#### Follow this

# (1) See the API documentation at https://docs.streamlit.io/develop/api-reference
# Add `st.text_input` or `st.slider` to gather the necessary inputs

# (2) Create a button to trigger model inference: `if st.button("Predict"):`

# (3) Print the results of the prediction on the website
# Load your AutoGluon model from the first hackathon 

# (4) Make the website look nice

import streamlit as st
from transformers import pipeline

import pandas as pd
from autogluon.tabular import TabularPredictor
import os

# Dont use GPUS (they are usually)
os.environ['CUDA_VISIBLE_DEVICES'] = ''

# model_path = f"your path to the model"
# predictor = TabularPredictor.load(model_path)


def main():
    st.title("My cool ML model predictor 🍩👀")



if __name__ == '__main__':
    main()

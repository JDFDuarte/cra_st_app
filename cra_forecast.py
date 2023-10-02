import os

import streamlit as st
import pandas as pd
import numpy as np
from urllib.request import urlopen
from PIL import Image
import base64
from blinker import signal


# ________________________________________________________________________________________

path = os.path.dirname(__file__)

migros_logo = Image.open(path + "/migros-logo.png")


# ________________________________________________________________________________________


st.title("Customer Data Analytics Challenge - Yoghurt Use Case") 
st.image(migros_logo, width = 150)
    
st.sidebar.info("Problem Statement: build a forecasting model to predict yoghurt sales")

st.write("The sales records from 20 different products were provided to the students, in a .csv format. The files contain information from different products (common yoghurt, kefir yoghurt, greek yoghurt, without lactose) in a variety of flavors (such as natural, strawberry, apple-mango, chocolate). The weight of the products also varies from 150 to 500g. \n The data belongs to a specific region (not determined) of Switzerland, so does not reflect the nationwide sales. \n The goal is to build a forecasting model to predict the sales of these products.")
#"For that, the students were given liberty to select which techniques they would like to explore in order to build their model.
#"Important notes:"
#"- promotions usually last from Tuesday to Tuesday, but week is from Monday to Monday. It may look like an item was a promotional article for 2 weeks in a row when in fact Monday was part of the promotion.")


st.write("a logo and text next to eachother")
col1, col2 = st.columns(2, gap = "small")
with col1:
    st.image(migros_logo, width=150)
with col2:
    st.header('Challenge - Yoghurt Use Case')


 # ________________________________________________________________________________________

# aha_lakt_classic = pd.read_csv(r".\ca_training_data_hs23\aha_jogh_lakt_classic.csv")
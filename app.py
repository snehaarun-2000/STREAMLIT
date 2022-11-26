import streamlit as st
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
import pickle


st.write("""
# Multiplication of 2 numbers
""")
#Get Input

st.header('Input Parameters')

def user_input_features():

    num1 = st.number_input("NUMBER 1",min_value=0.0,max_value=2000000.0)
    num2 = st.number_input("NUMBER 2",min_value=0.0,max_value=2000000.0)
    

st.write(num1*num2)

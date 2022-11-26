import streamlit as st
import pandas as pd
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
    
    data = {'NUMBER 1': num1,
            'NUMBER 2': num2
            }
    features = pd.DataFrame(data, index=[0])
    return features
    
df = user_input_features()
st.write(df.to_dict())
continous_features = ['NUMBER 1','NUMBER 2']
L=df['NUMBER 1']*df['NUMBER 2']
st.write(L)

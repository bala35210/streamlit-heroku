import streamlit as st
import pandas as pd


st.write("""
# Multiplication of two numbers

This app multiplies two numbers and outputs it.
""")
#Get Input

st.header('User Input Parameters')

def user_input_features():
    first_number = st.number_input("FIRST_NUMBER")
    second_number = st.number_input("SECOND_NUMBER")

    data = {'FIRST_NUMBER': first_number,
            'SECOND_NUMBER': second_number,
           }
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df.to_dict())

st.subheader('Output')
st.write(df.iloc[0]['FIRST_NUMBER'] * df.iloc[0]['SECOND_NUMBER'])


import streamlit as st
import requests

st.title('Iris Species Prediction')

sepal_length = st.slider('Sepal Length', 0, 50)
sepal_width = st.slider('Sepal Width', 0, 50)
petal_length = st.slider('Petal Length', 0, 50)
petal_width = st.slider('Petal Width', 0, 50)

if st.button('Predict'):
    data = {
        'data' :[sepal_length, sepal_width, petal_length, petal_width]
    }

    response = requests.post('http://127.0.0.1:5000/predict', json=data)
    prediction = response.json()['prediction']
    st.write(f'Prediction: {prediction}')

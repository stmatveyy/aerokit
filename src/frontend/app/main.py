import streamlit as st
import requests

st.title("APP")

def call():
    response = requests.get("http://127.0.0.1:8080/info")
    return response.json()

x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

a = st.button(label="Нажми")
if a:
    res = call()
    st.write(res)
    
with st.form(key="myform"):
    name = st.text_input("Имя")
    num = st.time_input("tgt")
    st.form_submit_button("Отправить")


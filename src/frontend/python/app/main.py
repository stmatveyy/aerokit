import streamlit as st
import requests

st.title("APP")

def call():
    response = requests.get("http://127.0.0.1:8080/info")
    return response.json()






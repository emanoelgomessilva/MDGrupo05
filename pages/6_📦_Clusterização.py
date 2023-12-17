
import streamlit as st
import mysql.connector as cnt
import matplotlib.pyplot as plt

conexao = cnt.connect(
    host="localhost",
    user="root",
    password="root",
    database="tabelao"
)

st.write('<h1>Pergunta 1 (<i>clustering</i>)</h1>', unsafe_allow_html=True)
st.write('''Texto da pergunta 1''', unsafe_allow_html=True)

def builder_body():
    Kmeans()


def Kmeans():


    st.sidebar.header('Configurações do Gráfico')
    filtro_1 = st.sidebar.text_input('Filtro 1')
    filtro_2 = st.sidebar.text_input('Filtro 2')

builder_body()

import streamlit as st
import mysql.connector as cnt
import matplotlib.pyplot as plt
import pandas as pd

conexao = cnt.connect(
    host="localhost",
    user="root",
    password="root",
    database="dw_convenios"
)

st.write('<h1>Pergunta 3</h1>', unsafe_allow_html=True)
st.write('''Qual órgão superior teve maior uso das verbas nos últimos 10 anos?''', unsafe_allow_html=True)

def builder_body():
    Pergunta_3()


def Pergunta_3():

    consulta_sql = "SELECT dos.NOME_ORGAO_SUPERIOR, SUM(VALOR_CONVENIO) as valor_convenio FROM dim_orgao_superior as dos inner join fatoconvenios as fc inner join dimdata as dt where dos.sk_orgao_superior = fc.k_Orgao_Superior and dt.keyData = fc.k_Data and dt.ano_id > 2013 GROUP BY dos.NOME_ORGAO_SUPERIOR ORDER BY valor_convenio DESC LIMIT 5"
    dados = pd.read_sql_query(consulta_sql, conexao)

    fig, ax = plt.subplots()
    bars = ax.bar(dados['NOME_ORGAO_SUPERIOR'], dados['valor_convenio'])
    ax.set_xlabel('Órgão superior')
    ax.set_ylabel('Valores em convênios')
    ax.set_title('Gráfico de Barras')

    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom')

    st.write('''Gráfico da quantidade de convênios por estado''', unsafe_allow_html=True)
    st.pyplot(fig)
    st.table(dados)

builder_body()

import streamlit as st
import mysql.connector as cnt
import matplotlib.pyplot as plt
import pandas as pd
import main

conexao = main.conexao

st.write('<h1>Pergunta 4</h1>', unsafe_allow_html=True)
st.write('''Considerando os anos de maior impacto da covid-19, 2020-2021-2022, o que houve com a média de gastos, comparando com os a média dos 3 anos anteriores, 2017-2018-2019?''', unsafe_allow_html=True)

def builder_body():
    Pergunta_3()


def Pergunta_3():

    consulta_sql = "SELECT dos.NOME_ORGAO_SUPERIOR, AVG(VALOR_CONVENIO) as valor_convenio FROM dim_orgao_superior as dos inner join fatoconvenios as fc inner join dimdata as dt where dos.sk_orgao_superior = fc.k_Orgao_Superior and dt.keyData = fc.k_Data and dt.ano_id >= 2019 and dt.ano_id <= 2022 GROUP BY dos.NOME_ORGAO_SUPERIOR ORDER BY valor_convenio DESC"
    dados = pd.read_sql_query(consulta_sql, conexao)

    fig, ax = plt.subplots()
    bars = ax.bar(dados['NOME_ORGAO_SUPERIOR'], dados['valor_convenio'])
    ax.set_xlabel('Órgão superior')
    ax.set_ylabel('Média de valores')
    ax.set_title('Gráfico de Barras')

    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom')

    consulta_sql_2 = "SELECT dos.NOME_ORGAO_SUPERIOR, AVG(VALOR_CONVENIO) as valor_convenio FROM dim_orgao_superior as dos inner join fatoconvenios as fc inner join dimdata as dt where dos.sk_orgao_superior = fc.k_Orgao_Superior and dt.keyData = fc.k_Data and dt.ano_id >= 2017 and dt.ano_id <= 2019 GROUP BY dos.NOME_ORGAO_SUPERIOR ORDER BY valor_convenio DESC"
    dados_2 = pd.read_sql_query(consulta_sql_2, conexao)

    fig_2, ax_2 = plt.subplots()
    bars_2 = ax_2.bar(dados_2['NOME_ORGAO_SUPERIOR'], dados_2['valor_convenio'])
    ax_2.set_xlabel('Órgão superior')
    ax_2.set_ylabel('Média de valores')
    ax_2.set_title('Gráfico de Barras')

    for bar in bars_2:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom')

    # st.write('''Gráfico com média de gastos por órgão superior de 2019 a 2022''', unsafe_allow_html=True)
    # st.pyplot(fig)
    # st.table(dados)
    st.write('''Gráfico com média de gastos por órgão superior de 2017 a 2019''', unsafe_allow_html=True)
    st.pyplot(fig_2)
    st.table(dados_2)

builder_body()

import streamlit as st
import mysql.connector as cnt
import matplotlib.pyplot as plt
import pandas as pd
import main

conexao = main.conexao



st.write('<h1>Pergunta 1</h1>', unsafe_allow_html=True)
st.write('''Qual é o período do ano em que mais são fechados contratos, em termos de trimestres e a média de valores expedidos nesses trimestres?''', unsafe_allow_html=True)

def builder_body():
    Pergunta_1()


def Pergunta_1():


    st.sidebar.header('Configurações do Gráfico')
    filtro_1 = st.sidebar.slider('Selecione o ano', min_value = 2008, max_value = 2023)

    consulta_sql = "SELECT trimestre_nome, COUNT(*) as quantidade FROM dimdata inner join fatoconvenios  where k_Data = keyData and ano_nome = "+"'"+str(filtro_1)+"'"+ "GROUP BY trimestre_nome"
    dados = pd.read_sql_query(consulta_sql, conexao)

    consulta_sql_2 = "SELECT dt.trimestre_nome, AVG(fc.VALOR_CONVENIO) as mediana_valores FROM dimdata as dt inner join fatoconvenios as fc  where dt.keyData = fc.k_Data and dt.ano_nome = "+"'"+str(filtro_1)+"'"+ "GROUP BY trimestre_nome"
    dados_2 = pd.read_sql_query(consulta_sql_2, conexao)

    fig, ax = plt.subplots()
    ax.bar(dados['trimestre_nome'], dados['quantidade'])
    ax.set_xlabel('Trimestre')
    ax.set_ylabel('Quantidade')
    ax.set_title('Gráfico de Barras')

    fig2, ax2 = plt.subplots()
    ax2.bar(dados_2['trimestre_nome'], round(dados_2['mediana_valores'], 1))
    ax2.set_xlabel('Trimestre') 
    ax2.set_ylabel('Mediana de valores do convênio')
    ax2.set_title('Gráfico de Barras')

    st.write('''Gráfico da quantidade de convênios por trimestre''', unsafe_allow_html=True)
    st.pyplot(fig)
    st.write('''Gráfico da mediana de valores de convênios por trimestre''', unsafe_allow_html=True)
    st.pyplot(fig2)
    st.table(dados_2)

builder_body()
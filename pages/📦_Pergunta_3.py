import streamlit as st
import pandas as pd
import main
import altair as alt

conexao = main.conexao

st.write('<h1>Pergunta 3</h1>', unsafe_allow_html=True)
st.write('''Qual órgão superior teve maior uso das verbas nos últimos 10 anos?''', unsafe_allow_html=True)

def builder_body():
    Pergunta_3()

def Pergunta_3():

    consulta_sql = "SELECT dos.NOME_ORGAO_SUPERIOR, SUM(VALOR_CONVENIO) as valor_convenio FROM dim_orgao_superior as dos inner join fatoconvenios as fc inner join dimdata as dt where dos.sk_orgao_superior = fc.k_Orgao_Superior and dt.keyData = fc.k_Data and dt.ano_id > 2013 GROUP BY dos.NOME_ORGAO_SUPERIOR ORDER BY valor_convenio DESC LIMIT 5"
    dados = pd.read_sql_query(consulta_sql, conexao)

    st.write('''Tabela de dados:''', unsafe_allow_html=True)
    st.table(dados)

    chart = alt.Chart(dados).mark_bar().encode(
        x='NOME_ORGAO_SUPERIOR',
        y='valor_convenio',
        tooltip=['NOME_ORGAO_SUPERIOR', 'valor_convenio']
    ).interactive()

    st.write('''Gráfico da quantidade de convênios por órgão superior''', unsafe_allow_html=True)
    st.altair_chart(chart, use_container_width=True)

builder_body()
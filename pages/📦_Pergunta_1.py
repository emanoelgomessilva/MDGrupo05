import streamlit as st
import pandas as pd
import main
import altair as alt

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

    consulta_sql_2 = "SELECT dt.trimestre_nome, AVG(fc.VALOR_CONVENIO) as media_valores FROM dimdata as dt inner join fatoconvenios as fc  where dt.keyData = fc.k_Data and dt.ano_nome = "+"'"+str(filtro_1)+"'"+ "GROUP BY trimestre_nome"
    dados_2 = pd.read_sql_query(consulta_sql_2, conexao)

    st.write('''Tabela de dados:''', unsafe_allow_html=True)
    st.table(dados)

    chart = alt.Chart(dados).mark_bar().encode(
        x= alt.X('trimestre_nome', title='Trimestre'),
        y=alt.Y('quantidade', title='Quantidade de convênios'),
        tooltip=['trimestre_nome', 'quantidade']
    ).interactive()

    st.write('''Gráfico da quantidade de convênios por trimestre''', unsafe_allow_html=True)
    st.altair_chart(chart, use_container_width=True)

    st.write('''Tabela de dados:''', unsafe_allow_html=True)
    st.table(dados_2)

    chart_2 = alt.Chart(dados_2).mark_bar().encode(
        x= alt.X('trimestre_nome', title='Trimestre'),
        y=alt.Y('media_valores', title='Média de valores de convênios'),
        tooltip=['trimestre_nome', 'media_valores']
    ).interactive()

    st.write('''Gráfico da média de valores de convênios por trimestre''', unsafe_allow_html=True)
    st.altair_chart(chart_2, use_container_width=True)

builder_body()
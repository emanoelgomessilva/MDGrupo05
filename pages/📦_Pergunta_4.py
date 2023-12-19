import streamlit as st
import pandas as pd
import main
import altair as alt

conexao = main.conexao

st.write('<h1>Pergunta 4</h1>', unsafe_allow_html=True)
st.write('''Considerando os anos de maior impacto da covid-19, 2020-2021-2022, o que houve com a média de gastos, comparando com os a média dos 3 anos anteriores, 2017-2018-2019?''', unsafe_allow_html=True)

def builder_body():
    Pergunta_3()

def Pergunta_3():

    consulta_sql = "SELECT dos.NOME_ORGAO_SUPERIOR, AVG(VALOR_CONVENIO) as valor_convenio FROM dim_orgao_superior as dos inner join fatoconvenios as fc inner join dimdata as dt where dos.sk_orgao_superior = fc.k_Orgao_Superior and dt.keyData = fc.k_Data and dt.ano_id >= 2019 and dt.ano_id <= 2022 GROUP BY dos.NOME_ORGAO_SUPERIOR ORDER BY valor_convenio DESC"
    dados = pd.read_sql_query(consulta_sql, conexao)

    consulta_sql_2 = "SELECT dos.NOME_ORGAO_SUPERIOR, AVG(VALOR_CONVENIO) as valor_convenio FROM dim_orgao_superior as dos inner join fatoconvenios as fc inner join dimdata as dt where dos.sk_orgao_superior = fc.k_Orgao_Superior and dt.keyData = fc.k_Data and dt.ano_id >= 2017 and dt.ano_id <= 2019 GROUP BY dos.NOME_ORGAO_SUPERIOR ORDER BY valor_convenio DESC"
    dados_2 = pd.read_sql_query(consulta_sql_2, conexao)

    st.write('''Tabela de dados:''', unsafe_allow_html=True)
    st.table(dados)

    chart = alt.Chart(dados).mark_bar().encode(
        x= alt.X('NOME_ORGAO_SUPERIOR', title='Nome do órgão superior'),
        y=alt.Y('valor_convenio', title='Valores em convênio'),
        tooltip=['NOME_ORGAO_SUPERIOR', 'valor_convenio']
    ).interactive()

    st.write('''Gráfico com média de gastos por órgão superior de 2019 a 2022''', unsafe_allow_html=True)
    st.altair_chart(chart, use_container_width=True)

    st.write('''Tabela de dados:''', unsafe_allow_html=True)
    st.table(dados_2)

    chart_2 = alt.Chart(dados_2).mark_bar().encode(
        x= alt.X('NOME_ORGAO_SUPERIOR', title='Nome do órgão superior'),
        y=alt.Y('valor_convenio', title='Valores em convênio'),
        tooltip=['NOME_ORGAO_SUPERIOR', 'valor_convenio']
    ).interactive()

    st.write('''Gráfico com média de gastos por órgão superior de 2017 a 2019''', unsafe_allow_html=True)
    st.altair_chart(chart_2, use_container_width=True)

builder_body()
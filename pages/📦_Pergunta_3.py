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

    st.sidebar.header('Configurações do Gráfico')
    filtro_1 = st.sidebar.selectbox('Selecione um estado', [
                            'AC',
                            'AL',
                            'AP',
                            'AM',
                            'BA',
                            'CE',
                            'DF',
                            'ES',
                            'GO',
                            'MA',
                            'MS',
                            'MT',
                            'MG',
                            'PA',
                            'PB',
                            'PR',
                            'PE',
                            'PI',
                            'RJ',
                            'RN',
                            'RS',
                            'RO',
                            'RR',
                            'SC',
                            'SP',
                            'SE',
                            'TO',
                        ])
    
    filtro_2 = st.sidebar.selectbox('De:', [
                            '2013',
                            '2014',
                            '2015',
                            '2016',
                            '2017',
                            '2018',
                            '2019',
                            '2020',
                            '2021',
                            '2022',
                            '2023',
                        ])
    
    filtro_3 = st.sidebar.selectbox('Até:', [
                            '2013',
                            '2014',
                            '2015',
                            '2016',
                            '2017',
                            '2018',
                            '2019',
                            '2020',
                            '2021',
                            '2022',
                            '2023',
                        ])
    
    consulta_filtro_orgao_superior = "select NOME_ORGAO_SUPERIOR from dw_convenios.dim_orgao_superior limit 0, 1000"
    lista_orgao_superior = pd.read_sql_query(consulta_filtro_orgao_superior, conexao)
    
    filtro_4 = st.sidebar.selectbox('Selecione um órgão superior', lista_orgao_superior)

    consulta_filtro_orgao_concedente = "select NOME_ORGAO_CONCEDENTE from dw_convenios.dim_orgao_concedente limit 0, 1000"
    lista_orgao_concedente = pd.read_sql_query(consulta_filtro_orgao_concedente, conexao)
    
    filtro_5 = st.sidebar.selectbox('Selecione um órgão concedente', lista_orgao_concedente)

    consulta_filtro_ug_concedente = "select NOME_UG_CONCEDENTE from dw_convenios.dim_ug_concedente limit 0, 1000"
    lista_ug_concedente = pd.read_sql_query(consulta_filtro_ug_concedente, conexao)
    
    filtro_6 = st.sidebar.selectbox('Selecione uma UG concedente', lista_ug_concedente)

    consulta_sql = "SELECT dos.NOME_ORGAO_SUPERIOR, SUM(VALOR_CONVENIO) as valor_convenio FROM dim_orgao_superior as dos inner join fatoconvenios as fc on dos.sk_orgao_superior = fc.k_Orgao_Superior inner join dim_ug_concedente as ugc on ugc.sk_ug_concedente = fc.k_UG_Concedente inner join dim_orgao_concedente as doc on doc.sk_orgao_concedente = fc.k_Orgao_Concedente inner join dim_municipio as dm on dm.sk_municipio = fc.k_Municipio inner join dimdata as dt on dt.keyData = fc.k_Data and dm.sk_municipio = fc.k_Municipio and dm.UF ="+"'"+str(filtro_1)+"'"

    consulta_sql += "and dt.ano_id >= "+str(filtro_2)+" and dt.ano_id <= "+str(filtro_3)

    if filtro_4 != None:
        consulta_sql += " and dos.NOME_ORGAO_SUPERIOR ="+"'"+filtro_4+"'"

    if filtro_5 != None:
        consulta_sql += " and doc.NOME_ORGAO_CONCEDENTE ="+"'"+filtro_5+"'"

    if filtro_6 != None:
       consulta_sql += " and ugc.NOME_UG_CONCEDENTE ="+"'"+filtro_6+"'"


    consulta_sql+= " GROUP BY dos.NOME_ORGAO_SUPERIOR ORDER BY valor_convenio DESC"
    dados = pd.read_sql_query(consulta_sql, conexao)

    st.write('''Tabela de dados:''', unsafe_allow_html=True)
    st.table(dados)

    chart = alt.Chart(dados).mark_bar().encode(
        x= alt.X('NOME_ORGAO_SUPERIOR', title='Nome do órgão superior'),
        y=alt.Y('valor_convenio', title='Valores em convênio'),
        tooltip=['NOME_ORGAO_SUPERIOR', 'valor_convenio']
    ).interactive()

    st.write('''Gráfico da quantidade de convênios por órgão superior''', unsafe_allow_html=True)
    st.altair_chart(chart, use_container_width=True)

builder_body()
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

    filtro_1 = st.sidebar.selectbox('De:', [
                            '2008',
                            '2009',
                            '2010',
                            '2011',
                            '2012',
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
    
    filtro_2 = st.sidebar.selectbox('Até:', [
                            '2008',
                            '2009',
                            '2010',
                            '2011',
                            '2012',
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

    filtro_3 = st.sidebar.selectbox('Selecione um estado', [
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
    
    consulta_filtro_orgao_superior = "select NOME_ORGAO_SUPERIOR from dw_convenios.dim_orgao_superior limit 0, 1000"
    lista_orgao_superior = pd.read_sql_query(consulta_filtro_orgao_superior, conexao)
    
    filtro_4 = st.sidebar.selectbox('Selecione um órgão superior', lista_orgao_superior)

    consulta_filtro_orgao_concedente = "select NOME_ORGAO_CONCEDENTE from dw_convenios.dim_orgao_concedente limit 0, 1000"
    lista_orgao_concedente = pd.read_sql_query(consulta_filtro_orgao_concedente, conexao)
    
    filtro_5 = st.sidebar.selectbox('Selecione um órgão concedente', lista_orgao_concedente)

    consulta_filtro_ug_concedente = "select NOME_UG_CONCEDENTE from dw_convenios.dim_ug_concedente limit 0, 1000"
    lista_ug_concedente = pd.read_sql_query(consulta_filtro_ug_concedente, conexao)
    
    filtro_6 = st.sidebar.selectbox('Selecione uma UG concedente', lista_ug_concedente)

    consulta_sql = "SELECT trimestre_nome, COUNT(*) as quantidade FROM dimdata inner join fatoconvenios as fc on keyData = k_Data INNER JOIN dim_municipio as dm on k_Municipio = sk_municipio INNER JOIN dim_orgao_superior as os on k_Orgao_Superior = sk_orgao_superior INNER JOIN dim_ug_concedente as ugc on k_UG_Concedente = sk_ug_concedente INNER JOIN dim_orgao_concedente as oc on k_Orgao_Concedente = sk_orgao_concedente and ano_id >= "+str(filtro_1)+" and ano_id <= "+str(filtro_2)
    
    consulta_sql += " and UF ="+"'"+str(filtro_3)+"'"

    if filtro_4 != None:
        consulta_sql += " and NOME_ORGAO_SUPERIOR ="+"'"+str(filtro_4)+"'"

    if filtro_5 != None:
       consulta_sql += " and NOME_ORGAO_CONCEDENTE ="+"'"+str(filtro_5)+"'"   
    
    if filtro_6 != None:
       consulta_sql += " and NOME_UG_CONCEDENTE ="+"'"+str(filtro_6)+"'"

    consulta_sql += " GROUP BY trimestre_nome"

    dados = pd.read_sql_query(consulta_sql, conexao)

    consulta_sql_2 = "SELECT dt.trimestre_nome, AVG(fc.VALOR_CONVENIO) as media_valores FROM dimdata as dt inner join fatoconvenios as fc on dt.keyData = fc.k_Data INNER JOIN dim_municipio as dm on fc.k_Municipio = dm.sk_municipio INNER JOIN dim_ug_concedente as ugc on fc.k_UG_Concedente = ugc.sk_ug_concedente INNER JOIN dim_orgao_superior as os on fc.k_Orgao_Superior = os.sk_orgao_superior INNER JOIN dim_orgao_concedente as oc on fc.k_Orgao_Concedente = oc.sk_orgao_concedente and dt.ano_id >= "+str(filtro_1)+" and dt.ano_id <= "+str(filtro_2)
    
    consulta_sql_2 += " and dm.UF ="+"'"+filtro_3+"'"

    if filtro_4 != None:
        consulta_sql_2 += " and os.NOME_ORGAO_SUPERIOR ="+"'"+filtro_4+"'"

    if filtro_5 != None:
        consulta_sql_2 += " and oc.NOME_ORGAO_CONCEDENTE ="+"'"+filtro_5+"'"

    if filtro_6 != None:
       consulta_sql_2 += " and ugc.NOME_UG_CONCEDENTE ="+"'"+filtro_6+"'"

    consulta_sql_2 += " GROUP BY trimestre_nome"

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
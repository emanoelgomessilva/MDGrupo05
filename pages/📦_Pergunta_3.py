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
    
    filtro_2 = st.sidebar.slider('Selecione o ano', min_value = 2013, max_value = 2023)

    consulta_sql = "SELECT dos.NOME_ORGAO_SUPERIOR, SUM(VALOR_CONVENIO) as valor_convenio FROM dim_orgao_superior as dos inner join fatoconvenios as fc on dos.sk_orgao_superior = fc.k_Orgao_Superior inner join dim_municipio as dm on dm.sk_municipio = fc.k_Municipio inner join dimdata as dt on dt.keyData = fc.k_Data and dm.sk_municipio = fc.k_Municipio and dm.UF ="+"'"+str(filtro_1)+"'"

    consulta_sql += " and dt.ano_nome ="+"'"+str(filtro_2)+"'"

    consulta_sql+= " GROUP BY doS.NOME_ORGAO_SUPERIOR ORDER BY valor_convenio DESC"
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

import streamlit as st
import pandas as pd
import main
import altair as alt

conexao = main.conexao

st.write('<h1>Pergunta 2</h1>', unsafe_allow_html=True)
st.write('''Qual órgão concedente foi mais beneficiado por estado e quanto foi direcionado para esse órgão?''', unsafe_allow_html=True)

def builder_body():
    Pergunta_2()

def Pergunta_2():

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

    consulta_sql = "SELECT doc.NOME_ORGAO_CONCEDENTE, COUNT(*) as quantidade_convenios FROM dim_orgao_concedente as doc inner join fatoconvenios as fc inner join dim_municipio as dm where doc.sk_orgao_concedente = fc.k_Orgao_Concedente and dm.sk_municipio = fc.k_Municipio and dm.UF ="+"'"+str(filtro_1)+"'"+ "GROUP BY doc.NOME_ORGAO_CONCEDENTE ORDER BY quantidade_convenios DESC LIMIT 5"
    dados = pd.read_sql_query(consulta_sql, conexao)

    consulta_sql_2 = "SELECT doc.NOME_ORGAO_CONCEDENTE, SUM(VALOR_CONVENIO) as valor_convenio FROM dim_orgao_concedente as doc inner join fatoconvenios as fc inner join dim_municipio as dm where doc.sk_orgao_concedente = fc.k_Orgao_Concedente and dm.sk_municipio = fc.k_Municipio and dm.UF ="+"'"+str(filtro_1)+"'"+ "GROUP BY doc.NOME_ORGAO_CONCEDENTE ORDER BY valor_convenio DESC LIMIT 5"
    dados_2 = pd.read_sql_query(consulta_sql_2, conexao)

    chart = alt.Chart(dados).mark_bar().encode(
        x='NOME_ORGAO_CONCEDENTE',
        y='quantidade_convenios',
        tooltip=['NOME_ORGAO_CONCEDENTE', 'quantidade_convenios']
    ).interactive()

    st.write('''Gráfico da quantidade de convênios por estado''', unsafe_allow_html=True)
    st.altair_chart(chart, use_container_width=True)

    chart_2 = alt.Chart(dados_2).mark_bar().encode(
        x='NOME_ORGAO_CONCEDENTE',
        y='valor_convenio',
        tooltip=['NOME_ORGAO_CONCEDENTE', 'valor_convenio']
    ).interactive()

    st.write('''Gráfico da valor em convênios por estado''', unsafe_allow_html=True)
    st.altair_chart(chart_2, use_container_width=True)
    
builder_body()
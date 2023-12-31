
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
    
    filtro_2 = st.sidebar.slider('Selecione o ano', min_value = 2008, max_value = 2023)



    consulta_sql = "SELECT doc.NOME_ORGAO_CONCEDENTE, COUNT(*) as quantidade_convenios FROM dim_orgao_concedente as doc inner join fatoconvenios as fc on doc.sk_orgao_concedente = fc.k_Orgao_Concedente inner join dim_municipio as dm on dm.sk_municipio = fc.k_Municipio inner join dimdata as dt on dt.keyData = fc.k_Data and dm.sk_municipio = fc.k_Municipio and dm.UF ="+"'"+str(filtro_1)+"'"

    consulta_sql += " and dt.ano_nome ="+"'"+str(filtro_2)+"'"

    consulta_sql+= " GROUP BY doc.NOME_ORGAO_CONCEDENTE ORDER BY quantidade_convenios DESC"

    dados = pd.read_sql_query(consulta_sql, conexao)

    consulta_sql_2 = "SELECT doc.NOME_ORGAO_CONCEDENTE, SUM(VALOR_CONVENIO) as valor_convenio FROM dim_orgao_concedente as doc inner join fatoconvenios as fc inner join dim_municipio as dm where doc.sk_orgao_concedente = fc.k_Orgao_Concedente and dm.sk_municipio = fc.k_Municipio and dm.UF ="+"'"+str(filtro_1)+"'"+ "GROUP BY doc.NOME_ORGAO_CONCEDENTE ORDER BY valor_convenio DESC"
    dados_2 = pd.read_sql_query(consulta_sql_2, conexao)

    chart = alt.Chart(dados).mark_bar().encode(
        x= alt.X('NOME_ORGAO_CONCEDENTE', title='Nome do órgão concedente'),
        y=alt.Y('quantidade_convenios', title='Quantidade de convênios'),
        tooltip=['NOME_ORGAO_CONCEDENTE', 'quantidade_convenios']
    ).interactive()

    st.write('''Gráfico da quantidade de convênios por estado''', unsafe_allow_html=True)
    st.altair_chart(chart, use_container_width=True)

    chart_2 = alt.Chart(dados_2).mark_bar().encode(
        x= alt.X('NOME_ORGAO_CONCEDENTE', title='Nome do órgão concedente'),
        y=alt.Y('valor_convenio', title='Valores em convênio'),
        tooltip=['NOME_ORGAO_CONCEDENTE', 'valor_convenio']
    ).interactive()

    st.write('''Gráfico da valor em convênios por estado''', unsafe_allow_html=True)
    st.altair_chart(chart_2, use_container_width=True)
    
builder_body()
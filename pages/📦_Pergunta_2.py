
import streamlit as st
import mysql.connector as cnt
import matplotlib.pyplot as plt
import pandas as pd

conexao = cnt.connect(
    host="localhost",
    user="root",
    password="root",
    database="dw_convenios"
)

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

    fig, ax = plt.subplots()
    bars = ax.bar(dados['NOME_ORGAO_CONCEDENTE'], dados['quantidade_convenios'])
    ax.set_xlabel('Órgão concedente')
    ax.set_ylabel('Quantidade de convênios')
    ax.set_title('Gráfico de Barras')

    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom')

    consulta_sql_2 = "SELECT doc.NOME_ORGAO_CONCEDENTE, SUM(VALOR_CONVENIO) as valor_convenio FROM dim_orgao_concedente as doc inner join fatoconvenios as fc inner join dim_municipio as dm where doc.sk_orgao_concedente = fc.k_Orgao_Concedente and dm.sk_municipio = fc.k_Municipio and dm.UF ="+"'"+str(filtro_1)+"'"+ "GROUP BY doc.NOME_ORGAO_CONCEDENTE ORDER BY valor_convenio DESC LIMIT 5"
    dados_2 = pd.read_sql_query(consulta_sql_2, conexao)

    fig_2, ax_2 = plt.subplots()
    bars_2 = ax_2.bar(dados_2['NOME_ORGAO_CONCEDENTE'], dados_2['valor_convenio'])
    ax_2.set_xlabel('Órgão concedente')
    ax_2.set_ylabel('Valor total em Convênios')
    ax_2.set_title('Gráfico de Barras')

    for bar in bars_2:
        yval = bar.get_height()
        ax_2.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom')

    st.write('''Gráfico da quantidade de convênios por estado''', unsafe_allow_html=True)
    st.pyplot(fig)
    st.table(dados)
    st.write('''Gráfico da valor total em convênios por estado''', unsafe_allow_html=True)
    st.pyplot(fig_2)
    st.table(dados_2)

        

builder_body()
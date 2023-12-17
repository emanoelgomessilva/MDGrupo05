import streamlit as st

# Ajuste da página geral
st.set_page_config(
    page_title = 'Projeto',
    page_icon = ':books:',
    layout = 'wide',
    menu_items= {
        'Get help': "https://streamlit.io",
        'Report a Bug': "https://blog.streamlit.io",
        'About': '''Este é um projeto estudantil feito por alunos da **UFRPE**.
        Acesse: bsi.ufrpe.br
        '''
        } # type: ignore
)

# Criação de um cabeçalho
st.markdown('''
# **Modelagem de dados: Convênios**

Este é um trabalho científico voltado à análise de dados, usando um <i>dataset</i> de convênios do governo federal.

O projeto se concentra na construção de um Data wharehouse a partir dos dados disponíveis.            

**Membros do Projeto:**
- `Aurineque`
- `Emanoel` (emanoel20092009@gmail.com)
- `Guilherme`
- `Júlia`
- `Pedro`
            
**Fonte**:
- [Convênios](https://portaldatransparencia.gov.br/download-de-dados/convenios)
---
''', unsafe_allow_html=True)
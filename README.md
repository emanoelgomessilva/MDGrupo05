# MD_GRUPO_05
Este é um trabalho científico voltado à análise de dados, usando um <i>dataset</i> de convênios do governo federal.

O projeto se concentra na construção de um Data wharehouse a partir dos dados disponíveis.  

## Instalação
<ol>
  <li>Instale o VSCode.</li>

  <li>Efetue o clone do projeto: <code>CTRL+SHIFT+P > Git:Clone > Clone from GitHub > https://github.com/emanoelgomessilva/MDGrupo05.git</code></li>

  <li>Instale o python.</li>
  
  <li>Acesse a aba "Terminal" disponível na parte inferior do VSCode.</li>

  <li>Atualize o pip:<br>
    <code>python -m pip install --upgrade pip</code>
  </li>

  <li>Instale as libs necessárias para o projeto:<br>
    <code>pip install -r requirements.txt --upgrade</code>
  </li>

  <li>Altere as credenciais de conexão com o banco de dados<br>
    No arquivo main.py, substitua as informações de conexão com o banco de dados por suas informações locais. As informações 
    a serem substiruídas estarão na linha de 18 do arquivo como no exemplo abaixo:
    <code>
    conexao = cnt.connect(
            host="localhost",
            user="root",
            password="root",
            database="dw_convenios"
          )
    </code>
  </li>

  <li>Rode o sistema:<br>
    <code>streamlit run main.py</code>
  </li>
</ol>

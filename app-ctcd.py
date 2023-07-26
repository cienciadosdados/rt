import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st

# URL do Google Sheets
sheet_url = 'https://docs.google.com/spreadsheets/d/1IZO_ycLDBfjE-xw78AY7BRp5iEQsLIMQzid6F9KMSx0/edit?usp=sharing'

# Substitui /edit?usp=sharing por /export?format=csv na URL
csv_export_url = sheet_url.replace('/edit?usp=sharing', '/export?format=csv')

# Lê o arquivo csv
df = pd.read_csv(csv_export_url)

# Calcula o valor de criticidade como a média dos outros quatro indicadores para cada ação.
df['Criticidade'] = df[['impacto', 'urgência', 'Probabilidade ', 'Gravidade']].mean(axis=1)

# Ordena as ações pela criticidade em ordem decrescente.
df = df.sort_values('Criticidade', ascending=False)

# Define a escala de cores
colorscale = 'Viridis'  # Outras opções: 'Plasma', 'Magma', 'Inferno', 'Cividis', etc.

# Cria o gráfico de barras com Plotly
fig = go.Figure(data=[go.Bar(x=df['Criticidade'], y=df['acao'],
                            hovertext=df['Recomendação'], marker=dict(color=df['Criticidade'], colorscale=colorscale),
                            textposition='outside', hoverlabel=dict(bgcolor='white', font_size=12))])

fig.update_layout(title='Criticidade das Recomendações',
                  xaxis_title='Criticidade', yaxis_title='Ação',
                  yaxis={'categoryorder': 'total descending'})

# Configurações do Streamlit
st.title('Painel de Criticidade das Ações de Ciência de Dados')
st.plotly_chart(fig)


################

import pandas as pd
import streamlit as st

# URL do Google Sheets
sheet_url = 'https://docs.google.com/spreadsheets/d/1IZO_ycLDBfjE-xw78AY7BRp5iEQsLIMQzid6F9KMSx0/edit?usp=sharing'

# Substitui /edit?usp=sharing por /export?format=csv na URL
csv_export_url = sheet_url.replace('/edit?usp=sharing', '/export?format=csv')

# Lê o arquivo csv
df = pd.read_csv(csv_export_url)

# Função para exibir os dados da ação selecionada
def exibir_dados_acao(acao):
    dados_acao = df[df['acao'] == acao]
    st.table(dados_acao)

# Dropdown para selecionar a ação
acoes = df['acao'].unique()
acao_selecionada = st.selectbox('Detalhamento da recomendação', acoes)

# Verifica se uma ação foi selecionada e exibe os dados correspondentes
if acao_selecionada:
    exibir_dados_acao(acao_selecionada)


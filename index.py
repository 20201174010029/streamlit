#importar Bibliotecas
import streamlit as st
import pandas as pd
import yfinance as yf
#Criar as funções de carregamento de dados
 #cotacões 
@st.cache_data
def carregar_dados(empresa):
    dados_acao = yf.Ticker(empresa)
    cotacoes_acao = dados_acao.history(period="1d", start = "2020-01-01", end = "2024-08-01")
    cotacoes_acao = cotacoes_acao[['Close']]
    return cotacoes_acao
dados = carregar_dados("PETR4.SA")
#criação a interface do streamlit
st.write("# Preço das acões") #markdown
st.write("o gráfico abaixo mostra a evolução do preço das acões da petrobras ao longo do tempo.")
st.line_chart(dados)
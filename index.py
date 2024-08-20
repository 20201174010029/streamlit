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
    return cotacoes_acao
dados = carregar_dados("PETR4.SA")
print(dados)
#criação a interface do streamlit
st.write("# hello word!") #markdown
st.write("seja bem-vindo")
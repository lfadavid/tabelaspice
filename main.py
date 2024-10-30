import streamlit as st
import pandas as pd
import numpy as np
from model import TabelaSpice

st.set_page_config(
                    page_title="Calculadora de Frete",
                    layout="wide", 
                    page_icon="cotralti_logo.png",
                    #initial_sidebar_state="collapsed" # inicia com barra de filtros fechada
)

#Cabeçalhos do sistemas
st.header("Calculadora de Frete ###", divider='gray',)

#Sidebar e seus comandos
with st.sidebar:
    st.sidebar.image("cotralti_logo.png",width=80)
    st.sidebar.markdown("""
                    #### Desenvolvido  por http://cotralti.com.br
                    """)
    st.write("""
              ###### &copy; 2024 - Luis Felipe A. David - Todos os direitos reservados
         """)
    st.text("Fonte: Tabela Spice.")

#Banco de dados com os valores usando lista ao inves de planilha tiramdo da model

df  =pd.DataFrame(TabelaSpice)

#Inserindo as colunas na tela
coluna_esquerda , coluna_meio , coluna_direita = st.columns([1, 1, 1])

peso_digitado = coluna_esquerda.number_input(label="Digite o peso em Kg", min_value=0.0, placeholder="Digite o valor do peso", value=None)

rota_digitada = coluna_meio.selectbox(
                        key=1,
                        label="Código",
                        options=df["Código"].unique(),
                        placeholder="Selecione a rota desejada",
                        index=None
)

faixa_peso_digitado = coluna_direita.selectbox(
                        key=2,
                        label="Faixa de Peso",
                        options=df.columns[6:11].to_list(),
                        placeholder="Selecione a faixa de peso",
                        index=None
)

#filtrando pelo codigo

df_filtro = df[df["Código"] == rota_digitada]

#INSERIR CALCULOS DO SISTEMA
if st.button("Calcular"): 
   if faixa_peso_digitado in df_filtro.columns:
      frete = df_filtro[faixa_peso_digitado].values[0]
      taxaNF = df_filtro['Taxa_NFE'].values[0]
      adv = df_filtro['ADV(%)'].values[0]
      frete_rota = ((frete / 1000) * peso_digitado)
     
      
      
      st.divider()
      
      st.success("Conseguimos Calcular  os seus dados :)")
      coluna_esquerda , coluna_meio , coluna_direita = st.columns([1, 1, 1])  
      
      
      coluna_meio.metric(f"A Rota selecionada é ", rota_digitada)
      coluna_direita.metric("A Faixa de Peso é .", faixa_peso_digitado)
      coluna_esquerda.metric("O valor do Frete Rota é ",f'R$ {frete_rota:,.2F}')
     
      coluna_esquerda , coluna_meio , coluna_direita = st.columns([1, 1, 1])  

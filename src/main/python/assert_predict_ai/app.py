import pandas as pd
import streamlit as st
from prophet import Prophet


def main():

    st.title("Bem-vindo ao AssetPredict IA")

    st.caption('''
    O AssetPredict IA é uma aplicação web desenvolvida com Python e Streamlit, 
    voltada para análise e previsão de ativos no mercado financeiro. O objetivo do projeto é 
    fornecer aos investidores uma ferramenta intuitiva e objetiva para avaliar ativos e realizar 
    previsões baseadas em modelos matemáticos.
    ''')

    st.subheader('Insira o número de dias para gerar a previsão:')
    days = st.number_input('', min_value=1, value=1, step=1)

if __name__ == "__main__":
    main()
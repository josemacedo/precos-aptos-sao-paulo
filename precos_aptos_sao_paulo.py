import pandas as pd
import random
import re
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import joblib

# Setando o estilo do seaborn
sns.set_style('darkgrid')

# ELIMINANDO O MENU SREAMLIT
hide_style = '''
             <style>
             #MainMenu {visibility: hidden;}
             footer {visibility: hidden;}
             </style>
             '''
st.markdown(hide_style, unsafe_allow_html=True)

# FUNCOES GERAIS CRIADAS
def titulo_centro(texto):
    html = "<h2 style='text-align: center;'><b>{}</b></h2>".format(texto)
    st.markdown(html, unsafe_allow_html=True)
    
def texto_destaque(texto):
    html = "<h3 style='text-align: center;'>{}</h3>".format(texto)
    st.markdown(html, unsafe_allow_html=True)
    
def texto_centro(texto):
    html = "<p style='text-align: center;'>{}</p>".format(texto)
    st.markdown(html, unsafe_allow_html=True)
    
# INICIO DO APP -------------------------

# Titulo da pagina
titulo_centro('WEB APP ─ APES SP')
texto_destaque('- - - - -')

# CARREGANDO OS ARQUIVOS -------------------------

# Dataset dos apes
data = pd.read_csv('precos_aptos_sao_paulo_prod.csv')

# COLETANDO AS INFORMACOES -------------------------

# Nome do bairro
bairros_nomes = list(data['bairros'].unique())
bairros_nomes = sorted(bairros_nomes)
bairro = st.sidebar.multiselect('Bairro/Bairros',
                                bairros_nomes,
                                'alto da lapa')

# Metragem (m2)
metros = st.sidebar.number_input('Metragem (m2)',
                                 value = 50,
                                 min_value = 12,
                                 max_value = 600)

# Total de quartos
quartos = st.sidebar.number_input('Total de quartos',
                                  value = 2,
                                  min_value = 1,
                                  max_value = 8)

# Total de banheiros
banheiros = st.sidebar.number_input('Total de banheiros',
                                    value = 1,
                                    min_value = 1,
                                    max_value = 8)

# Total de suites
suites = st.sidebar.number_input('Total de suites',
                                 value = 0,
                                 min_value = 0,
                                 max_value = 5)

# Vagas para carros
vagas = st.sidebar.number_input('Total de vagas',
                                value = 1,
                                min_value = 0,
                                max_value = 10)

# O USUARIO PREENCHE INFORMACOES -------------------------

if len(bairro) != 1:
    texto_destaque('< Escolha um bairro!')
    
else:
    # Bairro encodado
    # Carregando o modelo
    encode = joblib.load('encode_bairros.pkl')
    bairro_encode = encode.transform(bairro)

    # Comodos totais e igual
    comodos = quartos + banheiros + suites


    # PROCESSANDO A PREDICAO -------------------------
    model = joblib.load('modelo.pkl')
    
    predicao = int(model.predict([[bairro_encode,
                                   metros,
                                   vagas,
                                   comodos]])*1000)
    predicao = re.sub("(\d)(?=(\d{3})+(?!\d))",
                      r"\1.", "%d" % predicao)

    texto_destaque('O valor do imovel dos seus sonhos é:')
    texto_destaque('R$ {}'.format(predicao))
    texto_destaque('- - - - -')

    # PROCESSANDO AS INFORMACOES -------------------------
    
    # CONSTRUCAO DO GRAFICO
    bairro_escolhido = bairro[0]
    texto_destaque('Outros imoveis em {} - MR$'
                   .format(bairro_escolhido.capitalize()))
    
    # Filtrando o bairro escolhido
    data_bairro = data[data['bairros'] == bairro_escolhido]
    
    fig, ax = plt.subplots()
    sns.kdeplot(data_bairro['PRECO_MILHARES'],
                shade = True,
                gridsize = 100,
                hue = data_bairro['quartos'])
    plt.xlabel('')
    plt.xlim(int(data_bairro['PRECO_MILHARES'].min()),
             int(data_bairro['PRECO_MILHARES'].max()))
    plt.ylabel('')
    plt.yticks([])
    st.pyplot(fig)
    
    # Rodape
    texto_destaque('- - - - -')
    texto_centro('por felipe.amadorbueno@gmail.com')
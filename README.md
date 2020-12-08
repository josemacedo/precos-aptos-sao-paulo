### A - Objetivos do projeto

1.   Reunir dados do mercado imobiliario de Sao Paulo
2.   Descobrir caracteristicas que interferem no preco
3.   Criar um modelo para prever valores de apartamentos
4.   [Desenvolver um um web app usando o modelo salvo](https://precos-aptos-sao-paulo.herokuapp.com/)

### B - Arquivos nesse projeto

*   **ccd.py** - Aplicativo web desenvolvido em streamlit
*   **encode_bairros.pkl** - Encoder para os nomes dos bairros
*   **model.pkl** - Modelo treinado salvo para predicao
*   **precos_apes_em_sao_paulo.csv** - DS pronto - base de dados
*   **precos_aptos_sao_paulo_prod.csv** - DS final - producao
*   **precos_aptos_sao_paulo.ipynb** - Desenvolvimento do projeto
*   **Procfile** - Instrucao para execucao (Heroku cloud)
*   **README.md** - Descricao e notas gerais do projeto 
*   **requirements.txt** - Pacotes necessarios (Heroku cloud)
*   **setup.sh** - Configuracao do ambiente (Heroku cloud)

### C - Sobre o dataset .csv

1.   Fiz um scrape em varios sites de imobiliárias e anuncios 
2.   Colhi variados bairros, nº de comodos e um bom range de precos
3.   Com regex bati as infos dos campos com a descricao do imovel
4.   Tratei os csv's, eliminei discrepancias e juntei num só arquivo
5.   Eliminei o link do anuncio, e colunas que tinham a fonte (sites)

### D - Topicos para o futuro

1.   Parameter tuning mais sofisticado. Bayesian Optimization?
2.   Melhorar substancialmente os resultados do modelo
3.   Coletar mais dados, principalmente apartamentos de luxo
4.   Tipificar imoveis (padrao, flat, luxo) e testar no modelo
5.   Agregar informacoes novas, ex.: criminalidade dos bairros

### E - Consideracoes finais

*   Mais informacoes, consulte: **[precos_aptos_sao_paulo.ipynb](https://github.com/felipecabueno/precos-aptos-sao-paulo/blob/main/precos_aptos_sao_paulo.ipynb)**
*   **[Parte 1 do artigo do projeto - LinkedIn](https://www.linkedin.com/pulse/dataset-pre%C3%A7o-de-apartamentos-em-s%C3%A3o-paulo-2020-felipe-bueno/?published=t)**

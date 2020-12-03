### A - Objetivos do projeto

1.   Reunir dados do mercado imobiliario de **Sao Paulo**
2.   Descobrir caracteristicas que interferem no preco
3.   Criar um modelo para prever valores de apartamentos
4.   Desenvolver um um web app usando o modelo salvo

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

### D - Topicos para o futuro

1.   Parameter tuning mais sofisticado. Bayesian Optimization?
2.   Melhorar substancialmente os resultados do modelo
3.   Coletar mais dados, principalmente apartamentos de luxo
4.   Tipificar imoveis (padrao, flat, luxo) e testar no modelo
5.   Reescrever o codigo do app e organizar o repo do projeto

### E - Consideracoes finais

*   Mais informacoes, consulte: **precos_aptos_sao_paulo.ipynb**
*   Meus contatos e redes sociais: **[link](https://www.felipebueno.site)**

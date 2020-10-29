# Projeto Bom Pagador  

Este projeto foi apresentado ao Instituto de Educação Continuada (IEC) da PUCMinas, 
na disciplina de Projeto Integrado - Construção de Aplicação de Big Data e Analytics - 
para o curso de na Especialização em Ciência de Dados e Big Data.  

## O Bom Pagador  

O projeto é uma API a ser utilizada como apoio a análise de perfil de pagamento de clientes. 
Baseada em algoritmos de Machine Learning, a api faz classificação no sentido de sinalizar se o cliente pode ter sua solicitação de crédito aprovada ou não.  

O planejamento deste projeto teve como base as praticas do **Lean Inception** - Caroli(2018).

1. Base de Dados 

    Para treinar e validar o modelo foi utilizado a base de dados do Credit Risk que está disponível no [Kaggle](https://www.kaggle.com/laotse/credit-risk-dataset). 
    
    
2. Instalando bibliotecas  
    
    Para executar o código é necessário instalar algumas bibliotecas. Execute estes comandos utilizando o pip.
    ```
    pip install streamlit
    pip install pandas
    pip install numpy 
    pip install sklearn 
    ```

3. Executando o projeto 

    Execute o código a seguir via terminal de comando.
``` 
    streamlit run app.py 
```


from tkinter import *
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# executar esse arquivo ao selecionar a opção 3, com as acoes do cliente informado
def analisar_carteira(lista_acoes: list):
    # Definir o período de data desejado
    start_date = "2020-01-01"
    end_date = "2023-01-01"

    if len(lista_acoes) == 0:
        return
    
    # Criar um DataFrame vazio
    df = pd.DataFrame()

    # Baixar os dados para cada ação e adicionar ao DataFrame
    for i in lista_acoes:
        cotacao = yf.download(i, start=start_date, end=end_date)
        df[i] = cotacao['Adj Close']

    # Plotar as séries de preços do DataFrame
    df.plot(figsize=(15, 10))

    plt.xlabel('Anos')
    plt.ylabel('Valor Ticket')
    plt.title('Variação de valor das ações')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    analisar_carteira(['ABEV3.SA'])
    
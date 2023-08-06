import yfinance as yf
from utils.funcoes_auxiliares import join_tuple_string

# executar esse arquivo ao selecionar a opção 4
def obter_dados_acao(lista, nome_arquivo):
    try:
        acoes_string = map(join_tuple_string, lista)
        lista_acoes = list(acoes_string)

        
        for ticker in lista_acoes:
            # Obter os dados da ação usando o Yahoo Finance (B3)
            acao = yf.download(ticker, progress=False)

            # Exibir os dados
            with open(nome_arquivo, 'a+') as arquivo:
                arquivo.write("Relatorio da acao: " + ticker + "\n")
                arquivo.write(str(acao.tail()))
                arquivo.write("\n\n")

        print(f"Relatório exportado com sucesso para o arquivo '{nome_arquivo}'.")

    except Exception as e:
        print("Erro ao obter dados da ação. Verifique o código da ação e tente novamente.")
        print(f"Detalhes do erro: {e}")

if __name__ == "__main__":
    # Solicitar ao usuário o código da ação e o nome do arquivo
    ticker = input("Digite o código da ação na B3 (ex: PETR4): ").strip().upper()
    nome_arquivo = input("Digite o nome do arquivo de saída (ex: relatorio_acao.txt): ").strip()

    # Obter e mostrar os dados da ação e exportar para o arquivo
    obter_dados_acao(ticker, nome_arquivo)



# Open: Representa o preço de abertura da ação no período em questão. É o preço pelo qual a primeira transação da ação foi realizada no início do período.

# High: Indica o preço mais alto (valor máximo) que a ação alcançou durante o período de tempo específico.

# Low: Representa o preço mais baixo (valor mínimo) que a ação atingiu durante o período de tempo em questão.

# Close: Refere-se ao preço de fechamento da ação no final do período em questão. É o preço pelo qual a última transação da ação foi realizada no final do período.

# Adj Close: É o preço de fechamento ajustado (adjusted close). Ele leva em consideração dividendos, desdobramentos de ações e outras ações corporativas que possam afetar o preço da ação. É o valor mais preciso para análises de longo prazo, pois reflete o valor real da ação após ajustes.
    # Adj Close (Preço de Fechamento Ajustado):
    # O preço de fechamento ajustado (Adj Close) é o preço de fechamento que foi ajustado para considerar eventos corporativos que podem afetar o preço da ação. Esses eventos incluem:
    # Dividendos: Quando uma empresa distribui dividendos aos acionistas, o preço da ação normalmente cai após o ex-dividendo. O preço de fechamento ajustado leva em conta essa redução no valor da ação após o pagamento do dividendo.

# Volume: É a quantidade total de ações negociadas durante o período de tempo especificado. Representa o número de ações que mudaram de mãos entre compradores e vendedores durante o período.
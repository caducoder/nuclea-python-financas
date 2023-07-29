from datetime import datetime
import re

def printa_menu():
    print("1 - Cadastrar cliente")
    print("2 - Cadastrar ação")
    print("3 - Realizar análise da carteira")
    print("4 - Imprimir relatório da carteira")
    print("5 - Sair")

    return int(input("Digite a opção desejada: "))


def formatar_texto(texto: str):
    return texto.title()
    

def validar_rg():
    padrao_rg = r'^\d{1,2}\.\d{3}\.\d{3}-[0-9A-Za-z]{1}$'
    while True:
        rg = input("RG: ")
        eh_valido = re.match(padrao_rg,rg)
        if eh_valido == None:
            print('RG inválido')
        else:
            return rg
        

def validar_data():
    while True:
        data_nasc = input("Data de Nascimento: ")
        try:
            data_covertida = datetime.strptime(data_nasc, "%d/%m/%Y").date()

            data_atual = datetime.now().date()

            if data_covertida < data_atual:
                return data_covertida.strftime("%d/%m/%Y")
            else:
                print("Data de nascimento dever ser anterior a data de hoje")
        except ValueError as e:
            print("Data Inválida")

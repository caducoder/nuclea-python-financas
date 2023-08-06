from datetime import datetime
import re

def printa_menu():
    print("1 - Cliente")
    print("2 - Cadastrar ordem")
    print("3 - Realizar análise da carteira")
    print("4 - Imprimir relatório")
    print("5 - Sair")

    return input("Digite a opção desejada: ")


def printa_menu_cliente():
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Atualizar")
    print("4 - Remover")

    return input("Digite a opção desejada: ")

def formatar_texto(texto: str):
    return texto.title()
    

def validar_rg(prompt: str):
    padrao_rg = r'^\d{1,2}\.\d{3}\.\d{3}-[0-9A-Za-z]{1}$'
    while True:
        rg = input(prompt)
        eh_valido = re.match(padrao_rg,rg)
        if eh_valido == None:
            print('RG inválido')
        else:
            return rg
        

def validar_data(prompt: str):
    while True:
        data_nasc = input(prompt)
        try:
            data_covertida = datetime.strptime(data_nasc, "%d/%m/%Y").date()

            data_atual = datetime.now().date()

            if data_covertida < data_atual:
                return data_covertida.strftime("%Y-%m-%d")
            else:
                print("Data de nascimento dever ser anterior a data de hoje")
        except ValueError as e:
            print("Data Inválida")


def join_tuple_string(strings_tuple) -> str:
   string_ordem = ''.join(strings_tuple)
   return string_ordem + '.SA'
import requests
import re

def valida_cep():
    padrao_cep = r'^\d{8}'
    while True:
        # verificar se tem traço
        cep = input("CEP: ")
        if re.match(padrao_cep, cep) == None:
            print('CEP inválido')
        else:
            try:
                return busca_cep(cep)
            except Exception as e:
                print("CEP não encontrado. Tente novamente")


def busca_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    resJson = response.json()

    # buscar as informações e devolver um dicionário com cep, 
    # logradouro, complemento e localidade
    endereco = {
        "CEP": resJson["cep"],
        "Logradouro": resJson["logradouro"],
        "Bairro": resJson["bairro"],
        "Cidade": resJson["localidade"],
        "Estado": resJson["uf"],
        "Complemento": resJson["complemento"]
    }

    return endereco
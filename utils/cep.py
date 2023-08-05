import requests
import re

def valida_cep(prompt: str):
    padrao_cep = r'^\d{8}'
    while True:
        # verificar se tem traço
        cep = input(prompt)
        cep = cep.replace('-', '')
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

    endereco = {
        "cep": resJson["cep"],
        "logradouro": resJson["logradouro"],
        "bairro": resJson["bairro"],
        "cidade": resJson["localidade"],
        "estado": resJson["uf"],
        "complemento": 'N/A' if resJson["complemento"] == "" else resJson["complemento"]
    }

    return endereco

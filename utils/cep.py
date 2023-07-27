import requests
import re

def busca_cep():
    padrao_cep = r'^\d{8}'
    while True:
        cep = input("CEP: ")
        if re.match(padrao_cep, cep) == None:
            print('CEP inválido')
        else:
            try:
                url = f"https://viacep.com.br/ws/{cep}/json/"
                response = requests.get(url)
                resJson = response.json()

                # buscar as informações e devolver um dicionário com cep, 
                # logradouro, complemento e localidade
                endereco = {
                    "cep": resJson["cep"],
                    "logradouro": resJson["logradouro"],
                    "complemento": resJson["complemento"],
                    "localidade": resJson["localidade"]
                }

                return endereco
            except Exception as e:
                print("CEP não encontrado. Tente novamente")

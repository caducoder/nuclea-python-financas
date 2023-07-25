from utils.funcoes_auxiliares import *

print("Seja bem vindo(a) ao sistema de gerenciamento de carteira de ações da Nuclea. Selecione uma das opções:")
clientes = []

resp = 'sim'

while resp != 'nao':
    escolha = printa_menu()

    if escolha == 1:
        cliente = {
            "nome": formatar_texto(input("Nome: ")),
            "cpf": validar_cpf(),
            "rg": input("RG: "),
            "data_nasc": input("Data de Nascimento: "),
            "cep": input("CEP: "),
            "num_casa": input("Número casa: ")
        }
        
        clientes.append(cliente)
        print(clientes)
    elif escolha == 2:
        print("Apenas opção 1 implementada! Por favor, ecolha outra opção.")
    elif escolha == 3:
        pass
    elif escolha == 4:
        pass
    elif escolha == 5:
        pass
    else:
        print("Opção inválida")
    
    resp = input("Deseja retornar ao menu principal? ")

from utils.funcoes_auxiliares import *
from utils.cep import valida_cep
from utils.cpf import validar_cpf

print("Seja bem vindo(a) ao sistema de gerenciamento de carteira de ações da Nuclea. Selecione uma das opções:")
clientes = []



def main():
    resp = 'sim'
    while resp != 'nao':
        escolha = printa_menu()

        if escolha == 1:
            cliente = {
                "nome": formatar_texto(input("Nome: ")),
                "cpf": validar_cpf(),
                "rg": validar_rg(),
                "data_nasc": validar_data(),
                "endereco": valida_cep(),
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

if __name__ == "__main__":
    main()
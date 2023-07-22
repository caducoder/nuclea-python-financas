print("Seja bem vindo(a) ao sistema de gerenciamento de carteira de ações da Nuclea. Selecione uma das opções:")
clientes = []

def printa_menu():
    print("1 - Cadastrar cliente")
    print("2 - Cadastrar ação")
    print("3 - Realizar análise da carteira")
    print("4 - Imprimir relatório da carteira")
    print("5 - Sair")

    return int(input("Digite a opção desejada: "))

resp = 'sim'

while resp != 'nao':
    escolha = printa_menu()

    if escolha == 1:
        nome = input("Nome: ")
        cpf = input("CPF: ")
        rg = input("RG: ")
        data_nasc = input("Data de Nascimento: ")
        cep = input("CEP: ")
        num_casa = input("Número casa: ")

        clientes.append(dict(nome=nome, cpf=cpf, rg=rg, data_nasc=data_nasc, cep=cep, num_casa=num_casa))
        print(clientes)
    else:
        print("Apenas opção 1 implementada! Por favor, ecolha outra opção.")
    resp = input("Deseja retornar ao menu principal? ")

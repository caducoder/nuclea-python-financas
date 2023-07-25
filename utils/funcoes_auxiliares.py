from validate_docbr import CPF

def printa_menu():
    print("1 - Cadastrar cliente")
    print("2 - Cadastrar ação")
    print("3 - Realizar análise da carteira")
    print("4 - Imprimir relatório da carteira")
    print("5 - Sair")

    return int(input("Digite a opção desejada: "))


def formatar_texto(texto: str):
    return texto.title()


def validar_cpf():
    cpf_valido = CPF(repeated_digits=True)
    while True:
        cpf = input("CPF: ")
        eh_valido = cpf_valido.validate(cpf)
        if not eh_valido:
            print('CPF inválido')
        else:
            if cpf.find('.'):
                return cpf # já formatado
            return cpf_valido.mask(cpf)
    
    
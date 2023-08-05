from validate_docbr import CPF

def gerar_cpf():
    cpf = CPF()
    return cpf.generate()

def validar_cpf(prompt: str):
    cpf_valido = CPF(repeated_digits=True)
    while True:
        cpf = input(prompt)
        eh_valido = cpf_valido.validate(cpf)
        if not eh_valido:
            print('CPF inválido')
        else:
            if cpf.find('.') != -1:
                return cpf # já formatado
            return cpf_valido.mask(cpf)
        


from model.Cliente import Cliente
from model.Ordem import Ordem
from utils.funcoes_auxiliares import *
from utils.cep import valida_cep
from utils.cpf import validar_cpf
from repository.banco_de_dados import BancoDeDados

print("Seja bem vindo(a) ao sistema de gerenciamento de carteira de ações da Nuclea. Selecione uma das opções:")

banco_de_dados = BancoDeDados()

def main():
    resp = 'sim'
    while resp != 'nao':
        escolha = printa_menu()

        if escolha == 1:
            escolha_cliente = printa_menu_cliente()

            if escolha_cliente == 1:
                cliente = Cliente()
                
                cliente.set_nome(formatar_texto(input("Nome: ")))
                cliente.set_cpf(validar_cpf("CPF: "))
                cliente.set_rg(validar_rg("RG: "))
                cliente.set_data_nasc(validar_data("Data de nascimento: "))
                cliente.set_endereco(valida_cep())
                cliente.set_num_casa(input("Número casa: "))

                banco_de_dados.adicionar_cliente(cliente)
            elif escolha_cliente == 2:
                banco_de_dados.listar_clientes()
            elif escolha_cliente == 3:
                cpf = input("Digite o cpf do cliente: ")
                cliente_banco = banco_de_dados.buscar_cliente_por_cpf(cpf)

                cliente_atualizado = Cliente()
                cliente_atualizado.set_id(cliente_banco[0])
                print("|--Repita os dados caso não queira alterar")
                novo_nome = input(f"Nome ({cliente_banco[1]}): ")
                cliente_atualizado.set_nome(novo_nome)
                novo_cpf = validar_cpf(f"CPF ({cliente_banco[2]}): ")
                cliente_atualizado.set_cpf(novo_cpf)
                novo_rg = validar_rg(f"RG ({cliente_banco[3]}): ")
                cliente_atualizado.set_rg(novo_rg)
                nova_dn = validar_data(f"Data de nascimento ({cliente_banco[4]}): ")
                cliente_atualizado.set_data_nasc(nova_dn)
                novo_endereco = valida_cep(f"CEP ({cliente_banco[5]}): ")
                cliente_atualizado.set_endereco(novo_endereco)
                novo_num_casa = input(f"Número casa ({cliente_banco[6]}): ")
                cliente_atualizado.set_num_casa(novo_num_casa)
                
                banco_de_dados.atualizar_cliente(cliente_atualizado)
            elif escolha_cliente == 4:
                banco_de_dados.remover_cliente(int(input("Id do cliente: ")))
            else:
                print("Opção inválida")
                continue
        elif escolha == 2:
            ordem = Ordem()
            ordem.set_nome(input("Nome da ordem: "))
            ordem.set_ticket(input("Ticket da ordem: "))
            ordem.set_valor_compra(input("Valor da compra: "))
            ordem.set_quantidade_compra(input("Quantidade: "))
            ordem.set_data_compra(validar_data("Data da compra: "))
            ordem.set_cliente_id(input("Id do cliente: "))

            banco_de_dados.adicionar_ordem(ordem)
        elif escolha == 3:
            pass
        elif escolha == 4:
            pass
        elif escolha == 5:
            print("Saindo...")
            exit()
        else:
            print("Opção inválida")
            continue
        
        resp = input("Deseja retornar ao menu principal? ")


if __name__ == "__main__":
    main()
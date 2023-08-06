from utils.funcoes_auxiliares import *
from utils.cep import valida_cep
from utils.cpf import validar_cpf
from model.Cliente import Cliente
from model.Ordem import Ordem
from repository.banco_de_dados import BancoDeDados
from carteira import analisar_carteira
from relatorio import obter_dados_acao
from prettytable import PrettyTable


print("Seja bem vindo(a) ao sistema de gerenciamento de carteira de ações da Nuclea. Selecione uma das opções:")

banco_de_dados = BancoDeDados()

table_format = PrettyTable()

def main():
    resp = 'S'
    while resp.upper() != 'N':
        escolha = printa_menu()

        if escolha == '1':
            escolha_cliente = printa_menu_cliente()

            if escolha_cliente == '1':
                cliente = Cliente()
                
                cliente.set_nome(formatar_texto(input("Nome: ")))
                cliente.set_cpf(validar_cpf("CPF: "))
                cliente.set_rg(validar_rg("RG: "))
                cliente.set_data_nasc(validar_data("Data de nascimento: "))
                cliente.set_endereco(valida_cep("CEP: "))
                cliente.set_num_casa(input("Número casa: "))

                banco_de_dados.adicionar_cliente(cliente)
            elif escolha_cliente == '2':
                lista_clientes = banco_de_dados.listar_clientes()
                table_format.field_names = ["Id", "Nome", "CPF", "RG",  "Dt. Nascimento", "CEP", "Numero", "Rua", "Compl.", "Bairro", "Cidade", "UF"]
                table_format.add_rows(lista_clientes)
                table_format.del_column('Id')
                print(table_format)
                print("(Expanda o terminal, caso fique cortado)")
            elif escolha_cliente == '3':
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
            elif escolha_cliente == '4':
                banco_de_dados.remover_cliente(int(input("Id do cliente: ")))
            else:
                print("Opção inválida")
                continue
        elif escolha == '2':
            ordem = Ordem()
            ordem.set_nome(input("Nome da ordem: "))
            ordem.set_ticket(input("Ticket da ordem: "))
            ordem.set_valor_compra(input("Valor da compra: "))
            ordem.set_quantidade_compra(input("Quantidade: "))
            ordem.set_data_compra(validar_data("Data da compra: "))
            ordem.set_cliente_id(input("Id do cliente: "))

            banco_de_dados.adicionar_ordem(ordem)
        elif escolha == '3':
            cpf = validar_cpf("CPF do cliente: ")
            acoes = banco_de_dados.buscar_acoes_por_cpf_cliente(cpf)
            if acoes == [(None,)]:
                print("O cliente informado não tem ações cadastradas.")
            else:
                acoes_string = map(join_tuple_string, acoes)
                lista_acoes = list(acoes_string)
                print("Lista: ", lista_acoes)
                analisar_carteira(lista_acoes)
            
        elif escolha == '4':
            print("1 - Carteira do cliente")
            print("2 - Consultar ação")
            op = input("Digite a opção desejada: ")

            if op == '1':
                cpf = validar_cpf("CPF do cliente: ")
                acoes = banco_de_dados.buscar_acoes_por_cpf_cliente(cpf)
                if acoes == [(None,)]:
                    print("O cliente informado não tem ações cadastradas.")
                else:
                    nome_arquivo = input("Digite o nome do arquivo de saída (ex: relatorio_acao.txt): ").strip()
                    obter_dados_acao(acoes, nome_arquivo)
            elif op == '2':
                ticker = input("Digite o código da ação na B3 (ex: PETR4): ").strip().upper()
                nome_arquivo = input("Digite o nome do arquivo de saída (ex: relatorio_acao.txt): ").strip()
                obter_dados_acao([ticker], nome_arquivo)
            else:
                print("Opção inválida")
        elif escolha == '5':
            print("Saindo...")
            exit()
        else:
            print("Opção inválida")
            continue
        
        resp = input("Deseja retornar ao menu principal (s/n)? ")


if __name__ == "__main__":
    main()
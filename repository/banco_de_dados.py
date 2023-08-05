from dotenv import load_dotenv
import psycopg2
import os

from model.Cliente import Cliente
from model.Ordem import Ordem

load_dotenv()

class BancoDeDados:

    @staticmethod
    def retorna_parametros_conexao_banco_de_dados():
        parametros_conexao = {
            "user": os.getenv('DB_USER'),
            "password": os.getenv('DB_PASS'),
            "host": os.getenv('DB_HOST'),
            "port": os.getenv('DB_PORT'),
            "database": os.getenv('DB_NAME')
        }

        return parametros_conexao

    def __init__(self):
        self.conn = psycopg2.connect(**self.retorna_parametros_conexao_banco_de_dados())
        self.cursor = self.conn.cursor()


    def __del__(self):
        self.cursor.close()
        self.conn.close()


    def adicionar_cliente(self, cliente: Cliente):
        print("Adicionando cliente...")
        insert_query = f"INSERT INTO clientes \
            (nome, cpf, rg, data_nascimento, cep, numero_residencia, logradouro, complemento, bairro, cidade, estado) \
            VALUES ( \
                '{cliente.get_nome()}', \
                '{cliente.get_cpf()}', \
                '{cliente.get_rg()}', \
                '{cliente.get_data_nasc()}', \
                '{cliente.get_endereco()['cep']}', \
                '{cliente.get_num_casa()}', \
                '{cliente.get_endereco()['logradouro']}', \
                '{cliente.get_endereco()['complemento']}', \
                '{cliente.get_endereco()['bairro']}', \
                '{cliente.get_endereco()['cidade']}', \
                '{cliente.get_endereco()['estado']}' \
            )"
        self.cursor.execute(insert_query)
        self.conn.commit()
        print("Cliente adicionado com sucesso.")

    
    def listar_clientes(self):
        print("Buscando clientes...")
        select_query = "SELECT * FROM clientes"
        self.cursor.execute(select_query)
        clientes = self.cursor.fetchall()
        for cliente in clientes:
            print(cliente)
        return clientes


    def buscar_cliente_por_cpf(self, cpf: str) -> tuple:
        print("Buscando cliente...")
        select_query = f"SELECT * FROM clientes WHERE cpf = '{cpf}'"
        self.cursor.execute(select_query)
        cliente = self.cursor.fetchall()
        return cliente[0]


    def atualizar_cliente(self, cliente: Cliente):
        update_query = f"UPDATE clientes \
        SET nome = '{cliente.get_nome()}', \
            cpf = '{cliente.get_cpf()}', \
            rg = '{cliente.get_rg()}', \
            data_nascimento = '{cliente.get_data_nasc()}', \
            numero_residencia = '{cliente.get_num_casa()}', \
            cep = '{cliente.get_endereco()['cep']}', \
            logradouro = '{cliente.get_endereco()['logradouro']}', \
            complemento = '{cliente.get_endereco()['complemento']}', \
            bairro = '{cliente.get_endereco()['bairro']}', \
            cidade = '{cliente.get_endereco()['cidade']}', \
            estado = '{cliente.get_endereco()['estado']}' \
        WHERE id = {cliente.get_id()}"
        self.cursor.execute(update_query)
        self.conn.commit()
        print("Cliente atualizado com sucesso.")


    def remover_cliente(self, id: int):
        print(f"Removendo cliente {id}...")
        delete_query = f"DELETE FROM clientes WHERE id = {id}"
        self.cursor.execute(delete_query)
        self.conn.commit()
        print("Cliente removido com sucesso.")

    # <-- ORDEM -->
    def adicionar_ordem(self, ordem: Ordem):
        print("Adicionando ordem...")
        insert_query = f"INSERT INTO ordens \
            (nome, ticket, valor_compra, quantidade_compra, data_compra, cliente_id) \
            VALUES ( \
                '{ordem.get_nome()}', \
                '{ordem.get_ticket()}', \
                '{ordem.get_valor_compra()}', \
                '{ordem.get_quantidade_compra()}', \
                '{ordem.get_data_compra()}', \
                '{ordem.get_cliente_id()}' \
            )"
        self.cursor.execute(insert_query)
        self.conn.commit()
        print("Ordem adicionada com sucesso.")

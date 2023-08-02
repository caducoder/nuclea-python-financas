from dotenv import load_dotenv
import psycopg2
import os

load_dotenv()

def retorna_parametros_conexao_banco_de_dados():
    parametros_conexao = {
        "user": os.getenv('DB_USER'),
        "password": os.getenv('DB_PASS'),
        "host": os.getenv('DB_HOST'),
        "port": os.getenv('DB_PORT'),
        "database": os.getenv('DB_NAME')
    }

    return parametros_conexao


def conexao_postgres():
    try:
        connection = psycopg2.connect(**retorna_parametros_conexao_banco_de_dados())
        cursor = connection.cursor()
        print("Database connected successfully")
        return cursor, connection
    except:
        print("Database not connected")
    

def listar_clientes():
    print("Buscando clientes...")
    select_query = "SELECT * FROM clientes"
    cursor, _ = conexao_postgres()
    cursor.execute(select_query)
    clientes = cursor.fetchall()
    cursor.close()
    for cliente in clientes:
        print(cliente)


def adicionar_cliente(cliente):
    print("Adicionando cliente...")
    cursor, connection = conexao_postgres()
    insert_query = f"INSERT INTO \
        clientes (nome, cpf, rg, data_nascimento, cep, numero_residencia, logradouro, complemento, bairro, cidade, estado) \
        VALUES ('{cliente['nome']}', '{cliente['cpf']}', '{cliente['rg']}', '{cliente['data_nasc']}', '{cliente['endereco']['CEP']}', \
        '{cliente['num_casa']}', '{cliente['endereco']['Logradouro']}', '{cliente['endereco']['Complemento']}', \
        '{cliente['endereco']['Bairro']}', '{cliente['endereco']['Cidade']}', '{cliente['endereco']['Estado']}')"
    cursor.execute(insert_query)
    connection.commit()
    cursor.close()
    connection.close()
    print("Cliente adicionado com sucesso.")

def atualizar_cliente():
    pass

def remover_cliente(id: int):
    print(f"Removendo cliente {id}...")
    cursor, connection = conexao_postgres()
    delete_query = f"DELETE FROM clientes WHERE id = {id}"
    cursor.execute(delete_query)
    connection.commit()
    cursor.close()
    connection.close()
    print("Cliente removido com sucesso.")


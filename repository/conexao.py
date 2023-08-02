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
        return cursor
    except:
        print("Database not connected")
    


def seleciona_cliente():
    print("Buscando clientes...")
    select_query = "SELECT * FROM clientes"
    cursor = conexao_postgres()
    cursor.execute(select_query)
    clientes = cursor.fetchall()
    for cliente in clientes:
        print(cliente)

seleciona_cliente()
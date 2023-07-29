import unittest
from unittest.mock import patch
from utils.cpf import gerar_cpf
from faker import Factory

from main import main, clientes

class TestFunctions(unittest.TestCase):

    def gerar_nome_fake(self):
        fake = Factory.create("pt_BR")
        print(fake.name())
        return fake.name()
    

    def test_cliente(self):
        nome = self.gerar_nome_fake()
        cpf = gerar_cpf()
        inputs = [1, nome, cpf, "12.345.678-0", "02/02/2000", "05003060", "42", "nao"]


        with patch("builtins.input", side_effect=inputs):
            main()

        cliente_esperado = {
            'nome': nome, 
            'cpf': f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}", 
            'rg': '12.345.678-0', 
            'data_nasc': '22/02/2010', 
            'endereco': {
                'CEP': '05003-060', 
                'Logradouro': 'Rua Higino Pellegrini', 
                'Bairro': 'Água Branca', 
                'Cidade': 'São Paulo', 'Estado': 'SP'}, 
            'num_casa': '42'
        }

        self.assertIn(cliente_esperado, clientes)
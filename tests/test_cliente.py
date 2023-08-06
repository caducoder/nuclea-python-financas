import unittest
from unittest.mock import patch
from utils.cpf import gerar_cpf
from faker import Factory


from model.Cliente import Cliente

class TestCliente(unittest.TestCase):

    def gerar_nome_fake(self):
        fake = Factory.create("pt_BR")
        print(fake.name())
        return fake.name()
    

    def test_cliente_object(self):
        cliente = Cliente()
        nome = self.gerar_nome_fake()
        cpf = gerar_cpf()
        
        cliente.set_nome(nome)
        cliente.set_cpf(f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}")
        cliente.set_rg('12.345.678-0')
        cliente.set_data_nasc('22/02/2010')
        cliente.set_num_casa(42)
        cliente.set_endereco({
                'cep': '05003-060', 
                'logradouro': 'Rua Higino Pellegrini', 
                'bairro': 'Água Branca', 
                'cidade': 'São Paulo', 
                'estado': 'SP'
            }
        )
        
        self.assertIsInstance(cliente, Cliente)


if __name__ == '__main__':
    unittest.main()
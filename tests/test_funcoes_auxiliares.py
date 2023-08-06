import unittest
from unittest.mock import patch
from utils.funcoes_auxiliares import *

# não consegui testar as funções com 'while True'
class TestFuncoesAuxiliares(unittest.TestCase):

    def test_shoud_capitalize_text(self):
        nome = formatar_texto("fulano de tal")

        self.assertEqual(nome, "Fulano De Tal")

    
    def test_valid_RG(self):
        rg = "28.363.154-5"
        rg_valido = None
        with patch("builtins.input", side_effect=[rg]):
            rg_valido = validar_rg("RG: ")

        self.assertEqual(rg, rg_valido)

    
    def test_tuple_to_string(self):
        string = join_tuple_string(('ABCD3'))

        self.assertEqual(string, "ABCD3.SA")


if __name__ == '__main__':
    unittest.main()
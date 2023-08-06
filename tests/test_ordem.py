import unittest
from model.Ordem import Ordem

class TestOrdem(unittest.TestCase):

    def test_ordem_object(self):
        ordem = Ordem()
        
        self.assertIsInstance(ordem, Ordem)


if __name__ == '__main__':
    unittest.main()
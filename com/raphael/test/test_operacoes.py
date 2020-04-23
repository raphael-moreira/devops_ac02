from unittest import TestCase
from com.raphael.operacoes import Operacoes

class TestOperacoes(TestCase):
    
    def setUp(self):
        self.operacoes = Operacoes()

    def test_soma(self):
        self.assertEqual(self.operacoes.soma([1, 3]), 4, 'Deveria ser 4')

        

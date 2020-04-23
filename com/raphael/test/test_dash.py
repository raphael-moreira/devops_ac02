from unittest import TestCase
from com.raphael.dash import Dash

class TestDash(TestCase):
    
    def setUp(self):
        self.dash = Dash()

    def test_subtracao(self):
        self.assertEqual(self.dash.subtracao([3, 5]), -8, 'Deveria ser -8')

        

import unittest
from app import app

class AutoTrackerTests(unittest.TestCase):

    # O método setUp corre sempre antes de cada teste
    def setUp(self):
        # Cria um "cliente de teste" para simular o navegador
        app.config['TESTING'] = True
        self.client = app.test_client()

    # Teste 1: A página principal está a funcionar?
    def test_pagina_principal_carrega(self):
        resposta = self.client.get('/')
        # Verifica se o servidor devolveu o código 200 (Sucesso)
        self.assertEqual(resposta.status_code, 200)
        # Verifica se a palavra "AutoTracker" está no código HTML devolvido
        self.assertIn(b'AutoTracker', resposta.data)

    # Teste 2: A página de adicionar registo está a funcionar?
    def test_pagina_novo_registo_carrega(self):
        resposta = self.client.get('/novo_registo')
        self.assertEqual(resposta.status_code, 200)
        # Verifica se o botão do formulário está presente
        self.assertIn(b'Guardar Registo', resposta.data)

if __name__ == '__main__':
    unittest.main()
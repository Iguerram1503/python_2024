import unittest
import main

class TestMain(unittest.TestCase):

    def test_suma_cinco_uno(self):
        test_parameter = 5
        result = main.suma_cinco(test_parameter)
        self.assertEqual((result, 10))

    def test_suma_cinco_dos(self):
        test_parameter = 'String'
        result = main.suma_cinco(test_parameter)
        self.assertIsInstance(result, ValueError)

    def test_suma_cinco_tres(self):
        test_parameter = None
        result = main.suma_cinco(test_parameter)
        self.assertEqual(result, 'Por favor ingresa un numero')


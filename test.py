import unittest
from wednesday import app


class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_roman_to_integer_conversion(self):
        # XI = 11
        response = self.app.get('/number/XI')
        data = response.get_json()
        self.assertEqual(data['value'], 'XI')
        self.assertEqual(data['output'], 11)

        # IX = 9
        response = self.app.get('/number/IX')
        data = response.get_json()
        self.assertEqual(data['value'], 'IX')
        self.assertEqual(data['output'], 9)


if __name__ == '__main__':
    unittest.main()

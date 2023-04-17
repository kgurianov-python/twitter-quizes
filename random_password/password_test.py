import unittest
from unittest.mock import patch

from random_password.pass_generator import generate_password, DEFAULT_REQUIREMENTS


class MyTestCase(unittest.TestCase):

    def do_test_validity(self, expected, required=DEFAULT_REQUIREMENTS):
        for template in required:
            self.assertTrue(any(map(lambda x: x in template, expected)))

    @patch('builtins.input', return_value="1")
    def test_weak(self, mocked_input):
        expected = generate_password()
        self.assertEqual(5, len(expected))
        self.do_test_validity(expected)

    @patch('builtins.input', return_value="2")
    def test_strong(self, strength):
        expected = generate_password()
        self.assertEqual(8, len(expected))
        self.do_test_validity(expected)

    @patch('builtins.input', return_value="3")
    def test_very_strong(self, strength):
        expected = generate_password()
        self.assertEqual(12, len(expected))
        self.do_test_validity(expected)

    @patch('builtins.input', return_value="3")
    def test_custom_req_weak(self, strength):
        required = ['ABC', '123', '&%^']
        expected = generate_password(required)
        self.assertEqual(12, len(expected))
        self.do_test_validity(expected, required)


if __name__ == '__main__':
    unittest.main()

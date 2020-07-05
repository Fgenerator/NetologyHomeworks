import unittest
import app
from unittest.mock import patch

class TestSecretary(unittest.TestCase):
    def test_add_new_document(self):
        with patch('app.input', return_value='123'):
            app.add_new_doc()
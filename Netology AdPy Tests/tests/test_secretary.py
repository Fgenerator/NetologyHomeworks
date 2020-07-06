import unittest
import app
from unittest.mock import patch


class TestSecretary(unittest.TestCase):
    def setUp(self):
        # self.documents, self.directories = [], {}
        # with patch('app.update_date', return_value=(self.documents, self.directories)):
        with patch('app.input', return_value='q'):
            app.secretary_program_start()

    def test_move_doc_to_shelf(self):
        with patch('app.input', side_effect=['10006', '3']):
            app.move_doc_to_shelf()
        self.assertIn('10006', app.directories.get('3', []))

    def test_add_new_document(self):
        self.assertNotIn('333', app.directories.get('123', []))
        with patch('app.input', side_effect=['333', 'pasp', 'Max', '123']):
            app.add_new_doc()
        self.assertIn('333', app.directories.get('123', []))

    def test_negative_check_document_existance(self):
        self.assertNotIn('555', [doc['number'] for doc in app.documents])
        result = app.check_document_existance('555')
        self.assertFalse(result)

    def test_check_document_existance(self):
        self.assertIn('10006', [doc['number'] for doc in app.documents])
        result = app.check_document_existance('10006')
        self.assertTrue(result)

    def test_get_doc_owner_name(self):
        with patch('app.input', return_value='10006'):
            result = app.get_doc_owner_name()
        self.assertIn(result, [doc['name'] for doc in app.documents])


if __name__ == '__main__':
    unittest.main()
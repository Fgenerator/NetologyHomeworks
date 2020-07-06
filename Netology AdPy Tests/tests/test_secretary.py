import unittest
import app
from unittest.mock import patch
import io


class TestSecretary(unittest.TestCase):
    def setUp(self):
        # self.documents, self.directories = [], {}
        # with patch('app.update_date', return_value=(self.documents, self.directories)):
        with patch('app.input', return_value='q'):
            app.secretary_program_start()

    def test_update_date(self):
        self.assertTrue(app.documents)
        self.assertTrue(app.directories)

    def test_negative_check_document_existance(self):
        self.assertNotIn('555', [doc['number'] for doc in app.documents])
        result = app.check_document_existance('555')
        self.assertFalse(result)

    def test_check_document_existance(self):
        self.assertIn('10006', [doc['number'] for doc in app.documents])
        result = app.check_document_existance('10006')
        self.assertTrue(result)

    def test_get_doc_owner_name(self):
        self.assertIn('10006', [doc['number'] for doc in app.documents])
        with patch('app.input', return_value='10006'):
            result = app.get_doc_owner_name()
        self.assertIn(result, [doc['name'] for doc in app.documents])

    def get_docs_owners(self):
        owners = [doc['name'] for doc in app.documents]
        return owners

    def test_get_all_doc_owners_names(self):
        result = app.get_all_doc_owners_names()
        self.assertTrue(result)
        for name in result:
            self.assertIn(name, self.get_docs_owners())

    def get_docs_numbers_from_shells(self):
        docs = []
        for shell in app.directories.values():
            for doc in shell:
                docs.append(doc)
        return docs

    def test_remove_doc_from_shelf(self):
        doc_number = '10006'
        docs = self.get_docs_numbers_from_shells()

        self.assertIn(doc_number, docs)
        app.remove_doc_from_shelf(doc_number)
        docs = self.get_docs_numbers_from_shells()

        self.assertNotIn(doc_number, docs)

    def test_add_new_shelf(self):
        shelf_num = '345'
        self.assertNotIn(shelf_num, app.directories.keys())
        with patch('app.input', return_value=shelf_num):
            app.add_new_shelf()
        self.assertIn(shelf_num, app.directories.keys())

    def test_negative_add_new_shelf(self):
        shelf_num = '1'
        self.assertIn(shelf_num, app.directories.keys())
        with patch('app.input', return_value=shelf_num):
            result = app.add_new_shelf()
        self.assertFalse(result[1])

    def test_append_doc_to_shelf(self):
        doc_number = '8800'
        shelf_number = '3'
        app.append_doc_to_shelf(doc_number, shelf_number)
        self.assertIn(shelf_number, app.directories.keys())
        self.assertIn(doc_number, self.get_docs_numbers_from_shells())

    def test_delete_doc(self):
        doc_number = '10006'
        with patch('app.input', return_value=doc_number):
            app.delete_doc()
        self.assertFalse(app.check_document_existance(doc_number))

    def test_get_doc_shelf(self):
        doc_number = '10006'
        with patch('app.input', return_value=doc_number):
            result = app.get_doc_shelf()
        self.assertIn(result, app.directories.keys())

    def test_show_document_info(self):
        doc = app.documents[0]
        doc_type = doc['type']
        doc_number = doc['number']
        doc_owner = doc['name']

        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            app.show_document_info(doc)
        
        assert fake_stdout.getvalue() == f'{doc_type} "{doc_number}" "{doc_owner}"\n'

    def test_show_all_docs_info(self):
        with patch('sys.stdout', new=io.StringIO()) as main_fake_stdout:
            app.show_all_docs_info()

        f_stdout = '\n'
        for doc in app.documents:
            doc_type = doc['type']
            doc_number = doc['number']
            doc_owner = doc['name']

            with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
                app.show_document_info(doc)
            f_stdout += fake_stdout.getvalue()
            assert fake_stdout.getvalue() == f'{doc_type} "{doc_number}" "{doc_owner}"\n'

        assert main_fake_stdout.getvalue() == 'Список всех документов:\n' + f_stdout

    # example
    def test_move_doc_to_shelf(self):
        with patch('app.input', side_effect=['10006', '3']):
            app.move_doc_to_shelf()
        self.assertIn('10006', app.directories.get('3', []))

    def test_add_new_document(self):
        self.assertNotIn('333', app.directories.get('123', []))
        with patch('app.input', side_effect=['333', 'pasp', 'Max', '123']):
            app.add_new_doc()
        self.assertIn('333', app.directories.get('123', []))


if __name__ == '__main__':
    unittest.main()
import  unittest

class TestSimple(unittest.TestCase):
    def setUp(self):
        self.data_mult = 2 * 2

    def test_zero_div(self):
        self.assertRaises(ZeroDivisionError, lambda a, b: a / b, 2, 0)

    def test_multiple(self):
        self.assertEqual(self.data_mult, 4)
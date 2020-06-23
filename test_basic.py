import unittest
from basic import basic


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.new_basic = basic("john doe", "cs", "2022")
    def test_get_name(self):
        self.assertEqual(self.new_basic.get_name(), "john doe")
    def test_get_major(self):
        self.assertEqual(self.new_basic.get_major(), "cs")
    def test_get_year(self):
        self.assertEqual(self.new_basic.get_year(), "2022")
    def test_set_name(self):
        self.new_basic.set_name("jane")
        self.assertEqual(self.new_basic.get_name(), "jane")
    def test_set_major(self):
        self.new_basic.set_major("cmda")
        self.assertEqual(self.new_basic.get_major(), "cmda")
    def test_set_year(self):
        self.new_basic.set_year("2021")
        self.assertEqual(self.new_basic.get_year(), "2021")


if __name__ == '__main__':
    unittest.main()

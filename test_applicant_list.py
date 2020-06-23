import unittest
from applicant_list import applicant_list


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.new_list = applicant_list()

    def test_get_num_entries(self):
        self.assertEqual(0, self.new_list.get_num_of_entries())

    def test_empty(self):
        self.assertTrue(self.new_list.is_empty())

    def test_add_true(self):
        cheese = "cheese"
        self.assertTrue(self.new_list.add(cheese))

    def test_add_false(self):
        cheese = None
        self.assertFalse(self.new_list.add(cheese))

    def test_remove_false(self):
        cheese = None
        self.assertFalse(self.new_list.remove(cheese))

    def test_remove_true(self):
        cheese = "cheese"
        self.new_list.add(cheese)
        self.assertTrue(self.new_list.remove(cheese))

    def test_remove_false_2(self):
        cheese = "burger"
        self.assertFalse(self.new_list.remove(cheese))


if __name__ == '__main__':
    unittest.main()

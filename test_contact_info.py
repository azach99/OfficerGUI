import unittest
from contact_info import contact_info


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.new_contact = contact_info("7034759366", "vt.edu", "860 plantation")

    def test_get_number(self):
        self.assertEqual(self.new_contact.get_phone(), "7034759366")

    def test_get_email(self):
        self.assertEqual(self.new_contact.get_email(), "vt.edu")

    def test_get_address(self):
        self.assertEqual(self.new_contact.get_address(), "860 plantation")

    def test_set_number(self):
        self.new_contact.set_phone("123")
        self.assertEqual(self.new_contact.get_phone(), "123")

    def test_set_email(self):
        self.new_contact.set_email("gmail.com")
        self.assertEqual(self.new_contact.get_email(), "gmail.com")

    def test_set_address(self):
        self.new_contact.set_address("860")
        self.assertEqual(self.new_contact.get_address(), "860")

    def test_string(self):
        self.assertEqual(str(self.new_contact), "7034759366 vt.edu 860 plantation")


if __name__ == '__main__':
    unittest.main()

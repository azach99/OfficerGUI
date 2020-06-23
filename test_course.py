import unittest
from course import course


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.new_course = course(1215, "engineering", 2)
    def test_get_number(self):
        self.assertEqual(self.new_course.get_number(), 1215)
    def test_get_name(self):
        self.assertEqual(self.new_course.get_name(), "engineering")
    def test_get_credits(self):
        self.assertEqual(self.new_course.get_credits(), 2)
    def test_set_name(self):
        self.new_course.set_name("calculus")
        self.assertEqual(self.new_course.get_name(), "calculus")
    def test_set_number(self):
        self.new_course.set_number(1216)
        self.assertEqual(self.new_course.get_number(), 1216)
    def test_set_credits(self):
        self.new_course.set_credits(4)
        self.assertEqual(self.new_course.get_credits(), 4)
    def test_string(self):
        self.assertEqual("1215 engineering 2", str(self.new_course))

if __name__ == '__main__':
    unittest.main()

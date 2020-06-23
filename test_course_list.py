import unittest
from course_list import course_list
from course import course


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.new_course = course_list()

    def test_num_entries(self):
        self.assertEqual(self.new_course.get_num_entries(), 0)
    def test_is_empty(self):
        self.assertTrue(self.new_course.is_empty())
    def test_add(self):
        new_course = course(1026, "history", 3)
        self.new_course.add(new_course)
        self.assertFalse(self.new_course.is_empty())
        self.assertEqual(1, self.new_course.get_num_entries())
    def test_remove(self):
        new_course = course(1026, "history", 3)
        self.new_course.add(new_course)
        self.assertFalse(self.new_course.is_empty())
        self.assertTrue(self.new_course.remove(new_course))
        self.assertEqual(0, self.new_course.get_num_entries())
    def test_remove_2(self):
        new_course = course(1026, "history", 3)
        self.assertFalse(self.new_course.remove(new_course))
    def test_remove_3(self):
        new_course = None
        self.assertFalse(self.new_course.remove(new_course))
    def test_add_2(self):
        new_course = None
        self.assertFalse(self.new_course.add(new_course))
    def test_total_credits(self):
        new_course = course(1026, "history", 3)
        self.new_course.add(new_course)
        n_course = course(1114, "cs", 4)
        self.new_course.add(n_course)
        self.assertEqual(7, self.new_course.total_credits())


if __name__ == '__main__':
    unittest.main()

import unittest
from questions import questions


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.new_questions = questions()
    def test_one(self):
        self.new_questions.set_one("cheese")
        self.assertEqual("cheese", self.new_questions.get_one())
    def test_two(self):
        self.new_questions.set_two("two")
        self.assertEqual("two", self.new_questions.get_two())
    def test_three(self):
        self.new_questions.set_three("tree")
        self.assertEqual("tree", self.new_questions.get_three())
    def test_four(self):
        self.new_questions.set_four("food")
        self.assertEqual("food", self.new_questions.get_four())


if __name__ == '__main__':
    unittest.main()

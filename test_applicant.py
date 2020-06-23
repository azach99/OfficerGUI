import unittest
from applicant import applicant
from basic import basic
from contact_info import contact_info
from course_list import course_list
from course import course
from questions import questions


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.new_basic = basic("john", "cs", "2022")
        self.new_contact_info = contact_info("703", "vt.edu", "addy")
        self.course_list = course_list()
        self.new_course = course("1215", "engineering", "2")
        self.course_list.add(self.new_course)
        self.new_questions = questions()
        self.new_questions.set_one("one")
        self.new_questions.set_two("two")
        self.new_questions.set_three("three")
        self.new_questions.set_four("four")
        self.new_applicant = applicant(self.new_basic, self.new_contact_info, self.course_list, self.new_questions)
    def test_get_basic(self):
        self.assertEqual(self.new_applicant.get_basic().get_name(), "john")
    def test_get_contact_info(self):
        self.assertEqual(self.new_applicant.get_contact_info().get_email(), "vt.edu")
    def test_get_course_list(self):
        self.assertEqual(self.new_applicant.get_course_list().get_num_entries(), 1)
    def test_get_quesitons(self):
        self.assertEqual(self.new_applicant.get_questions().get_one(), "one")
    def test_set_basic(self):
        other_basic = basic("jane", "cmda", "2021")
        self.new_applicant.set_basic(other_basic)
        self.assertEqual(self.new_applicant.get_basic().get_name(), "jane")


if __name__ == '__main__':
    unittest.main()

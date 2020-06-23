from basic import basic
from contact_info import contact_info
from course import course
from course_list import course_list
from questions import questions


class applicant:
    def __init__(self, basic, contact_info, course_list, questions):
        self.basic = basic
        self.contact_info = contact_info
        self.course_list = course_list
        self.questions = questions

    def get_basic(self):
        return self.basic

    def get_contact_info(self):
        return self.contact_info

    def get_course_list(self):
        return self.course_list

    def get_questions(self):
        return self.questions

    def set_basic(self, new_basic):
        self.basic = new_basic

    def set_course_info(self, new_contact_info):
        self.contact_info = new_contact_info

    def set_course_list(self, new_course_list):
        self.course_list = new_course_list

    def set_questions(self, new_questions):
        self.questions = new_questions

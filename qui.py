from tkinter import *
from functools import partial
from applicant import applicant
from applicant_list import applicant_list
from basic import basic
from contact_info import contact_info
from course import course
from course_list import course_list
from questions import questions
import tkinter as tk
import sqlite3


class window:

    #string_name = tk.StringVar()
    submitted = False

    new_applicant = applicant(None, None, None, None)
    new_applicant_list = applicant_list()
    new_basic = basic(None, None, None)
    new_contact_info = contact_info(None, None, None)
    new_course_list = course_list()
    new_questions = questions()

    course_two = None

    d7_text = None
    fundraising_text = None
    hospitality_text = None
    sports_text = None
    promotions_text = None
    service_text = None
    web_text = None
    culture_text = None
    events_text = None

    name_text = None
    phone_text = None
    email_text = None
    address_text = None
    major_text = None
    year_text = None

    question_1_text = None
    question_2_text = None
    question_3_text = None
    question_4_text = None

    question_1_response = None
    question_2_response = None
    question_3_response = None
    question_4_response = None

    number_1 = None
    name_1 = None
    credits_1 = None

    number_2 = None
    name_2 = None
    credits_2 = None

    number_3 = None
    name_3 = None
    credits_3 = None

    number_4 = None
    name_4 = None
    credits_4 = None

    number_5 = None
    name_5 = None
    credits_5 = None

    number_6 = None
    name_6 = None
    credits_6 = None

    number_7 = None
    name_7 = None
    credits_7 = None

    number_8 = None
    name_8 = None
    credits_8 = None



    name = None
    phone_number_box = None
    email_label_box = None
    address_label_box = None
    major_label_box = None
    gradyear_label_box = None

    course_1_number_box = None
    course_1_name_box = None
    course_1_credits_box = None

    course_2_number_box = None
    course_2_name_box = None
    course_2_credits_box = None

    course_3_number_box = None
    course_3_name_box = None
    course_3_credits_box = None

    course_4_number_box = None
    course_4_name_box = None
    course_4_credits_box = None

    course_5_number_box = None
    course_5_name_box = None
    course_5_credits_box = None

    course_6_number_box = None
    course_6_name_box = None
    course_6_credits_box = None

    course_7_number_box = None
    course_7_name_box = None
    course_7_credits_box = None

    course_8_number_box = None
    course_8_name_box = None
    course_8_credits_box = None

    d7_box = None
    fundraising_box = None
    hospitality_box = None
    sports_box = None
    promotions_box = None
    service_box = None
    web_box = None
    culture_box = None
    events_box = None


    def __init__(self, master):

        self.conn_basic = sqlite3.connect('basic.db')
        self.conn_contact_info = sqlite3.connect('contact_info.db')
        self.conn_questions = sqlite3.connect('questions.db')

        self.c_basic = self.conn_basic.cursor()
        self.c_contact_info = self.conn_contact_info.cursor()
        self.c_questions = self.conn_questions.cursor()
        '''
        self.c_basic.execute("""CREATE TABLE basic(
                email text,
                name text,
                major text,
                year text
                )""")

        self.c_contact_info.execute("""CREATE TABLE contact_info(
                    email text,
                    phone text,
                    email_2 text,
                    address text
                    )""")
        
        self.c_questions.execute("""CREATE TABLE questions_new(
                        email text,
                        question_1 text,
                        question_2 text,
                        question_3 text,
                        question_4 text
                        )""")
        '''

        self.string_name = tk.StringVar()
        self.string_phone = tk.StringVar()
        self.string_email = tk.StringVar()
        self.string_address = tk.StringVar()
        self.string_major = tk.StringVar()
        self.string_year = tk.StringVar()

        self.string_number_1 = tk.StringVar()
        self.string_name_1 = tk.StringVar()
        self.string_credits_1 = tk.StringVar()

        self.string_number_2 = tk.StringVar()
        self.string_name_2 = tk.StringVar()
        self.string_credits_2 = tk.StringVar()

        self.string_number_3 = tk.StringVar()
        self.string_name_3 = tk.StringVar()
        self.string_credits_3 = tk.StringVar()

        self.string_number_4 = tk.StringVar()
        self.string_name_4 = tk.StringVar()
        self.string_credits_4 = tk.StringVar()

        self.string_number_5 = tk.StringVar()
        self.string_name_5 = tk.StringVar()
        self.string_credits_5 = tk.StringVar()

        self.string_number_6 = tk.StringVar()
        self.string_name_6 = tk.StringVar()
        self.string_credits_6 = tk.StringVar()

        self.string_number_7 = tk.StringVar()
        self.string_name_7 = tk.StringVar()
        self.string_credits_7 = tk.StringVar()

        self.string_number_8 = tk.StringVar()
        self.string_name_8 = tk.StringVar()
        self.string_credits_8 = tk.StringVar()

        self.string_d7 = tk.StringVar()
        self.string_fundraising = tk.StringVar()
        self.string_hospitality = tk.StringVar()
        self.string_sports = tk.StringVar()
        self.string_promotions = tk.StringVar()
        self.string_service = tk.StringVar()
        self.string_web = tk.StringVar()
        self.string_culture = tk.StringVar()
        self.string_events = tk.StringVar()

        self.string_question_1 = tk.StringVar()
        self.string_question_2 = tk.StringVar()
        self.string_question_3 = tk.StringVar()
        self.string_question_4 = tk.StringVar()

        self.paddingX = 20
        self.some_frame = Frame(master)
        self.view_home(master, self.some_frame)

    def insert_applicant_basic(self, applicant):
        with self.conn_basic:
            self.c_basic.execute("INSERT INTO basic VALUES(:email, :name, :major, :year)", {'email': applicant.get_contact_info().get_email(), 'name': applicant.get_basic().get_name(), 'major': applicant.get_basic().get_major(), 'year': applicant.get_basic().get_year()})
    def insert_applicant_contact_info(self, applicant):
        with self.conn_contact_info:
            self.c_contact_info.execute("INSERT INTO contact_info VALUES(:email, :phone, :email_2, :address)", {'email': applicant.get_contact_info().get_email(), 'phone': applicant.get_contact_info().get_phone(), 'email_2': applicant.get_contact_info().get_email(), 'address': applicant.get_contact_info().get_address()})
    def insert_applicant_questions(self, applicant):
        with self.conn_questions:
            self.c_questions.execute("INSERT INTO questions_new VALUES(:email, :question_1, :question_2, :question_3, :question_4)", {'email': applicant.get_contact_info().get_email(), 'question_1': applicant.get_questions().get_one(), 'question_2': applicant.get_questions().get_two(), 'question_3': applicant.get_questions().get_three(), 'question_4': applicant.get_questions().get_four()})
    def get_applicant_basic(self, email_string):
        self.string = str(email_string)
        self.c_basic.execute("SELECT * FROM basic WHERE email = :email", {'email': self.string})
        return self.c_basic.fetchall()
    def get_applicant_contact_info(self, email_string):
        '''
        self.c_contact_info.execute("SELECT * FROM contact_info WHERE email = :email", {'email': email_string})
        self.c_contact_info.fetchone()
        '''
        self.string = str(email_string)
        self.c_contact_info.execute("SELECT * FROM contact_info WHERE email = :email", {'email': self.string})
        return self.c_contact_info.fetchall()
    def get_applicant_questions(self, email_string):
        '''
        self.c_questions.execute("SELECT * FROM questions_new WHERE email = :email", {'email': email_string})
        self.c_questions.fetchall()
        '''
        self.string = str(email_string)
        self.c_questions.execute("SELECT * FROM questions_new WHERE email = :email", {'email': self.string})
        return self.c_questions.fetchall()
    def insert_applicant(self, applicant):
        self.insert_applicant_basic(applicant)
        self.insert_applicant_contact_info(applicant)
        self.insert_applicant_questions(applicant)
    def clear(self):
        self.new_applicant = applicant(None, None, None, None)
        #self.new_applicant_list = applicant_list()
        self.new_basic = basic(None, None, None)
        self.new_contact_info = contact_info(None, None, None)
        self.new_course_list = course_list()
        self.new_questions = questions()

        self.course_two = None

        self.d7_text = None
        self.fundraising_text = None
        self.hospitality_text = None
        self.sports_text = None
        self.promotions_text = None
        self.service_text = None
        self.web_text = None
        self.culture_text = None
        self.events_text = None

        self.name_text = None
        self.phone_text = None
        self.email_text = None
        self.address_text = None
        self.major_text = None
        self.year_text = None

        self.question_1_text = None
        self.question_2_text = None
        self.question_3_text = None
        self.question_4_text = None

        self.question_1_response = None
        self.question_2_response = None
        self.question_3_response = None
        self.question_4_response = None

        self.number_1 = None
        self.name_1 = None
        self.credits_1 = None

        self.number_2 = None
        self.name_2 = None
        self.credits_2 = None

        self.number_3 = None
        self.name_3 = None
        self.credits_3 = None

        self.number_4 = None
        self.name_4 = None
        self.credits_4 = None

        self.number_5 = None
        self.name_5 = None
        self.credits_5 = None

        self.number_6 = None
        self.name_6 = None
        self.credits_6 = None

        self.number_7 = None
        self.name_7 = None
        self.credits_7 = None

        self.number_8 = None
        self.name_8 = None
        self.credits_8 = None

        self.name = None
        self.phone_number_box = None
        self.email_label_box = None
        self.address_label_box = None
        self.major_label_box = None
        self.gradyear_label_box = None

        self.course_1_number_box = None
        self.course_1_name_box = None
        self.course_1_credits_box = None

        self.course_2_number_box = None
        self.course_2_name_box = None
        self.course_2_credits_box = None

        self.course_3_number_box = None
        self.course_3_name_box = None
        self.course_3_credits_box = None

        self.course_4_number_box = None
        self.course_4_name_box = None
        self.course_4_credits_box = None

        self.course_5_number_box = None
        self.course_5_name_box = None
        self.course_5_credits_box = None

        self.course_6_number_box = None
        self.course_6_name_box = None
        self.course_6_credits_box = None

        self.course_7_number_box = None
        self.course_7_name_box = None
        self.course_7_credits_box = None

        self.course_8_number_box = None
        self.course_8_name_box = None
        self.course_8_credits_box = None

        self.d7_box = None
        self.fundraising_box = None
        self.hospitality_box = None
        self.sports_box = None
        self.promotions_box = None
        self.service_box = None
        self.web_box = None
        self.culture_box = None
        self.events_box = None


    def eboard_view(self, master, frame):
        frame.destroy()
        self.applicant_list_test = applicant_list()
        self.basic_test = basic("cheese", "cheese2", "cheese3")
        self.contact_info_test = contact_info("love", "hope", "sorrow")
        self.course_test = course("1216", "engineering", "2")
        self.course_test_2 = course("1035", "chem", "3")
        self.course_list_test = course_list()
        self.course_list_test.add(self.course_test)
        self.course_list_test.add(self.course_test_2)
        self.question_test = questions()
        self.question_test.set_one("i dont know")
        self.question_test.set_two("yes it can")
        self.question_test.set_three("taking fate in hands")
        self.question_test.set_four("cloud reading book")
        self.applicant_test = applicant(self.basic_test, self.contact_info_test, self. course_list_test, self.question_test)
        self.applicant_list_test.add(self.applicant_test)

        self.basic_test_2 = basic("pepperoni", "pizza", "tomato")
        self.contact_info_test_2 = contact_info("I", "need", "food")
        self.applicant_test_2 = applicant(self.basic_test_2, self.contact_info_test_2, self.course_list_test, self.question_test)
        self.applicant_list_test.add(self.applicant_test_2)

        self.main_frame = Frame(master, width = 80)
        i = 0
        #j = 0
        self.head_label = Label(self.main_frame,
                                text="2020-2021 FASA Officer Committees Application", width=80)  # , height = 5)

        self.head_label.pack(fill=X)
        self.one = Frame(self.main_frame, width = 80)
        self.two = Frame(self.main_frame, width = 80)
        self.three = Frame(self.main_frame,width = 80)
        self.four = Frame(self.main_frame, width = 80)
        self.five = Frame(self.main_frame, width = 80)
        self.one.pack(fill = X, pady = 10)
        self.two.pack(fill = X, pady = 10)
        self.three.pack(fill = X, pady = 10)
        self.four.pack(fill = X, pady = 10)
        self.five.pack(fill = X, pady = 10)
        '''
        self.some_list = applicant_list()

        for a in range (40):
            self.some_list.add(a)

        for self.app in self.some_list.list:
            if i < 8:
                self.this_label = Button(self.one, text = i, width = 5)
                self.this_label.pack(side = LEFT, padx = 30)
            elif i < 16:
                self.this_label_2 = Button(self.two, text = i, width = 5)
                self.this_label_2.pack(side = LEFT, padx = 30)
            elif i < 24:
                self.this_label_3 = Button(self.three, text = i, width = 5)
                self.this_label_3.pack(side = LEFT, padx = 30)
            elif i < 32:
                self.this_label_4 = Button(self.four, text = i, width = 5)
                self.this_label_4.pack(side = LEFT, padx = 30)
            elif i < 40:
                self.this_label_5 = Button(self.five, text = i, width = 5)
                self.this_label_5.pack(side = LEFT, padx = 30)
            else:
                pass
            i += 1
        '''


        '''
        for self.app in self.applicant_list_test.list:
            if (i % 5) == 0 and (i is not 0):
                j += 1
            self.app_button = Button(self.main_frame, text = self.app.get_basic().get_name(), command = partial(self.view_info, master, self.main_frame, self.app))
            self.app_button.grid(column = (i % 5), row = j)
            i += 1
        '''

        for self.app in self.new_applicant_list.list:
            if i < 8:
                self.this_button = Button(self.one, text = self.app.get_basic().get_name(), command = partial(self.view_info, master, self.main_frame, self.app))
                self.this_button.pack(side = LEFT, padx = 30)
            elif i < 16:
                self.this_button = Button(self.two, text=self.app.get_basic().get_name(),
                                          command=partial(self.view_info, master, self.main_frame, self.app))
                self.this_button.pack(side=LEFT, padx=30)
            elif i < 24:
                self.this_button = Button(self.three, text=self.app.get_basic().get_name(),
                                          command=partial(self.view_info, master, self.main_frame, self.app))
                self.this_button.pack(side=LEFT, padx=30)
            elif i < 32:
                self.this_button = Button(self.four, text=self.app.get_basic().get_name(),
                                          command=partial(self.view_info, master, self.main_frame, self.app))
                self.this_button.pack(side=LEFT, padx=30)
            elif i < 40:
                self.this_button = Button(self.five, text=self.app.get_basic().get_name(),
                                          command=partial(self.view_info, master, self.main_frame, self.app))
                self.this_button.pack(side=LEFT, padx=30)
            else:
                pass
            i += 1
        self.basic_button = Button(self.main_frame, text = "Find Name, Year, Major", command = partial(self.basic_window, master, self.main_frame))
        self.basic_button.pack()
        self.contact_info_button = Button(self.main_frame, text = "Find Phone, Email, Address", command = partial(self.contact_info_window, master, self.main_frame))
        self.contact_info_button.pack()
        #self.questions_button = Button(self.main_frame, text = "Find Questions", command = partial(self.questions_window, master, self.main_frame))
        #self.questions_button.pack()
        self.main_frame.pack()
    def questions_window(self, master, frame):
        frame.destroy()
        self.main_frame = Frame(master)
        self.head_label = Label(self.main_frame,
                                text="2020-2021 FASA Officer Committees Application", width=80)  # , height = 5)

        self.head_label.pack(fill=X)
        self.label = Label(self.main_frame, text="Enter applicant's email", width=80)
        self.label.pack()
        self.label_entry_3 = Entry(self.main_frame)
        self.label_entry_3.pack()
        self.spacer = Label(self.main_frame, text="")
        self.spacer.pack()
        self.input_string = str(self.label_entry_3.get())
        self.enter_button = Button(self.main_frame, text="Enter",
                                   command=partial(self.display_questions, master, self.main_frame, self.input_string))
        self.enter_button.pack()
        self.main_frame.pack()
    def contact_info_window(self, master, frame):
        #pass
        frame.destroy()
        self.main_frame = Frame(master)
        self.head_label = Label(self.main_frame,
                                text="2020-2021 FASA Officer Committees Application", width=80)  # , height = 5)

        self.head_label.pack(fill=X)
        self.label = Label(self.main_frame, text="Enter applicant's email", width=80)
        self.label.pack()
        self.label_entry_2 = Entry(self.main_frame)
        self.label_entry_2.pack()
        self.spacer = Label(self.main_frame, text="")
        self.spacer.pack()
        self.input_string = str(self.label_entry_2.get())
        self.enter_button = Button(self.main_frame, text="Enter",
                                   command=partial(self.display_contact_info, master, self.main_frame, self.input_string))
        self.enter_button.pack()
        self.main_frame.pack()
    def basic_window(self, master, frame):
        frame.destroy()
        self.main_frame = Frame(master)
        self.head_label = Label(self.main_frame,
                                text="2020-2021 FASA Officer Committees Application", width=80)  # , height = 5)

        self.head_label.pack(fill=X)
        self.label = Label(self.main_frame, text = "Enter applicant's email", width = 80)
        self.label.pack()
        self.label_entry = Entry(self.main_frame)
        self.label_entry.pack()
        self.spacer = Label(self.main_frame, text = "")
        self.spacer.pack()
        self.input_string = str(self.label_entry.get())
        self.enter_button = Button(self.main_frame, text = "Enter", command = partial(self.display_basic_info, master, self.main_frame, self.input_string))
        self.enter_button.pack()
        self.main_frame.pack()
        #pass
    def display_questions(self, master, frame, string_email):
        print(self.label_entry_3.get())
        self.temp = self.label_entry_3.get()
        frame.destroy()
        self.main_frame = Frame(master)
        # print(str(self.label_entry.get()))
        self.input_data = str(self.get_applicant_questions(self.temp))
        self.result = Label(self.main_frame, text=self.input_data)
        self.result.pack()
        self.return_button = Button(self.main_frame, text="Return to Applicants",
                                    command=partial(self.eboard_view, master, self.main_frame))
        self.return_button.pack()
        self.spacer = Label(self.main_frame, text="")
        self.spacer.pack()
        self.main_frame.pack()
    def display_contact_info(self, master, frame, string_email):
        #pass
        print(self.label_entry_2.get())
        self.temp = self.label_entry_2.get()
        frame.destroy()
        self.main_frame = Frame(master)
        # print(str(self.label_entry.get()))
        self.input_data = str(self.get_applicant_contact_info(self.temp))
        self.result = Label(self.main_frame, text=self.input_data)
        self.result.pack()
        self.return_button = Button(self.main_frame, text="Return to Applicants",
                                    command=partial(self.eboard_view, master, self.main_frame))
        self.return_button.pack()
        self.spacer = Label(self.main_frame, text="")
        self.spacer.pack()
        self.main_frame.pack()

    def display_basic_info(self, master, frame, string_email):
        print(self.label_entry.get())
        self.temp = self.label_entry.get()
        frame.destroy()
        self.main_frame = Frame(master)
        #print(str(self.label_entry.get()))
        self.input_data = str(self.get_applicant_basic(self.temp))
        self.result = Label(self.main_frame, text = self.input_data)
        self.result.pack()
        self.return_button = Button(self.main_frame, text = "Return to Applicants", command = partial(self.eboard_view, master, self.main_frame))
        self.return_button.pack()
        self.spacer = Label(self.main_frame, text = "")
        self.spacer.pack()
        self.main_frame.pack()
        pass
    def view_info(self, master, frame, applicant):
        frame.destroy()
        self.applicant_frame = Frame(master, width = 80)
        self.head_label = Label(self.applicant_frame,
                                text="2020-2021 FASA Officer Committees Application", width=80)  # , height = 5)

        self.head_label.pack(fill=X)
        self.main_frame = Frame(self.applicant_frame)
        self.name_label = Label(self.main_frame, text = "Name: " + applicant.get_basic().get_name())
        self.name_label.pack()
        self.major_label = Label(self.main_frame, text = "Major: " + applicant.get_basic().get_major())
        self.major_label.pack()
        self.year_label = Label(self.main_frame, text = "Year: " + applicant.get_basic().get_year())
        self.year_label.pack()
        self.phone_label = Label(self.main_frame, text = "Phone Number: " + applicant.get_contact_info().get_phone())
        self.phone_label.pack()
        self.email_label = Label(self.main_frame, text = "Email Address: " + applicant.get_contact_info().get_email())
        self.email_label.pack()
        self.address_label = Label(self.main_frame, text = "Address: " + applicant.get_contact_info().get_address())
        self.address_label.pack()
        self.spacer_1 = Label(self.main_frame, text = "")
        self.spacer_1.pack()
        i = 0
        self.row_1 = Frame(self.main_frame, width = 80)
        self.row_1.pack(fill = X, pady = 3)
        self.row_2 = Frame(self.main_frame, width = 80)
        self.row_2.pack(fill = X, pady = 3)
        for course in applicant.get_course_list().list:
            '''
            self.number_label = Label(self.main_frame, text = "Course Number: " + course.get_number())
            self.number_label.pack()
            self.name_course_label = Label(self.main_frame, text = "Course Name: " + course.get_name())
            self.name_course_label.pack()
            self.credits_label = Label(self.main_frame, text = "Credits: " + course.get_credits())
            self.credits_label.pack()
            self.spacer = Label(self.main_frame, text = "")
            self.spacer.pack()
            '''
            if i < 4:
                self.course_frame = Frame(self.row_1)
                self.course_number = Label(self.course_frame, text = "Course Number: " + course.get_number())
                self.course_number.pack()
                self.course_name = Label(self.course_frame, text = "Course Name: " + course.get_name())
                self.course_name.pack()
                self.course_credits = Label(self.course_frame, text = "Credits: " + course.get_credits())
                self.course_credits.pack()
                self.course_frame.pack(side = LEFT, padx = 30)
            else:
                self.course_frame = Frame(self.row_1)
                self.course_number = Label(self.course_frame, text="Course Number" + course.get_number())
                self.course_number.pack()
                self.course_name = Label(self.course_frame, text="Course Name: " + course.get_name())
                self.course_name.pack()
                self.course_credits = Label(self.course_frame, text="Credits: " + course.get_credits())
                self.course_credits.pack()
                self.course_frame.pack(side=LEFT, padx=30)
        self.question_one_label = Label(self.main_frame, text = "Question 1: " + applicant.get_questions().get_one())
        self.question_one_label.pack()
        self.question_two_label = Label(self.main_frame, text = "Question 2: " + applicant.get_questions().get_two())
        self.question_two_label.pack()
        self.question_three_label = Label(self.main_frame, text = "Question 3: " + applicant.get_questions().get_three())
        self.question_three_label.pack()
        self.question_four_label = Label(self.main_frame, text = "Question 4: " + applicant.get_questions().get_four())
        self.question_four_label.pack()
        self.button_back = Button(self.main_frame, text = "View Applicants", command = partial(self.eboard_view, master, self.applicant_frame))
        self.button_back.pack()
        self.main_frame.pack()
        self.applicant_frame.pack(fill = X)

    def view_home(self, master, frame):
        if (frame is not None):
            frame.destroy()
        self.head_frame = Frame(master)
        self.head_label = Label(self.head_frame,
                                text="2020-2021 FASA Officer Committees Application", width=80)
        self.head_label.pack(fill=X)
        self.head_frame.pack(fill=X, padx=100, pady=self.paddingX)
        self.applicant_frame = Frame(self.head_frame)
        self.applicant_button = Button(self.applicant_frame, text="Applicant?",
                                       command=partial(self.view_application, master, self.head_frame,
                                                       self.applicant_frame))
        self.applicant_button.pack()
        #self.eboard_button = Button(self.head_frame, text = "Executive Board Only", command = partial(self.eboard_view, master, self.head_frame))
        self.eboard_button = Button(self.head_frame, text = "Executive Board Only", command = partial(self.confirmation, master, self.head_frame))
        self.eboard_button.pack()
        self.applicant_frame.pack()

    def confirmation(self, master, frame):
        frame.destroy()
        self.main_frame = Frame(master, width = 80)
        self.head_label = Label(self.main_frame,
                                text="2020-2021 FASA Officer Committees Application", width=80)
        self.head_label.pack(fill=X)
        self.password_frame = Frame(self.main_frame)
        self.password_frame.pack()
        self.password_label = Label(self.password_frame, text = "Enter Password: ")
        self.password_label.pack()
        self.password_input = Entry(self.password_frame)
        self.passw = self.password_input.get()
        self.password_input.pack()
        self.password_button = Button(self.password_frame, text = "Enter", command = partial(self.confirm_password, master, self.main_frame, self.password_input))
        self.password_button.pack()
        self.main_frame.pack()

    def confirm_password(self, master, frame, password):
        print(self.password_input.get())
        word = "fasa_2020_2021"

        if str(self.password_input.get()) == str(word):
            frame.destroy()
            self.main_frame = Frame(master, width=80)
            self.head_label = Label(self.main_frame,
                                    text="2020-2021 FASA Officer Committees Application", width=80)
            self.head_label.pack(fill=X)
            self.main_frame.pack()
            self.go_button = Button(self.main_frame, text = "Click to View Applicants", command = partial(self.eboard_view, master, self.main_frame))
            self.go_button.pack()
        else:
            self.output_label = Label(frame, text = "Incorrect. Try Again")
            self.output_label.pack()


    def view_application(self, master, frame_1, frame_2):
        if (self.submitted == True):
            self.clear()
            self.submitted = False
        if (self.question_1_response is not None):
            self.question_1_text = self.question_1_response.get("1.0", END)
        if (self.question_2_response is not None):
            self.question_2_text = self.question_2_response.get("1.0", END)
        if (self.question_3_response is not None):
            self.question_3_text = self.question_3_response.get("1.0", END)
        if (self.question_4_response is not None):
            self.question_4_text = self.question_4_response.get("1.0", END)
        self.new_questions.set_one(self.question_1_text)
        self.new_questions.set_two(self.question_2_text)
        self.new_questions.set_three(self.question_3_text)
        self.new_questions.set_four(self.question_4_text)
        frame_1.destroy()
        frame_2.destroy()
        self.new_course_list.clear()
        self.main_frame = Frame(master)
        self.paddingX = 20

        self.head_frame = Frame(self.main_frame)
        self.head_label = Label(self.head_frame,
                                text="2020-2021 FASA Officer Committees Application", width=80)  # , height = 5)

        self.head_label.pack(fill=X)
        self.head_frame.pack(fill=X, padx=100, pady=self.paddingX)
        self.name_field = Frame(self.main_frame)
        self.name_label = Label(self.name_field, text="Name:", width=self.paddingX)
        self.name_label.pack(side=LEFT, fill=X)


        if (not self.name is None):
            self.string_name.set("{}".format(self.name_text))
            self.name = Entry(self.name_field, textvariable = self.string_name)
        else:
            self.name = Entry(self.name_field)
        self.name.pack(fill=X)


        self.name_field.pack(fill=X, padx=self.paddingX)

        self.contact_info = Frame(self.main_frame)
        self.contact_label = Label(self.contact_info, text="Contact Information")
        self.contact_label.pack()
        self.phone_number = Label(self.contact_info, text="Phone: ", width=self.paddingX)
        self.phone_number.pack(side=LEFT, fill=X)


        if (not self.phone_number_box is None):
            self.string_phone.set("{}".format(self.phone_text))
            self.phone_number_box = Entry(self.contact_info, textvariable = self.string_phone)
        else:
            self.phone_number_box = Entry(self.contact_info)

        self.phone_number_box.pack(fill=X)
        self.contact_info.pack(fill=X, padx=self.paddingX)

        self.email_frame = Frame(self.main_frame)
        self.email_label = Label(self.email_frame, text="Email:", width=self.paddingX)
        self.email_label.pack(side=LEFT, fill=X)


        if (not self.email_label_box is None):
            self.string_email.set("{}".format(self.email_text))
            self.email_label_box = Entry(self.email_frame, textvariable = self.string_email)
        else:
            self.email_label_box = Entry(self.email_frame)
        self.email_label_box.pack(fill=X)




        self.email_frame.pack(fill=X, padx=self.paddingX)

        self.address_frame = Frame(self.main_frame)
        self.address_label = Label(self.address_frame, text="Address (this summer):", width=self.paddingX)
        self.address_label.pack(side=LEFT, fill=X)

        if (not self.address_label_box is None):
            self.string_address.set("{}".format(self.address_text))
            self.address_label_box = Entry(self.address_frame, textvariable = self.string_address)
        else:
            self.address_label_box = Entry(self.address_frame)



        self.address_label_box.pack(fill=X)
        self.address_frame.pack(fill=X, padx=self.paddingX)
        self.other_frame = Frame(self.main_frame)
        self.major_label = Label(self.other_frame, text="Major:", width=self.paddingX)
        self.major_label.pack(side=LEFT)

        if (not self.major_label_box is None):
            self.string_major.set("{}".format(self.major_text))
            self.major_label_box = Entry(self.other_frame, textvariable = self.string_major)
        else:
            self.major_label_box = Entry(self.other_frame)


        self.major_label_box.pack(fill=X)
        self.other_frame.pack(fill=X, padx=self.paddingX)

        self.year_frame = Frame(self.main_frame)
        self.gradyear_label = Label(self.year_frame, text="Graduation Year:", width=self.paddingX)
        self.gradyear_label.pack(side=LEFT)

        if (not self.gradyear_label_box is None):
            self.string_year.set("{}".format(self.year_text))
            self.gradyear_label_box = Entry(self.year_frame, textvariable = self.string_year)
        else:
            self.gradyear_label_box = Entry(self.year_frame, width=0)

        self.gradyear_label_box.pack(fill=X)
        self.year_frame.pack(fill=X, padx=self.paddingX)
        self.planned_courses_label = Label(self.main_frame, text="Planned Courses Next Semester")
        self.planned_courses_label.pack()
        self.first_row = Frame(self.main_frame)


        self.course_1_frame = Frame(self.first_row)
        self.course_1_number_label = Label(self.course_1_frame, text="Course Number", width=self.paddingX)
        self.course_1_number_label.pack(side=TOP)
        if (not self.course_1_number_box is None):
            self.string_number_1.set("{}".format(self.number_1))
            self.course_1_number_box = Entry(self.course_1_frame, textvariable = self.string_number_1)
        else:
            self.course_1_number_box = Entry(self.course_1_frame)
        self.course_1_number_box.pack(side=TOP)
        self.course_1_name_label = Label(self.course_1_frame, text="Course Name", width=self.paddingX)
        self.course_1_name_label.pack(side=TOP)
        if (not self.course_1_name_box is None):
            self.string_name_1.set("{}".format(self.name_1))
            self.course_1_name_box = Entry(self.course_1_frame, textvariable = self.string_name_1)
        else:
            self.course_1_name_box = Entry(self.course_1_frame)
        self.course_1_name_box.pack(side=TOP)
        self.course_1_number_label = Label(self.course_1_frame, text="# of Credits", width=self.paddingX)
        self.course_1_number_label.pack(side=TOP)
        if (not self.course_1_credits_box is None):
            self.string_credits_1.set("{}".format(self.credits_1))
            self.course_1_credits_box = Entry(self.course_1_frame, textvariable = self.string_credits_1)
        else:
            self.course_1_credits_box = Entry(self.course_1_frame)
        self.course_1_credits_box.pack(side=TOP)
        self.course_1_frame.pack(side=LEFT, padx=self.paddingX)



        self.course_2_frame = Frame(self.first_row)
        self.course_2_number_label = Label(self.course_2_frame, text="Course Number", width=self.paddingX)
        self.course_2_number_label.pack(side=TOP)
        if (not self.course_2_number_box is None):
            self.string_number_2.set("{}".format(self.number_2))
            self.course_2_number_box = Entry(self.course_2_frame, textvariable=self.string_number_2)
        else:
            self.course_2_number_box = Entry(self.course_2_frame)
        self.course_2_number_box.pack(side=TOP)
        self.course_2_name_label = Label(self.course_2_frame, text="Course Name", width=self.paddingX)
        self.course_2_name_label.pack(side=TOP)
        if (not self.course_2_name_box is None):
            self.string_name_2.set("{}".format(self.name_2))
            self.course_2_name_box = Entry(self.course_2_frame, textvariable=self.string_name_2)
        else:
            self.course_2_name_box = Entry(self.course_2_frame)
        self.course_2_name_box.pack(side=TOP)
        self.course_2_number_label = Label(self.course_2_frame, text="# of Credits", width=self.paddingX)
        self.course_2_number_label.pack(side=TOP)
        if (not self.course_2_credits_box is None):
            self.string_credits_2.set("{}".format(self.credits_2))
            self.course_2_credits_box = Entry(self.course_2_frame, textvariable=self.string_credits_2)
        else:
            self.course_2_credits_box = Entry(self.course_2_frame)
        self.course_2_credits_box.pack(side=TOP)
        self.course_2_frame.pack(side=LEFT, padx=self.paddingX)

        self.course_3_frame = Frame(self.first_row)
        self.course_3_number_label = Label(self.course_3_frame, text="Course Number", width=self.paddingX)
        self.course_3_number_label.pack(side=TOP)
        if (not self.course_3_number_box is None):
            self.string_number_3.set("{}".format(self.number_3))
            self.course_3_number_box = Entry(self.course_3_frame, textvariable=self.string_number_3)
        else:
            self.course_3_number_box = Entry(self.course_3_frame)
        self.course_3_number_box.pack(side=TOP)
        self.course_3_name_label = Label(self.course_3_frame, text="Course Name", width=self.paddingX)
        self.course_3_name_label.pack(side=TOP)
        if (not self.course_3_name_box is None):
            self.string_name_3.set("{}".format(self.name_3))
            self.course_3_name_box = Entry(self.course_3_frame, textvariable=self.string_name_3)
        else:
            self.course_3_name_box = Entry(self.course_3_frame)
        self.course_3_name_box.pack(side=TOP)
        self.course_3_number_label = Label(self.course_3_frame, text="# of Credits", width=self.paddingX)
        self.course_3_number_label.pack(side=TOP)
        if (not self.course_3_credits_box is None):
            self.string_credits_3.set("{}".format(self.credits_3))
            self.course_3_credits_box = Entry(self.course_3_frame, textvariable=self.string_credits_3)
        else:
            self.course_3_credits_box = Entry(self.course_3_frame)
        self.course_3_credits_box.pack(side=TOP)
        self.course_3_frame.pack(side=LEFT, padx=self.paddingX)

        self.course_4_frame = Frame(self.first_row)
        self.course_4_number_label = Label(self.course_4_frame, text="Course Number", width=self.paddingX)
        self.course_4_number_label.pack(side=TOP)
        if (not self.course_4_number_box is None):
            self.string_number_4.set("{}".format(self.number_4))
            self.course_4_number_box = Entry(self.course_4_frame, textvariable=self.string_number_4)
        else:
            self.course_4_number_box = Entry(self.course_4_frame)
        self.course_4_number_box.pack(side=TOP)
        self.course_4_name_label = Label(self.course_4_frame, text="Course Name", width=self.paddingX)
        self.course_4_name_label.pack(side=TOP)
        if (not self.course_4_name_box is None):
            self.string_name_4.set("{}".format(self.name_4))
            self.course_4_name_box = Entry(self.course_4_frame, textvariable=self.string_name_4)
        else:
            self.course_4_name_box = Entry(self.course_4_frame)
        self.course_4_name_box.pack(side=TOP)
        self.course_4_number_label = Label(self.course_4_frame, text="# of Credits", width=self.paddingX)
        self.course_4_number_label.pack(side=TOP)
        if (not self.course_4_credits_box is None):
            self.string_credits_4.set("{}".format(self.credits_4))
            self.course_4_credits_box = Entry(self.course_4_frame, textvariable=self.string_credits_4)
        else:
            self.course_4_credits_box = Entry(self.course_4_frame)
        self.course_4_credits_box.pack(side=TOP)
        self.course_4_frame.pack(side=LEFT, padx=self.paddingX)



        self.first_row.pack(fill=X)

        self.gap = Frame(self.main_frame, height=30)
        self.gap.pack(fill=X)

        self.second_row = Frame(self.main_frame)

        self.course_5_frame = Frame(self.second_row)
        self.course_5_number_label = Label(self.course_5_frame, text="Course Number", width=self.paddingX)
        self.course_5_number_label.pack(side=TOP)
        if (not self.course_5_number_box is None):
            self.string_number_5.set("{}".format(self.number_5))
            self.course_5_number_box = Entry(self.course_5_frame, textvariable=self.string_number_5)
        else:
            self.course_5_number_box = Entry(self.course_5_frame)
        self.course_5_number_box.pack(side=TOP)
        self.course_5_name_label = Label(self.course_5_frame, text="Course Name", width=self.paddingX)
        self.course_5_name_label.pack(side=TOP)
        if (not self.course_5_name_box is None):
            self.string_name_5.set("{}".format(self.name_5))
            self.course_5_name_box = Entry(self.course_5_frame, textvariable=self.string_name_5)
        else:
            self.course_5_name_box = Entry(self.course_5_frame)
        self.course_5_name_box.pack(side=TOP)
        self.course_5_number_label = Label(self.course_5_frame, text="# of Credits", width=self.paddingX)
        self.course_5_number_label.pack(side=TOP)
        if (not self.course_5_credits_box is None):
            self.string_credits_5.set("{}".format(self.credits_5))
            self.course_5_credits_box = Entry(self.course_5_frame, textvariable=self.string_credits_5)
        else:
            self.course_5_credits_box = Entry(self.course_5_frame)
        self.course_5_credits_box.pack(side=TOP)
        self.course_5_frame.pack(side=LEFT, padx=self.paddingX)


        self.course_6_frame = Frame(self.second_row)
        self.course_6_number_label = Label(self.course_6_frame, text="Course Number", width=self.paddingX)
        self.course_6_number_label.pack(side=TOP)
        if (not self.course_6_number_box is None):
            self.string_number_6.set("{}".format(self.number_6))
            self.course_6_number_box = Entry(self.course_6_frame, textvariable=self.string_number_6)
        else:
            self.course_6_number_box = Entry(self.course_6_frame)
        self.course_6_number_box.pack(side=TOP)
        self.course_6_name_label = Label(self.course_6_frame, text="Course Name", width=self.paddingX)
        self.course_6_name_label.pack(side=TOP)
        if (not self.course_6_name_box is None):
            self.string_name_6.set("{}".format(self.name_6))
            self.course_6_name_box = Entry(self.course_6_frame, textvariable=self.string_name_6)
        else:
            self.course_6_name_box = Entry(self.course_6_frame)
        self.course_6_name_box.pack(side=TOP)
        self.course_6_number_label = Label(self.course_6_frame, text="# of Credits", width=self.paddingX)
        self.course_6_number_label.pack(side=TOP)
        if (not self.course_6_credits_box is None):
            self.string_credits_6.set("{}".format(self.credits_6))
            self.course_6_credits_box = Entry(self.course_6_frame, textvariable=self.string_credits_6)
        else:
            self.course_6_credits_box = Entry(self.course_6_frame)
        self.course_6_credits_box.pack(side=TOP)
        self.course_6_frame.pack(side=LEFT, padx=self.paddingX)



        self.course_7_frame = Frame(self.second_row)
        self.course_7_number_label = Label(self.course_7_frame, text="Course Number", width=self.paddingX)
        self.course_7_number_label.pack(side=TOP)
        if (not self.course_7_number_box is None):
            self.string_number_7.set("{}".format(self.number_7))
            self.course_7_number_box = Entry(self.course_7_frame, textvariable=self.string_number_7)
        else:
            self.course_7_number_box = Entry(self.course_7_frame)
        self.course_7_number_box.pack(side=TOP)
        self.course_7_name_label = Label(self.course_7_frame, text="Course Name", width=self.paddingX)
        self.course_7_name_label.pack(side=TOP)
        if (not self.course_7_name_box is None):
            self.string_name_7.set("{}".format(self.name_7))
            self.course_7_name_box = Entry(self.course_7_frame, textvariable=self.string_name_7)
        else:
            self.course_7_name_box = Entry(self.course_7_frame)
        self.course_7_name_box.pack(side=TOP)
        self.course_7_number_label = Label(self.course_7_frame, text="# of Credits", width=self.paddingX)
        self.course_7_number_label.pack(side=TOP)
        if (not self.course_7_credits_box is None):
            self.string_credits_7.set("{}".format(self.credits_7))
            self.course_7_credits_box = Entry(self.course_7_frame, textvariable=self.string_credits_7)
        else:
            self.course_7_credits_box = Entry(self.course_7_frame)
        self.course_7_credits_box.pack(side=TOP)
        self.course_7_frame.pack(side=LEFT, padx=self.paddingX)

        self.course_8_frame = Frame(self.second_row)
        self.course_8_number_label = Label(self.course_8_frame, text="Course Number", width=self.paddingX)
        self.course_8_number_label.pack(side=TOP)
        if (not self.course_8_number_box is None):
            self.string_number_8.set("{}".format(self.number_8))
            self.course_8_number_box = Entry(self.course_8_frame, textvariable=self.string_number_8)
        else:
            self.course_8_number_box = Entry(self.course_8_frame)
        self.course_8_number_box.pack(side=TOP)
        self.course_8_name_label = Label(self.course_8_frame, text="Course Name", width=self.paddingX)
        self.course_8_name_label.pack(side=TOP)
        if (not self.course_8_name_box is None):
            self.string_name_8.set("{}".format(self.name_8))
            self.course_8_name_box = Entry(self.course_8_frame, textvariable=self.string_name_8)
        else:
            self.course_8_name_box = Entry(self.course_8_frame)
        self.course_8_name_box.pack(side=TOP)
        self.course_8_number_label = Label(self.course_8_frame, text="# of Credits", width=self.paddingX)
        self.course_8_number_label.pack(side=TOP)
        if (not self.course_8_credits_box is None):
            self.string_credits_8.set("{}".format(self.credits_8))
            self.course_8_credits_box = Entry(self.course_8_frame, textvariable=self.string_credits_8)
        else:
            self.course_8_credits_box = Entry(self.course_8_frame)
        self.course_8_credits_box.pack(side=TOP)
        self.course_8_frame.pack(side=LEFT, padx=self.paddingX)


        self.second_row.pack(fill=X)
        self.gap_2 = Label(self.main_frame, height=1)
        self.gap_2.pack(fill=X)

        self.committee_label = Label(self.main_frame, text="Committees")
        self.committee_label_2 = Label(self.main_frame, text="Select and number up to 3 with 1 being your first choice")
        self.committee_label.pack(fill=X)
        self.committee_label_2.pack(fill=X)

        self.committees_row_1 = Frame(self.main_frame)
        self.d7_frame = Frame(self.committees_row_1)
        self.d7_label = Label(self.d7_frame, text="D7", width=self.paddingX + 10)
        self.d7_label.pack(side=TOP)
        if (not self.d7_box is None):
            self.string_d7.set("{}".format(self.d7_text))
            self.d7_box = Entry(self.d7_frame, textvariable = self.string_d7)
        else:
            self.d7_box = Entry(self.d7_frame)
        self.d7_box.pack(side=TOP)
        self.d7_frame.pack(side=LEFT, padx=self.paddingX, fill=X)

        self.fundraising_frame = Frame(self.committees_row_1)
        self.fundraising_label = Label(self.fundraising_frame, text="Fundraising", width=self.paddingX + 10)
        self.fundraising_label.pack(side=TOP)
        if (not self.fundraising_box is None):
            self.string_fundraising.set("{}".format(self.fundraising_text))
            self.fundraising_box = Entry(self.fundraising_frame, textvariable = self.string_fundraising)
        else:
            self.fundraising_box = Entry(self.fundraising_frame)
        self.fundraising_box.pack(side=TOP)

        self.fundraising_box.pack(side=TOP)
        self.fundraising_frame.pack(side=LEFT, padx=self.paddingX, fill=X)


        self.hospitality_frame = Frame(self.committees_row_1)
        self.hospitality_label = Label(self.hospitality_frame, text="Hospitality", width=self.paddingX + 10)
        self.hospitality_label.pack(side=TOP)
        if (not self.hospitality_box is None):
            self.string_hospitality.set("{}".format(self.hospitality_text))
            self.hospitality_box = Entry(self.hospitality_frame, textvariable = self.string_hospitality)
        else:
            self.hospitality_box = Entry(self.hospitality_frame)
        self.hospitality_box.pack(side=TOP)
        self.hospitality_box.pack(side=TOP)
        self.hospitality_frame.pack(side=LEFT, padx=self.paddingX, fill=X)

        self.committees_row_1.pack(fill=X)
        self.committees_row_2 = Frame(self.main_frame)

        self.sports_frame = Frame(self.committees_row_2)
        self.sports_label = Label(self.sports_frame, text="Sports", width=self.paddingX + 10)
        self.sports_label.pack(side=TOP)
        if (not self.sports_box is None):
            self.string_sports.set("{}".format(self.sports_text))
            self.sports_box = Entry(self.sports_frame, textvariable = self.string_sports)
        else:
            self.sports_box = Entry(self.sports_frame)
        self.sports_box.pack(side=TOP)
        self.sports_box.pack(side=TOP)
        self.sports_frame.pack(side=LEFT, padx=self.paddingX, fill=X)
        self.promotions_frame = Frame(self.committees_row_2)
        self.promotions_label = Label(self.promotions_frame, text="Promotions", width=self.paddingX + 10)
        self.promotions_label.pack(side=TOP)
        if (not self.promotions_box is None):
            self.string_promotions.set("{}".format(self.promotions_text))
            self.promotions_box = Entry(self.promotions_frame, textvariable = self.string_promotions)
        else:
            self.promotions_box = Entry(self.promotions_frame)
        self.promotions_box.pack(side=TOP)
        self.promotions_box.pack(side=TOP)
        self.promotions_frame.pack(side=LEFT, padx=self.paddingX, fill=X)

        self.service_frame = Frame(self.committees_row_2)
        self.service_label = Label(self.service_frame, text="Service", width=self.paddingX + 10)
        self.service_label.pack(side=TOP)
        if (not self.service_box is None):
            self.string_service.set("{}".format(self.service_text))
            self.service_box = Entry(self.service_frame, textvariable = self.string_service)
        else:
            self.service_box = Entry(self.service_frame)
        self.service_box.pack(side=TOP)
        self.service_box.pack(side=TOP)
        self.service_frame.pack(side=LEFT, padx=self.paddingX, fill=X)
        self.committees_row_2.pack(fill=X)
        self.committees_row_3 = Frame(self.main_frame)

        self.web_frame = Frame(self.committees_row_3)
        self.web_label = Label(self.web_frame, text="Web", width=self.paddingX + 10)
        self.web_label.pack(side=TOP)
        if (not self.web_box is None):
            self.string_web.set("{}".format(self.web_text))
            self.web_box = Entry(self.web_frame, textvariable = self.string_web)
        else:
            self.web_box = Entry(self.web_frame)
        self.web_box.pack(side=TOP)
        self.web_box.pack(side=TOP)
        self.web_frame.pack(side=LEFT, padx=self.paddingX, fill=X)

        self.culture_frame = Frame(self.committees_row_3)
        self.culture_label = Label(self.culture_frame, text="Culture", width=self.paddingX + 10)
        self.culture_label.pack(side=TOP)
        if (not self.culture_box is None):
            self.string_culture.set("{}".format(self.culture_text))
            self.culture_box = Entry(self.culture_frame, textvariable = self.string_culture)
        else:
            self.culture_box = Entry(self.culture_frame)
        self.culture_box.pack(side=TOP)
        self.culture_box.pack(side=TOP)
        self.culture_frame.pack(side=LEFT, padx=self.paddingX, fill=X)

        self.events_frame = Frame(self.committees_row_3)
        self.events_label = Label(self.events_frame, text="Events", width=self.paddingX + 10)
        self.events_label.pack(side=TOP)
        if (not self.events_box is None):
            self.string_events.set("{}".format(self.events_text))
            self.events_box = Entry(self.events_frame, textvariable = self.string_events)
        else:
            self.events_box = Entry(self.events_frame)
        self.events_box.pack(side=TOP)
        self.events_box.pack(side=TOP)
        self.events_frame.pack(side=LEFT, padx=self.paddingX, fill=X)

        self.committees_row_3.pack(fill=X)

        self.gap_3 = Label(self.main_frame, height=1)
        self.gap_3.pack(fill=X)
        question_button = Button(self.main_frame, text = "View Questions ->", pady = 2, command = partial(self.view_questions, self.main_frame, master))
        #back_button = Button(self.main_frame, text = "<-Back", command = partial(self.view_home, master, self.main_frame))
        #back_button.pack()
        self.main_frame.pack()
        question_button.pack()

    def view_questions(self, deleted_frame, master):
        self.name_text = self.name.get()
        self.phone_text = self.phone_number_box.get()
        self.email_text = self.email_label_box.get()
        self.address_text = self.address_label_box.get()
        self.major_text = self.major_label_box.get()
        self.year_text = self.gradyear_label_box.get()

        self.number_1 = self.course_1_number_box.get()
        self.name_1 = self.course_1_name_box.get()
        self.credits_1 = self.course_1_credits_box.get()
        self.course_1 = course(self.number_1, self.name_1, self.credits_1)

        self.number_2 = self.course_2_number_box.get()
        self.name_2 = self.course_2_name_box.get()
        self.credits_2 = self.course_2_credits_box.get()
        self.course_two = course(self.number_2, self.name_2, self.credits_2)

        self.number_3 = self.course_3_number_box.get()
        self.name_3 = self.course_3_name_box.get()
        self.credits_3 = self.course_3_credits_box.get()
        self.course_3 = course(self.number_3, self.name_3, self.credits_3)

        self.number_4 = self.course_4_number_box.get()
        self.name_4 = self.course_4_name_box.get()
        self.credits_4 = self.course_4_credits_box.get()
        self.course_4 = course(self.number_4, self.name_4, self.credits_4)

        self.number_5 = self.course_5_number_box.get()
        self.name_5 = self.course_5_name_box.get()
        self.credits_5 = self.course_5_credits_box.get()
        self.course_5 = course(self.number_5, self.name_5, self.credits_5)

        self.number_7 = self.course_7_number_box.get()
        self.name_7 = self.course_7_name_box.get()
        self.credits_7 = self.course_7_credits_box.get()
        self.course_7 = course(self.number_7, self.name_7, self.credits_7)

        self.number_8 = self.course_8_number_box.get()
        self.name_8 = self.course_8_name_box.get()
        self.credits_8 = self.course_8_credits_box.get()
        self.course_8 = course(self.number_8, self.name_8, self.credits_8)

        self.number_6 = self.course_6_number_box.get()
        self.name_6 = self.course_6_name_box.get()
        self.credits_6 = self.course_6_credits_box.get()
        self.course_6 = course(self.number_6, self.name_6, self.credits_6)
        self.new_course_list.add(self.course_1)
        self.new_course_list.add(self.course_two)
        self.new_course_list.add(self.course_3)
        self.new_course_list.add(self.course_4)
        self.new_course_list.add(self.course_5)
        self.new_course_list.add(self.course_6)
        self.new_course_list.add(self.course_7)
        self.new_course_list.add(self.course_8)
        print(self.new_course_list.num_entries)


        self.new_basic = basic(self.name_text, self.major_text, self.year_text)
        self.new_contact_info = contact_info(self.phone_text, self.email_text, self.address_text)

        self.d7_text = self.d7_box.get()
        self.fundraising_text = self.fundraising_box.get()
        self.hospitality_text = self.hospitality_box.get()
        self.sports_text = self.sports_box.get()
        self.promotions_text = self.promotions_box.get()
        self.service_text = self.service_box.get()
        self.web_text = self.web_box.get()
        self.culture_text = self.culture_box.get()
        self.events_text = self.events_box.get()

        print(self.promotions_text)

        deleted_frame.destroy()
        self.new_main_frame = Frame(master)
        self.head_frame = Frame(self.new_main_frame)
        self.head_label = Label(self.head_frame,
                                text="2020-2021 FASA Officer Committees Application", width=80)  # , height = 5)
        self.head_label.pack(fill=X)
        self.head_frame.pack(fill=X, padx=100, pady=self.paddingX)

        self.question_1_frame = Frame(self.head_frame, padx=10, width=80, height=100)
        self.question_1_label = Label(self.question_1_frame, text="Question 1")


        if (self.question_1_response is not None):
            self.string_question_1.set("{}".format(self.question_1_text))
            self.question_1_response = Text(self.question_1_frame, height=5, width=40, font=('Helvetica'))
            self.question_1_response.insert(1.0, "{}".format(self.question_1_text))
        else:
            self.question_1_response = Text(self.question_1_frame, height=5, width=40, font=('Helvetica'))



        self.question_1_label.pack(fill=X)
        self.question_1_response.pack(fill=X)
        self.question_1_frame.pack(fill=X, padx=2, pady=10)
        self.question_1_label.pack(fill = X)
        self.question_1_frame.pack(fill = X)

        self.question_2_frame = Frame(self.head_frame, padx=10, width=80, height=100)
        self.question_2_label = Label(self.question_2_frame, text="Question 2")
        if (self.question_2_response is not None):
            self.string_question_2.set("{}".format(self.question_2_text))
            self.question_2_response = Text(self.question_2_frame, height=5, width=40, font=('Helvetica'))
            self.question_2_response.insert(1.0, "{}".format(self.question_2_text))
        else:
            self.question_2_response = Text(self.question_2_frame, height=5, width=40, font=('Helvetica'))
        self.question_2_label.pack(fill=X)
        self.question_2_response.pack(fill=X)
        self.question_2_frame.pack(fill=X, padx=2, pady=10)
        self.question_2_label.pack(fill=X)
        self.question_2_frame.pack(fill=X)
        self.question_3_frame = Frame(self.head_frame, padx=10, width=80, height=100)
        self.question_3_label = Label(self.question_3_frame, text="Question 3")
        if (self.question_3_response is not None):
            self.string_question_3.set("{}".format(self.question_3_text))
            self.question_3_response = Text(self.question_3_frame, height=5, width=40, font=('Helvetica'))
            self.question_3_response.insert(1.0, "{}".format(self.question_3_text))
            print(self.string_question_3.get())
        else:
            self.question_3_response = Text(self.question_3_frame, height=5, width=40, font=('Helvetica'))
        self.question_3_label.pack(fill=X)
        self.question_3_response.pack(fill=X)
        self.question_3_frame.pack(fill=X, padx=2, pady=10)
        self.question_3_label.pack(fill=X)
        self.question_3_frame.pack(fill=X)

        self.question_4_frame = Frame(self.head_frame, padx=10, width=80, height=100)
        self.question_4_label = Label(self.question_4_frame, text="Question 4")


        #self.question_4_response = Text(self.question_4_frame, height=5, width=40, font=('Helvetica'))
        if (self.question_4_response is not None):
            self.string_question_4.set("{}".format(self.question_4_text))
            self.question_4_response = Text(self.question_4_frame, height=5, width=40, font=('Helvetica'))
            self.question_4_response.insert(1.0, "{}".format(self.question_4_text))
            print(self.string_question_4.get())
        else:
            self.question_4_response = Text(self.question_4_frame, height=5, width=40, font=('Helvetica'))


        self.question_4_label.pack(fill=X)
        self.question_4_response.pack(fill=X)
        self.question_4_frame.pack(fill=X, padx=2, pady=10)
        self.question_4_label.pack(fill=X)
        self.question_4_frame.pack(fill=X)

        self.back_button = Button(self.new_main_frame, text = "<-Back", command = partial(self.view_application, master, self.new_main_frame, self.new_main_frame))
        self.back_button.pack()
        self.submit_button = Button(self.new_main_frame, text = "Submit", command = partial(self.submit, self.new_main_frame, master))
        self.submit_button.pack()
        self.new_main_frame.pack()

    def submit(self, deleted_frame_2, master):
        self.submitted = True
        self.new_questions.set_one(self.question_1_text)
        self.new_questions.set_two(self.question_2_text)
        self.new_questions.set_three(self.question_3_text)
        self.new_questions.set_four(self.question_4_text)

        print(self.question_1_text)

        self.new_applicant.set_basic(self.new_basic)
        self.new_applicant.set_questions(self.new_questions)
        self.new_applicant.set_course_list(self.new_course_list)
        self.new_applicant.set_course_info(self.new_contact_info)

        self.new_applicant_list.add(self.new_applicant)
        self.insert_applicant(self.new_applicant)

        deleted_frame_2.destroy()
        self.new_main_frame = Frame(master)
        self.head_frame = Frame(self.new_main_frame)
        self.head_label = Label(self.head_frame,
                                text="2020-2021 FASA Officer Committees Application", width=80)  # , height = 5)
        self.head_label.pack(fill=X)
        self.head_frame.pack(fill=X, padx=100, pady=self.paddingX)
        self.exit_label = Label(self.head_frame, text = "Your applicant has been submitted")
        self.exit_label.pack(fill = X)
        self.home_button = Button(self.new_main_frame, text = "Go Home", command = partial(self.view_home, master, self.new_main_frame))
        self.home_button.pack()
        self.new_main_frame.pack(fill = X)







root = Tk()
new_window = window(root);
root.mainloop()

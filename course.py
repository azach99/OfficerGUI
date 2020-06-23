class course:
    def __init__(self, number, name, credits):
        self.number = number
        self.name = name
        self.credits = credits
    #@property
    def get_number(self):
        return self.number
    #@property
    def get_name(self):
        return self.name
    #@property
    def get_credits(self):
        return self.credits
    #@property.setter
    def set_number(self, new_number):
        self.number = new_number
    #@property.setter
    def set_name(self, new_name):
        self.name = new_name
    #@property.setter
    def set_credits(self, new_credits):
        self.credits = new_credits;
    def __str__(self):
        return "{} {} {}".format(self.number, self.name, self.credits)
    '''
    def equals(self, course):
        if (self == course):
            return True
        if (course == None):
            return False
        if (self.__class__ == course.__class__):
            new_course = course(course)
            return 
     '''
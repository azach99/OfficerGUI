class course_list:
    def __init__(self):
        self.list = []
        self.num_entries = 0;
    def get_num_entries(self):
        return self.num_entries
    def is_empty(self):
        return self.num_entries == 0
    def add(self, course):
        if (course is None):
            return False
        else:
            self.list.append(course)
            self.num_entries += 1
            return True
    def remove(self, course):
        if (course is None):
            return False
        if (course in self.list):
            self.list.remove(course)
            self.num_entries -= 1
            return True
        else:
            return False
    def clear(self):
        if (not self.is_empty()):
            self.list.clear()
            self.num_entries = len(self.list)
    def total_credits(self):
        out_sum = 0;
        for course in self.list:
            out_sum = out_sum + course.get_credits()
        return out_sum

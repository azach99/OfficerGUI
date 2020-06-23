class applicant_list:

    def __init__(self):
        self.list = []
        self.num_of_entries = 0

    def get_num_of_entries(self):
        return self.num_of_entries

    def is_empty(self):
        return self.num_of_entries == 0

    def add(self, applicant):
        if applicant is None:
            return False
        else:
            self.list.append(applicant)
            self.num_of_entries += 1
            return True

    def remove(self, applicant):
        if (applicant is None):
            return False
        if (applicant in self.list):
            self.list.remove(applicant)
            self.num_of_entries -= 1
            return True
        else:
            return False
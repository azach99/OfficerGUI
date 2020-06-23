class basic:
    def __init__(self, name, major, year):
        self.name = name
        self.major = major
        self.year = year

    def get_name(self):
        return self.name

    def get_major(self):
        return self.major

    def get_year(self):
        return self.year

    def set_name(self, name):
        self.name = name

    def set_major(self, major):
        self.major = major

    def set_year(self, year):
        self.year = year

    def __str__(self):
        return "{} {} {}".format(self.name, self.major, self.year)

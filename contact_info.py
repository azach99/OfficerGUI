class contact_info:
    def __init__(self, phone, email, address):
        self.phone = phone
        self.email = email
        self.address = address
    def get_phone(self):
        return self.phone
    def get_email(self):
        return self.email
    def get_address(self):
        return self.address
    def set_address(self, address):
        self.address = address
    def set_email(self, email):
        self.email = email
    def set_phone(self, phone):
        self.phone = phone
    def __str__(self):
        return "{} {} {}".format(self.phone, self.email, self.address)
    
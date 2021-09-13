class User(object):

    def __init__(self, lastname, firstname, dob, pob, email, pwd):
        self.lastname = lastname
        self.firstname = firstname
        self.dateOfBirth = dob
        self.placeOfBirth = pob
        self.email = email
        self.password = pwd

    def set_lastname(self, lastname):
        self.lastname = lastname

    def get_lastname(self):
        return self.lastname

    def set_firstname(self, firstname):
        self.firstname = firstname

    def get_firstname(self):
        return self.firstname

    def set_dob(self, day, month, year):
        self.dateOfBirth = [day, month, year]

    def get_dob(self):
        return self.dateOfBirth

    def set_pob(self, country):
        self.placeOfBirth = country

    def get_pob(self):
        return self.placeOfBirth

    def set_email(self, email):
        self.email = email

    def get_email(self):
        return self.email

    def set_pwd(self, pwd):
        self.password = pwd

    def get_pwd(self):
        return self.password
    
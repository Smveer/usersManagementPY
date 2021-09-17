from functions import *


class User(object):

    def __init__(self, lastname, firstname, day, month, year, pob, email):
        self.lastname = lastname
        self.firstname = firstname
        verify_date(day, month, year)
        self.dateOfBirth = [day, month, year]
        self.placeOfBirth = pob
        verify_email(email)
        self.email = email
        self.password = generate_pwd()

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

    def set_pwd(self):
        self.password = generate_pwd()

    def get_pwd(self):
        return self.password

    def get_id(self):
        return self.firstname[0] + self.lastname

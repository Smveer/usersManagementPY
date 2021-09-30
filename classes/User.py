from functions import *
from dbFunctions import *
import sys

sys.path.append("../../usersManagementPY")


class User(object):

    def __init__(self, lastname, firstname, dateBirth, pob, email):
        self.lastname = lastname
        self.firstname = firstname
        while True:
            if verify_date(dateBirth):
                self.dateOfBirth = dateBirth
                break
            else:
                dateBirth = ask_date_birth()
        self.placeOfBirth = pob
        while True:
            if verify_email(email):
                self.email = email
                break
            else:
                email = ask_email()
        self.password = generate_pwd_hash()
        self.login = attribute_login(self.firstname, self.lastname)

    def set_lastname(self, lastname):
        self.lastname = lastname

    def get_lastname(self):
        return self.lastname

    def set_firstname(self, firstname):
        self.firstname = firstname

    def get_firstname(self):
        return self.firstname

    def set_dob(self, dateBirth):
        self.dateOfBirth = dateBirth

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

    def random_pwd(self):
        self.password = generate_pwd_hash()

    def set_pwd(self, pwd):
        self.password = create_pwd_hash(pwd)

    def get_pwd(self):
        return self.password

    def get_login(self):
        return self.login

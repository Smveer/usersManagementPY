from functions import *
from dbFunctions import *
import sys

from functions import create_pwd_hash

sys.path.append("../../usersManagementPY")


class User(object):

    def __init__(self, lastname, firstname, dateBirth, pob, email):
        while True:
            if check_string(lastname):
                self.lastname = check_string(lastname)
                break
            else:
                lastname = ask_lastname()
        while True:
            if check_string(firstname):
                self.firstname = check_string(firstname)
                break
            else:
                firstname = ask_firstname()
        while True:
            if verify_date(dateBirth):
                self.dateOfBirth = dateBirth
                break
            else:
                dateBirth = ask_date_birth()
        while True:
            if check_string(pob):
                self.placeOfBirth = check_string(pob)
                break
            else:
                pob = ask_country()
        while True:
            if verify_email(email):
                self.email = email
                break
            else:
                email = ask_email()
        self.password = generate_pwd_hash()
        self.login = attribute_login(self.firstname, self.lastname)

    def set_lastname(self, lastname):
        while True:
            if check_string(lastname):
                self.lastname = check_string(lastname)
                break
            else:
                lastname = ask_lastname()

    def get_lastname(self):
        return self.lastname

    def set_firstname(self, firstname):
        while True:
            if check_string(firstname):
                self.firstname = check_string(firstname)
                break
            else:
                firstname = ask_firstname()

    def get_firstname(self):
        return self.firstname

    def set_dob(self, dateBirth):
        while True:
            if verify_date(dateBirth):
                self.dateOfBirth = dateBirth
                break
            else:
                dateBirth = ask_date_birth()

    def get_dob(self):
        return self.dateOfBirth

    def set_pob(self, country):
        while True:
            if check_string(country):
                self.placeOfBirth = check_string(country)
                break
            else:
                country = ask_country()

    def get_pob(self):
        return self.placeOfBirth

    def set_email(self, email):
        while True:
            if verify_email(email):
                self.email = email
                break
            else:
                email = ask_email()

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

    def set_login(self):
        self.login = attribute_login(self.firstname, self.lastname)
        
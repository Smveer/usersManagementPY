import functions
from dbFunctions import *
import sys

sys.path.append("../../usersManagementPY")


class User(object):

    def __init__(self, lastname, firstname, dateBirth, pob, email):
        while True:
            if functions.check_string(lastname):
                self.lastname = functions.check_string(lastname)
                break
            else:
                lastname = functions.ask_lastname()
        while True:
            if functions.check_string(firstname):
                self.firstname = functions.check_string(firstname)
                break
            else:
                firstname = functions.ask_firstname()
        while True:
            if functions.verify_date(dateBirth):
                self.dateOfBirth = dateBirth
                break
            else:
                dateBirth = functions.ask_date_birth()
        while True:
            if functions.check_string(pob):
                self.placeOfBirth = functions.check_string(pob)
                break
            else:
                pob = functions.ask_country()
        while True:
            if functions.verify_email(email):
                self.email = email
                break
            else:
                email = functions.ask_email()
        self.password = ""
        self.login = functions.attribute_login(self.firstname, self.lastname)
        self.id = ""
        self.departement = ""

    def set_lastname(self, lastname):
        while True:
            if functions.check_string(lastname):
                self.lastname = functions.check_string(lastname)
                self.set_login()
                break
            else:
                lastname = functions.ask_lastname()

    def get_lastname(self):
        return self.lastname

    def set_firstname(self, firstname):
        while True:
            if functions.check_string(firstname):
                self.firstname = functions.check_string(firstname)
                self.set_login()
                break
            else:
                firstname = functions.ask_firstname()

    def get_firstname(self):
        return self.firstname

    def set_dob(self, dateBirth):
        while True:
            if functions.verify_date(dateBirth):
                self.dateOfBirth = dateBirth
                break
            else:
                dateBirth = functions.ask_date_birth()

    def get_dob(self):
        return self.dateOfBirth

    def set_pob(self, country):
        while True:
            if functions.check_string(country):
                self.placeOfBirth = functions.check_string(country)
                break
            else:
                country = functions.ask_country()

    def get_pob(self):
        return self.placeOfBirth

    def set_email(self, email):
        while True:
            if functions.verify_email(email):
                if if_email_exists(email):
                    print("Email already exists")
                    return False
                else:
                    self.email = email
                    break
            else:
                email = functions.ask_email()

    def get_email(self):
        return self.email

    def set_random_pwd(self):
        self.password = functions.generate_pwd_hash()

    def set_pwd(self, pwd):
        self.password = functions.create_pwd_hash(pwd)

    def get_pwd(self):
        return self.password

    def get_login(self):
        return self.login

    def set_login(self):
        self.login = functions.attribute_login(self.firstname, self.lastname)
        print("Your new login is " + str(self.login))

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_departement(self):
        return self.departement

    def set_departement(self, departement):
        self.departement = departement
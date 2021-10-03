import functions
from dbFunctions import *
import sys

sys.path.append("../../usersManagementPY")


class User(object):

    def __init__(self, lastname, firstname, dateBirth, pob, email):

        # Check lastname (no useless space and no empty string)
        while True:
            if functions.check_string(lastname):
                self.lastname = functions.check_string(lastname)
                break
            else:
                lastname = functions.ask_lastname()

        # Check firstname (no useless space and no empty string)
        while True:
            if functions.check_string(firstname):
                self.firstname = functions.check_string(firstname)
                break
            else:
                firstname = functions.ask_firstname()

        # Check date of birth (if correct format and passed date)
        while True:
            if functions.verify_date(dateBirth):
                self.dateOfBirth = dateBirth
                break
            else:
                dateBirth = functions.ask_date_birth()

        # Check lastname (no useless space and no empty string)
        while True:
            if functions.check_string(pob):
                self.placeOfBirth = functions.check_string(pob)
                break
            else:
                pob = functions.ask_country()

        # Check email (if correct format and if not already exists)
        while True:
            if functions.verify_email(email):
                self.email = email
                break
            else:
                email = functions.ask_email()

        self.password = ""

        self.login = functions.attribute_login(self.firstname, self.lastname) #Give unique login

        self.id = ""

        self.departement = ""

    # set lastname after checking (no useless space and no empty string)
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

    # set lastname after checking (no useless space and no empty string)
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

   # set date of birth (with corect format)
    def set_dob(self, dateBirth):
        while True:
            if functions.verify_date(dateBirth):
                self.dateOfBirth = dateBirth
                break
            else:
                dateBirth = functions.ask_date_birth()

    def get_dob(self):
        return self.dateOfBirth

    # set country
    def set_pob(self, country):
        while True:
            if functions.check_string(country):
                self.placeOfBirth = functions.check_string(country)
                break
            else:
                country = functions.ask_country()

    def get_pob(self):
        return self.placeOfBirth

    # set email
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

    # set random password
    def set_random_pwd(self):
        self.password = functions.generate_pwd_hash()
        if self.id == "":
            "New user"
        else:
            update_pwd(self.password, self.id)

    # set password
    def set_pwd(self, pwd):
        self.password = functions.create_pwd_hash(pwd)
        if self.id == "":
            "New user"
        else:
            update_pwd(self.password, self.id)

    def get_pwd(self):
        return self.password

    def get_login(self):
        return self.login

    # set login
    def set_login(self):
        self.login = functions.attribute_login(self.firstname, self.lastname)
        print("Your new login is " + str(self.login))

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_departement(self):
        return self.departement

    # set department
    def set_departement(self, departement):
        self.departement = departement

    # search email
    def search_email(self, email):
        while True:
            if functions.verify_email(email):
                users = search_by_email(email)
                functions.show_user(users)
                break
            else:
                email = functions.ask_email()

    # search date of birth
    def search_dob(self, dob):
        while True:
            if functions.verify_date(dob):
                users = search_by_dob(dob)
                functions.show_user(users)
                break
            else:
                dob = functions.ask_date_birth()

    # search place of birth
    def search_pob(self, pob):
        while True:
            if functions.check_string(pob):
                users = search_by_cob(functions.check_string(pob))
                functions.show_user(users)
                break
            else:
                pob = functions.ask_country()

    # search lastname
    def search_lastname(self, lastname):
        while True:
            if functions.check_string(lastname):
                users = search_by_lastname(functions.check_string(lastname))
                functions.show_user(users)
                break
            else:
                lastname = functions.ask_lastname()

    # search firstname
    def search_firstname(self, firstname):
        while True:
            if functions.check_string(firstname):
                users = search_by_firstname(functions.check_string(firstname))
                functions.show_user(users)
                break
            else:
                firstname = functions.ask_lastname()
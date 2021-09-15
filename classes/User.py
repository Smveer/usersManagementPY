class User(object):

    def __init__(self, lastname, firstname, dob, pob, email):
        self.lastname = lastname
        self.firstname = firstname
        self.dateOfBirth = dob
        self.placeOfBirth = pob
        self.email = email



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

    def get_id(self):
        return self.firstname[0] + self.lastname


nom = input("nom:")
prenom = input("prenom:")
dateNaissance = []
dateNaissance.append(int(input("day:")))
dateNaissance.append(int(input("month:")))
dateNaissance.append(int(input("year:")))
pays = input("pays:")
email = input("nom:")

moi = User(nom, prenom, dateNaissance , pays, email)
print(moi.get_id())
print(moi.get_dob())
print(moi.get_email())

import string
from random import *
allcharactere = string.ascii_letters+string.digits+string.punctuation
pwd= "".join(choice(allcharactere ) for x in range(randint(8, 20)))
print("Your Password is: ", pwd)
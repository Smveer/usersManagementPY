import sys

from functions import create_user

sys.path.append("../../usersManagementPY")

from classes.User import *

nom = input("nom:")
prenom = input("prenom:")
dateNaissance =  input("date de naissance:")
pays = input("pays:")
email = input("email:")

moi = User(nom, prenom, dateNaissance, pays, email)
#print(moi.get_login())
#print(moi.get_dob())
#print(moi.get_email())
#print("------------------------------------------------")
#print(moi.get_pwd())
#moi.random_pwd()
#print(moi.get_pwd())

create_user(moi)


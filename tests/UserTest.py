import sys
sys.path.append("../../usersManagementPY")

from classes.User import *

nom = input("nom:")
prenom = input("prenom:")
day = int(input("day:"))
month = int(input("month:"))
year = int(input("year:"))
pays = input("pays:")
email = input("email:")

moi = User(nom, prenom, day, month, year, pays, email)
print(moi.get_id())
print(moi.get_dob())
print(moi.get_email())
print("ok")
print(moi.get_pwd())
moi.set_pwd()
print(moi.get_pwd())


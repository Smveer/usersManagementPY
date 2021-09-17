from classes.User import *

nom = input("nom:")
prenom = input("prenom:")
dateNaissance = []
dateNaissance.append(int(input("day:")))
dateNaissance.append(int(input("month:")))
dateNaissance.append(int(input("year:")))
pays = input("pays:")
email = input("email:")

moi = User(nom, prenom, dateNaissance, pays, email)
print(moi.get_id())
print(moi.get_dob())
print(moi.get_email())
print("ok")
print(moi.get_pwd())
moi.set_pwd()
print(moi.get_pwd())


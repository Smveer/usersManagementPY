import re
import random
import string
import hashlib
import datetime
from datetime import date, timedelta
import calendar
import sys

from classes.Admin import Admin
from classes.Worker import Worker

sys.path.append("../../usersManagementPY")
from classes.User import *
from dbFunctions import *


# remove useless spaces (before & after) and capitalize string
def check_string(striing):
    if len(striing.strip()) == 0:
        return False
    else:
        return striing.strip().capitalize()


# verification mail
def verify_email(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if re.search(regex, email):
        return True
    else:
        return False


# password expire 1 month
def set_pwd_expiry():
    now = datetime.datetime.now()
    now = datetime.datetime.now()
    end = now + datetime.timedelta(days=31)
    return end.strftime("%Y-%m-%d")


# verification password expire 1 month uk model & user can't log when the password is expired he must change
def verify_expiry(id):
    user = get_user_with_id(id)
    if (str(user[0]["userPasswordExpiry"]) != "None"):
        splited_date = str(user[0]["userPasswordExpiry"]).split('-')
        expiry_date = str(splited_date[2]) + "-" + str(splited_date[1]) + "-" + str(splited_date[0])
        if verify_date(expiry_date):
            return False
        else:
            return True
    else:
        return False


# set password condition
def verify_pwd_validity(pwd):
    print("Your password must contain at least:\n"
          "8 characters,\n"
          "1 lowercase letter,\n"
          "1 capital letter,\n"
          "1 digit\n")
    lower, upper, special, digit = 0, 0, 0, 0
    if len(pwd) >= 8:
        for character in pwd:
            if character.isupper():
                upper += 1
            if character.islower():
                lower += 1
            if character.isdigit():
                digit += 1
            for punctuation in string.punctuation:
                if character == punctuation:
                    special += 1
    else:
        print("Password should be more than 8 characters")
        return False
    if lower >= 1 and upper >= 1 and special >= 1 and digit >= 1:
        print("Valid Password")
        return True
    else:
        print("Password not valid. Please try again")
        return False


# password encryption sha512
def create_hash(pwd):
    salt = "project"
    hashed = hashlib.sha512(pwd.encode() + salt.encode()).hexdigest()
    # print("The encryption password:", hashed)
    return hashed


# Generate password with hash & password can generate with all characters
def generate_pwd_hash():
    characters = string.ascii_letters + string.digits + string.punctuation
    # print ('The available characters:', characters)
    pwd = ""
    for i in range(12):
        pwd += characters[random.randint(0, len(characters) - 1)]
    print("Your password is: ", pwd)
    hashed = create_hash(pwd)
    return hashed


# when user choose create password
def create_pwd_hash(pwd):
    while True:
        if verify_pwd_validity(pwd):
            print("Your password is: ", pwd)
            break
        else:
            pwd = ask_pwd()
    hashed = create_hash(pwd)
    # print("The encryption password:", hashed)
    return hashed


# verification date future and february
# for example birth day: 2022-03-05 it's not correct. The user must to registre correctly
# for the month of leap February
def verify_date(the_date):
    split_date = the_date.split('-')
    if len(split_date) == 3:
        if (1 > int(split_date[0]) > 31) or (
                datetime.date.today().year == int(split_date[2]) and datetime.date.today().month == int(
            split_date[1]) and datetime.date.today().day < int(split_date[0])):
            return False
        elif (1 > int(split_date[1]) > 12) or (
                datetime.date.today().year == int(split_date[2]) and datetime.date.today().month < int(split_date[1])):
            return False
        elif datetime.date.today().year < int(split_date[2]):
            return False
        else:
            try:
                datetime.datetime(int(split_date[2]), int(split_date[1]), int(split_date[0]))
                return True
            except ValueError:
                print("The given date is wrong")
                return False
    else:
        print("The given date is wrong")
        return False


def return_user(info):
    if len(info) != 0:
        if info[0]["userDepartement"] == "admin":
            user = Admin(info[0]["userLastName"], info[0]["userFirstName"], info[0]["userDoB"].strftime("%d-%m-%Y"),
                         info[0]["userCoB"], info[0]["userEmail"])
        else:
            user = Worker(info[0]["userLastName"], info[0]["userFirstName"], info[0]["userDoB"].strftime("%d-%m-%Y"),
                          info[0]["userCoB"], info[0]["userEmail"])
        user.set_id(info[0]["userId"])
        user.login = info[0]["userLogin"]
        user.set_departement(info[0]["userDepartement"])
        return user


# ask email
def ask_email():
    return input("Please enter email in format xxxxxxx@xxxxxx.xxx: ")


# ask date of birth
def ask_date_birth():
    return input("Please enter date of birth in format DD-MM-YYYY: ")


# ask firstname
def ask_firstname():
    return input("Please enter your firstname: ")


# ask lastname
def ask_lastname():
    return input("Please enter your lastname: ")


# ask country
def ask_country():
    return input("Please enter your birth country: ")


# ask password
def ask_pwd():
    print("Your password must contain at least:\n"
          "8 characters,\n"
          "1 lowercase letter,\n"
          "1 capital letter,\n"
          "1 digit\n")
    return input("Please enter password again: ")


# ask department
def ask_department():
    print("admin-1\n"
          "worker-2\n")
    try:
        return int(input("Please enter your department: "))
    except:
        return -1


# admin connection with password verification if expired
def sign_in_as_admin(login, password):
    info = get_user_with_login_password(login, password)
    if len(info) != 0:
        if info[0]["userDepartement"] == "admin":
            user = return_user(info)
            if verify_expiry(user.get_id()):
                return user
            else:
                user.set_random_pwd()
                update_pwd(user.get_pwd(), user.get_id())
                return user
        else:
            return False
    else:
        return False


# user connection with password verification if expired
def sign_in_as_worker(login, password):
    info = get_user_with_login_password(login, password)
    if len(info) != 0:
        if info[0]["userDepartement"] == "worker":
            user = return_user(info)
            if verify_expiry(user.get_id()):
                return user
            else:
                user.set_random_pwd()
                update_pwd(user.get_pwd(), user.get_id())
                return user
        else:
            return False
    else:
        return False


# set login - first letter firstname + lastname if exist +1
def attribute_login(firstname, lastname):
    counter = 0
    login = firstname[0] + lastname
    while True:
        if counter == 0:
            login = firstname[0] + lastname
        else:
            login = firstname[0] + lastname + str(counter)
        if if_login_exists(login):
            counter += 1
            continue
        else:
            return login


# create user with all information
def create_user(user):
    if if_email_exists(user.email):
        print("Email already exists")
        return False
    else:
        user.set_random_pwd()
        splited_dob = user.dateOfBirth.split('-')
        dob = str(splited_dob[2]) + "-" + str(splited_dob[1]) + "-" + str(splited_dob[0])
        insert_user(user.login, user.lastname, user.firstname, user.email, user.password, dob, user.placeOfBirth)


# create user with all information
def modify_user(user):
    splited_dob = user.dateOfBirth.split('-')
    dob = str(splited_dob[2]) + "-" + str(splited_dob[1]) + "-" + str(splited_dob[0])
    update_user(user.login, user.lastname, user.firstname, user.email, dob, user.placeOfBirth, user.id)


# choice department
def change_departement(id):
    while True:
        department = ask_department()
        if department == 1:
            department = "admin"
            break
        if department == 2:
            department = "worker"
            break
    update_departement(department, id)


def show_user(users):
    print(
        "------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print(
        f"{'ID': ^20}"
        f"{'LOGIN': ^20}"
        f"{'EMAIL': ^20}"
        f"{'LASTNAME': ^20}"
        f"{'FIRSTNAME': ^20}"
        f"{'DATE OF BIRTH': ^20}"
        f"{'COUNTRY OF BIRTH': ^20}"
        f"{'DEPARTMENT': ^20}"
        f"{'PASSWORD EXPIRY DATE': ^20}")
    print(
        "------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    for row in users:
        print(
            f"{str(row['userId']): ^20}"
            f"{str(row['userLogin']): ^20}"
            f"{str(row['userEmail']): ^20}"
            f"{str(row['userLastName']): ^20}"
            f"{str(row['userFirstName']): ^20}"
            f"{str(row['userDoB']): ^20}"
            f"{str(row['userCoB']): ^20}"
            f"{str(row['userDepartement']): ^20}"
            f"{str(row['userPasswordExpiry']): ^20}")

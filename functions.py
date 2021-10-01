import re
import random
import string
import hashlib
import datetime
from datetime import date, timedelta
import calendar
import sys

sys.path.append("../../usersManagementPY")
from classes.User import *
from dbFunctions import *


def verify_email(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if (re.search(regex, email)):
        return True
    else:
        return False


def set_pwd_expiry():
    now = datetime.datetime.now()
    one_month = calendar.monthrange(now.year, now.month)[1]
    end = now + timedelta(days=one_month)
    return end.strftime("%Y-%m-%d")


def verify_expiry(id):
    user = get_user_with_id(id)
    splited_date = str(user[0]["userPasswordExpiry"]).split('-')
    expiry_date = str(splited_date[2]) + "-" + str(splited_date[1]) + "-" + str(splited_date[0])
    if verify_date(expiry_date):
        return False
    else:
        return True


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


def create_hash(pwd):
    salt = "project"
    hashed = hashlib.sha512(pwd.encode() + salt.encode()).hexdigest()
    # print("The encryption password:", hashed)
    return hashed


def generate_pwd_hash():
    characters = string.ascii_letters + string.digits + string.punctuation
    # print ('The available characters:', characters)
    pwd = ""
    for i in range(12):
        pwd += characters[random.randint(0, len(characters) - 1)]
    print("Your password is: ", pwd)
    hashed = create_hash(pwd)
    return hashed


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


def ask_email():
    return input("Please enter email in format xxxxxxx@xxxxxx.xxx: ")


def ask_date_birth():
    return input("Please enter date of birth in format DD-MM-YYYY: ")


def ask_pwd():
    print("Your password must contain at least:\n"
          "8 characters,\n"
          "1 lowercase letter,\n"
          "1 capital letter,\n"
          "1 digit\n")
    return input("Please enter password again: ")


def sign_in_as_admin(login, password):
    info = get_user_with_login_password(login, password)
    if len(info) != 0:
        if info[0]["userDepartement"] == "admin":
            return True
        else:
            return False
    else:
        return False


def sign_in_as_worker(login, password):
    info = get_user_with_login_password(login, password)
    if len(info) != 0:
        if info[0]["userDepartement"] == "worker":
            return True
        else:
            return False
    else:
        return False


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


def create_user(user):
    splited_dob = user.dateOfBirth.split('-')
    dob = str(splited_dob[2]) + "-" + str(splited_dob[1]) + "-" + str(splited_dob[0])
    insert_user(user.login, user.lastname, user.firstname, user.email, user.password, dob, user.placeOfBirth)

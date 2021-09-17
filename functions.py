import re
import random
import string
import hashlib
import datetime
import sys


def verify_email(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if (re.search(regex, email)):
        return True
    else:
        sys.exit("Error in email")


def generate_pwd():
    characters = string.ascii_letters + string.digits + string.punctuation
    # print ('The available characters:', characters)
    pwd = ""
    for i in range(12):
        pwd += characters[random.randint(0, len(characters) - 1)]
    print("Your password is: ", pwd)
    salt = "project"
    hashed = hashlib.sha512(pwd.encode() + salt.encode()).hexdigest()
    # print("The encryption password:", hashed)
    return hashed


def verify_date(day, month, year):
    if (1 > day > 31) or (datetime.date.today().year == year and datetime.date.today().month == month and datetime.date.today().day < day):
        sys.exit("The given date is wrong")
    elif (1 > month > 12) or (datetime.date.today().year == year and datetime.date.today().month < month):
        sys.exit("The given date is wrong")
    elif datetime.date.today().year < year:
        sys.exit("The given date is wrong")
    else:
        return True

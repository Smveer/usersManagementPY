import re
import random
import string
import hashlib
import datetime
from datetime import date, timedelta
import calendar
import sys
sys.path.append("../../usersManagementPY")


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

def expired_pwd():
    now = datetime.datetime.now()
    one_month = calendar.monthrange(now.year, now.month)[1]
    end = now + timedelta(days=one_month)
    # print ("You started the company on : " )
    # print (now.strftime("%d-%m-%Y"))
    print("You can change your password on  ")
    print(end.strftime("%d-%m-%Y"))

def create_pwd(pwd):
    print("Your password must contain at least 8 characters,  1 lowercase letter, 1 capital letter, 1 digit and special characters.\n")
    print("Now enter your password.\n")
    lower, upper, special, digit = 0, 0, 0, 0
    if (len(pwd) >= 8):
        for i in pwd:
            if (i.isupper()):
                upper += 1
            if (i.islower()):
                lower += 1
            if (i.isdigit()):
                digit += 1
            for j in string.punctuation:
                if i == j:
                    special += 1
    else:
        print("Password should be more than 8 characters")
    if (lower >= 1 and upper >= 1 and special >= 1 and digit >= 1):
        print("Valid Password")
    else:
        print("Password not valid. Please try again")


def verify_date(day, month, year):
    Date = input("Enter the date of birth : ")
    day, month, year = Date.split('/')
    Valid = True
    try:
        datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        Valid = False
    if (Valid):
        print("Correct")
    else:
        print("please can you retry ")
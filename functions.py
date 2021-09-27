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


def set_pwd_expiry():
    now = datetime.datetime.now()
    one_month = calendar.monthrange(now.year, now.month)[1]
    end = now + timedelta(days=one_month)
    print("You can change your password on  ")
    print(end.strftime("%d-%m-%Y"))


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


def verify_date(the_date):
    split_date = the_date.split('/')
    if len(split_date) == 3:
        if (1 > int(split_date[0]) > 31) or (datetime.date.today().year == int(split_date[2]) and datetime.date.today().month == int(split_date[1]) and datetime.date.today().day < int(split_date[0])):
            print("The given date is wrong")
            return False
        elif (1 > int(split_date[1]) > 12) or (datetime.date.today().year == int(split_date[2]) and datetime.date.today().month < int(split_date[1])):
            print("The given date is wrong")
            return False
        elif datetime.date.today().year < int(split_date[2]):
            print("The given date is wrong")
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

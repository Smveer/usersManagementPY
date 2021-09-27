import re
import random
import string
import hashlib
import datetime
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

def expiration_pwd()




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
import re
import string
from random import *


def verify_email(email):

    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    if (re.search(regex, email)):
        print("Valid Email")
    else:
        print("Invalid Email")

def generate_pwd():
    allCharacters = string.ascii_letters + string.digits + string.punctuation
    pwd = "".join(choice(allCharacters) for x in range(randint(8, 10)))
    print("Your Password is: ", pwd)
    return pwd

verify_email("singh.manveer93@IC2LOUD.com")
generate_pwd()
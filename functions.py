import re

def verify_email(email):

    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    if (re.search(regex, email)):
        print("Valid Email")
    else:
        print("Invalid Email")

verify_email("singh.manveer93@IC2LOUD.com")
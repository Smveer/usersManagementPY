import re
import random 
import string 
import hashlib


def verify_email(email):

    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    if (re.search(regex, email)):
        print("Valid Email")
    else:
        print("Invalid Email")

def generate_pwd():
   allcharactere = string.ascii_letters+string.digits+string.punctuation
print ('The available characters:',allcharactere)
pwd=""

for i in range (12):
    pwd+=allcharactere [ random.randint(0,len (allcharactere)-1)]
print("The password is :", pwd)

salt="project"
pwd_hashe=hashlib.sha512(pwd.encode()+ salt.encode()) .hexdigest()
print("The encryption password:", pwd_hashe

verify_email("singh.manveer93@IC2LOUD.com")
generate_pwd()



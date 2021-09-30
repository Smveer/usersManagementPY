import sys
sys.path.append("../../usersManagementPY")

from classes.User import *

print(generate_pwd_hash())
verify_pwd_validity("passwOrd2!")
pwd = "passwOrd2"
print(create_hash(pwd))

import sys
sys.path.append("../../usersManagementPY")

from classes.User import *

print(generate_pwd())
verify_pwd_validity("passwOrd2!")

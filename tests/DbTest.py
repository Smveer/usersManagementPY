import sys
sys.path.append("../../usersManagementPY")
from dbFunctions import *

print(get_all_users())

print(get_user_with_id(6))

print(get_user_with_login_password("MSingh", "singh"))

print(if_login_exists("AAnonymous"))


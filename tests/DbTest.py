import sys
sys.path.append("../../usersManagementPY")
from dbFunctions import *

get_all_users()
get_user_with_id(1)

print(sign_in("MSingh", "singh"))

print(if_login_exists("AAnonymous"))


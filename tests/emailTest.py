import sys

from functions import *

sys.path.append("../../usersManagementPY")

from classes.User import *

print(verify_email("singh@singh.sin"))
print(if_email_exists("singh@singh.sin"))

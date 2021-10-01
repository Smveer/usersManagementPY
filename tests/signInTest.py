import sys
sys.path.append("../../usersManagementPY")
from functions import *

print(sign_in_as_admin("MSingh", "passwOrd2!"))
print(sign_in_as_worker("AAnonymous", "passwOrd2!"))
print(sign_in_as_worker("FSananes", "I~+Us+}g%wWg"))
print(create_hash("passwOrd2!"))
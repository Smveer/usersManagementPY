import sys
sys.path.append("../../usersManagementPY")
from functions import *

print(sign_in_as_admin("MSingh", "passwOrd2!"))
user = sign_in_as_worker("AAnonymous", "&RXXe.H'c!kW")
print(user)
#print(sign_in_as_worker("FSananes", "I~+Us+}g%wWg"))
#print(create_hash("passwOrd2!"))
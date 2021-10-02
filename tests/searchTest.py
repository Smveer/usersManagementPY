import sys

sys.path.append("../../usersManagementPY")

from dbFunctions import *

print(search_by_lastname("sin"))
print(search_by_firstname("m"))
print(search_by_email("sin"))
print(search_by_dob("28-07-2000"))
print(search_by_Department("w"))

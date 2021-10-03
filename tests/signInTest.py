import sys
sys.path.append("../../usersManagementPY")
from functions import *

admin = sign_in_as_admin("MSingh", "passwOrd2!")
user = sign_in_as_worker("MSingh", "passwOrd2!")
print(user)
if(user):
    #print(sign_in_as_worker("FSananes", "ir4{*ZVM[FJ0"))

    #print(create_hash("passwOrd2!"))     'X/qs9`k?eU.
    user.set_lastname("Singh")
    user.set_firstname("Manveer")
    #user.set_login()
    user.set_email("fsananes@esgi.fr")
    user.set_dob("hbsxjs")
    modify_user(user)

if(admin):
    admin.list_all_user()
    admin.remove_user(17)
    admin.list_all_user()
    admin.change_rights(16)
    admin.list_all_user()
    #admin.add_user("  ", "    ", "   ", "   ", "  ")
    print(sign_in_as_worker("COulmi", "_zCNc.j(Ec{,"))
    admin.list_all_user()
    admin.generate_user_pwd(16)
    admin.modify_user_lastname(" ", 21)
    admin.list_all_user()
    admin.modify_user_firstname(" ", 21)
    admin.list_all_user()
    admin.modify_user_email(" ", 21)
    admin.modify_user_dob(" ", 21)
    admin.modify_user_pob(" ", 21)

admin.generate_user_pwd(123)
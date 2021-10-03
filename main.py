import functions
from classes.User import *
from functions import *
from dbFunctions import *
import mysql.connector
import sys
from classes.colors import *
sys.path.append("../../usersManagementPY")
##MAIN MENU
print (f"{bcolors.Cyan}#############################################################################")
print (f"{bcolors.Cyan}########                                                             ########")
print (f"{bcolors.Cyan}######## "f"{bcolors.Purple}            GESTION UTILISATEUR IN PYTHON  " f"{bcolors.Cyan}                 ########")
print (f"{bcolors.Cyan}######## ----------------------------------------------------------- ########")
print (f"{bcolors.Cyan}######## "f"{bcolors.Purple}      Create By : SINGH Manveer & GEORGE Mukilventhan " f"{bcolors.Cyan}      ########")
print (f"{bcolors.Cyan}######## ----------------------------------------------------------- ########")
print (f"{bcolors.Cyan}########                                                             ########")
print (f"{bcolors.Cyan}######## "f"{bcolors.Purple}                  Choose a option: " f"{bcolors.Cyan}                         ########")
print (f"{bcolors.Cyan}########                                                             ########")
print (f"{bcolors.Cyan}######## "f"{bcolors.Purple}             1) ADMIN        |   2) USER "f" {bcolors.Cyan}                  ########")
print (f"{bcolors.Cyan}########                                                             ########")
print (f"{bcolors.Cyan}######## "f"{bcolors.Purple}                        3) Exit     "f" {bcolors.Cyan}                       ########")
print (f"{bcolors.Cyan}########                                                             ########")
print (f"{bcolors.Cyan}########                                                             ########")
print (f"{bcolors.Cyan}#############################################################################")
number = input(f"{bcolors.BYellow}Enter a number from 1 to 3: ")
if int(number) == 1:
    print(f"{bcolors.pink}#############################################################################")
    print(f"{bcolors.pink}######## "f"{bcolors.Blue}                     WELCOME ADMIN  " f"{bcolors.pink}                        ########")
    print(f"{bcolors.pink}######## ----------------------------------------------------------- ########")
    print(f"{bcolors.pink}######## "f"{bcolors.Blue}      Create By : SINGH Manveer & GEORGE Mukilventhan " f"{bcolors.pink}      ########")
    print(f"{bcolors.pink}######## ----------------------------------------------------------- ########")
    print(f"{bcolors.pink}######## "f"{bcolors.Blue}                     Login page  " f"{bcolors.pink}                           ########")
    print(f"{bcolors.pink}########                                                             ########")
    while True:
        admin = sign_in_as_admin(input(f"{'Enter the login:': >40}"), input(f"{'Enter the password:': >40}"))
        if not admin:
            continue
        else:
            break
    print(f"{bcolors.pink}########                                                             ########")
    print(f"{bcolors.pink}########                                                             ########")
    print(f"{bcolors.pink}#############################################################################")

    if int(number) == 1:
        print(f"{bcolors.pink}#############################################################################")
        print(f"{bcolors.pink}########                                                             ########")
        print(f"{bcolors.pink}######## "f"{bcolors.Blue}                     WELCOME ADMIN  " f"{bcolors.pink}                        ########")
        print(f"{bcolors.pink}######## ----------------------------------------------------------- ########")
        print(f"{bcolors.pink}######## "f"{bcolors.Blue}      Create By : SINGH Manveer & GEORGE Mukilventhan " f"{bcolors.pink}      ########")
        print(f"{bcolors.pink}######## ----------------------------------------------------------- ########")
        print(f"{bcolors.pink}########                                                             ########")
        print(f"{bcolors.pink}######## "f"{bcolors.Blue}                  Choose a option: " f"{bcolors.pink}                         ########")
        print(f"{bcolors.pink}########                                                             ########")
        print(f"{bcolors.pink}######## "f"{bcolors.Blue}    1) Add a user        |  3) Search a user   " f"{bcolors.pink}             ########")
        print(f"{bcolors.pink}######## "f"{bcolors.Blue}    2) Modify a user     |  4) Delete a user   " f"{bcolors.pink}             ########")
        print(f"{bcolors.pink}########                                                             ########")
        print(f"{bcolors.pink}######## "f"{bcolors.Blue}                   5) Exit                      " f"{bcolors.pink}            ########")
        print(f"{bcolors.pink}########                                                             ########")
        print(f"{bcolors.pink}########                                                             ########")
        print(f"{bcolors.pink}#############################################################################")
        number = input(f"{bcolors.BYellow}Enter a number from 1 to 5: ")
        if int(number) == 1:
            print(f"{bcolors.pink}#############################################################################")
            print(f"{bcolors.pink}########                                                             ########")
            print(f"{bcolors.pink}######## "f"{bcolors.Blue}                     WELCOME ADMIN  " f"{bcolors.pink}                        ########")
            print(f"{bcolors.pink}######## ----------------------------------------------------------- ########")
            print(f"{bcolors.pink}######## "f"{bcolors.Blue}      Create By : SINGH Manveer & GEORGE Mukilventhan " f"{bcolors.pink}      ########")
            print(f"{bcolors.pink}######## ----------------------------------------------------------- ########")
            print(f"{bcolors.pink}########                                                             ########")
            print( f"{bcolors.pink}######## "f"{bcolors.Blue}                  Add User : " f"{bcolors.pink}                               ########")
            print(f"{bcolors.pink}########                                                             ########")
            admin.add_user(input(f"{'Enter last name :': >40}"),
                           input(f"{'Enter first name :': >40}"),
                           input(f"{'Enter date of birth :': >40}"),
                           input(f"{'Enter place of birth :': >40}"),
                           input(f"{'Enter email:': >40}"))
            print(f"{bcolors.pink}########                                                             ########")
            print(f"{bcolors.pink}########                                                             ########")
            print(f"{bcolors.pink}########                                                             ########")
            print(f"{bcolors.pink}#############################################################################")

        elif int(number) == 2:
            print(f"{bcolors.pink}#############################################################################")
            print(f"{bcolors.pink}########                                                             ########")
            print(f"{bcolors.pink}######## "f"{bcolors.Blue}                     WELCOME ADMIN  " f"{bcolors.pink}                        ########")
            print(f"{bcolors.pink}######## ----------------------------------------------------------- ########")
            print(f"{bcolors.pink}######## "f"{bcolors.Blue}      Create By : SINGH Manveer & GEORGE Mukilventhan " f"{bcolors.pink}      ########")
            print(f"{bcolors.pink}######## ----------------------------------------------------------- ########")
            print(f"{bcolors.pink}########                                                             ########")
            print(f"{bcolors.pink}######## "f"{bcolors.Blue}                  Modify User : " f"{bcolors.pink}                            ########")
            print(f"{bcolors.pink}########                                                             ########")
            print(f"{bcolors.pink}######## "f"{bcolors.Blue}          Last name : " f"{bcolors.pink}                                      ########")
            print(f"{bcolors.pink}######## "f"{bcolors.Blue}          First  name : " f"{bcolors.pink}                                    ########")
            print(f"{bcolors.pink}######## "f"{bcolors.Blue}          Date of birth : " f"{bcolors.pink}                                  ########")
            print(f"{bcolors.pink}######## "f"{bcolors.Blue}          Place of birth : " f"{bcolors.pink}                                 ########")
            print(f"{bcolors.pink}######## "f"{bcolors.Blue}          Email : " f"{bcolors.pink}                                          ########")
            print(f"{bcolors.pink}######## "f"{bcolors.Blue}          Department: " f"{bcolors.pink}                                      ########")
            print(f"{bcolors.pink}########                                                             ########")
            print(f"{bcolors.pink}######## "f"{bcolors.Blue}                   1) Enter                      " f"{bcolors.pink}           ########")
            print(f"{bcolors.pink}########                                                             ########")
            print(f"{bcolors.pink}########                                                             ########")
            print(f"{bcolors.pink}#############################################################################")





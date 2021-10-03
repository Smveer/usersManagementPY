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
    print(f"{bcolors.pink}########                                                             ########")
    print(f"{bcolors.pink}######## "f"{bcolors.Blue}                        Login: " f"{bcolors.pink}                             ########")
    print(f"{bcolors.pink}######## "f"{bcolors.Blue}             Login: " f"{bcolors.pink}                                        ########")
    print(f"{bcolors.pink}######## "f"{bcolors.Blue}             Password: " f"{bcolors.pink}                                     ########")
    print(f"{bcolors.pink}########                                                             ########")
    print(f"{bcolors.pink}######## "f"{bcolors.Blue}                   1) Enter                      " f"{bcolors.pink}           ########")
    print(f"{bcolors.pink}######## "f"{bcolors.Blue}                   2) Exit                      " f"{bcolors.pink}            ########")
    print(f"{bcolors.pink}########                                                             ########")
    print(f"{bcolors.pink}########                                                             ########")
    print(f"{bcolors.pink}#############################################################################")
    number = input(f"{bcolors.BYellow}Enter a number from 1 to 2: ")
class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR
    Black = "\033[0;30m"  # Black
    Red = "\033[0;31m"  # Red
    Green = "\033[0;32m"  # Green
    Yellow = "\033[0;33m"  # Yellow
    Blue = "\033[0;34m"  # Blue
    Purple = "\033[0;35m"  # Purple
    Cyan = "\033[0;36m"  # Cyan
    pink = '\033[95m'
    White = "\033[0;37m"  # White
    BBlack = '\033[1;30m'  # Black
    BRed = '\033[1;31m'  # Red
    BGreen = '\033[1;32m'  # Green
    BYellow = '\033[1;33m'  # Yellow
    BBlue = '\033[1;34m'  # Blue
    BPurple = '\033[1;35m'  # Purple
    BCyan = '\033[1;36m'  # Cyan
    BWhite = '\033[1;37m'  # White



import sys
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
    print(f"{bcolors.pink}########                                                             ########")
    print (f"{bcolors.pink}######## "f"{bcolors.Blue}                     WELCOME ADMIN  " f"{bcolors.pink}                        ########")
    print (f"{bcolors.pink}######## ----------------------------------------------------------- ########")
    print (f"{bcolors.pink}######## "f"{bcolors.Blue}      Create By : SINGH Manveer & GEORGE Mukilventhan " f"{bcolors.pink}      ########")
    print (f"{bcolors.pink}######## ----------------------------------------------------------- ########")
    print(f"{bcolors.pink}########                                                             ########")
    print (f"{bcolors.pink}######## "f"{bcolors.Blue}                  Choose a option: " f"{bcolors.pink}                         ########")
    print(f"{bcolors.pink}########                                                             ########")
    print (f"{bcolors.pink}######## "f"{bcolors.Blue}                   1) CONNECTION                      " f"{bcolors.pink}      ########")
    print(f"{bcolors.pink}########                                                             ########")
    print (f"{bcolors.pink}######## "f"{bcolors.Blue}                   1) Exit                      " f"{bcolors.pink}            ########")
    print(f"{bcolors.pink}########                                                             ########")
    print(f"{bcolors.pink}########                                                             ########")
    print(f"{bcolors.pink}#############################################################################")
    number = input(f"{bcolors.BYellow}Enter a number from 1 to 2: ")
    if int(number) == 1:
        print("#############################################################################")
        print("########                                                             ########")
        print("########                       WELCOME ADMIN                         ########")
        print("######## ----------------------------------------------------------- ########")
        print("########      Create By : SINGH Manveer & GEORGE Mukilventhan        ########")
        print("######## ----------------------------------------------------------- ########")
        print("########                                                             ########")
        print("########                   Login                                     ########")
        print("########            LOGIN:                                           ########")
        print("########            Password:                                        ########")
        print("########                                                             ########")
        print("########                        1) Enter                             ########")
        print("########                        2) Exit                              ########")
        print("########                                                             ########")
        print("########                                                             ########")
        print("#############################################################################")
        number = input("Enter a number from 1 to 2: ")
        if int(number) == 1:
            print("#############################################################################")
            print("########                                                             ########")
            print("########                     WELCOME ADMIN                           ########")
            print("######## ----------------------------------------------------------- ########")
            print("########      Create By : SINGH Manveer & GEORGE Mukilventhan        ########")
            print("######## ----------------------------------------------------------- ########")
            print("########                                                             ########")
            print("########                    Choose a option:                         ########")
            print("########                                                             ########")
            print("########      1) Add a user        |  3) Search a user               ########")
            print("########      2) Modify a user     |  4) Delete a user               ########")
            print("########                                                             ########")
            print("########                        5) Exit                              ########")
            print("########                                                             ########")
            print("#############################################################################")
            number = input("Enter a number from 1 to 5: ")
            if int(number) == 1:
                print("#############################################################################")
                print("########                                                             ########")
                print("########                       WELCOME ADMIN                         ########")
                print("######## ----------------------------------------------------------- ########")
                print("########      Create By : SINGH Manveer & GEORGE Mukilventhan        ########")
                print("######## ----------------------------------------------------------- ########")
                print("########                                                             ########")
                print("########                    Add User:                                ########")
                print("########                                                             ########")
                print("########           Last name:                                        ########")
                print("########           First name:                                       ########")
                print("########           Date of birth:                                    ########")
                print("########           Place of birth:                                   ########")
                print("########           E-Mail:                                           ########")
                print("########           Department:                                       ########")
                print("########                                                             ########")
                print("########                        1) Enter                             ########")
                print("########                                                             ########")
                print("########                                                             ########")
                print("#############################################################################")
                number = input("Enter 1 to add user:")
                if int(number) == 1:
                    print('Success')
                    sys.exit
                else:
                    print('Sorry, your choice is wrong can you try again please!')
            elif int(number) == 2:
                print("#############################################################################")
                print("########                                                             ########")
                print("########                      WELCOME ADMIN                         ########")
                print("######## ----------------------------------------------------------- ########")
                print("########      Create By : SINGH Manveer & GEORGE Mukilventhan        ########")
                print("######## ----------------------------------------------------------- ########")
                print("########                                                             ########")
                print("########                    Modify User:                             ########")
                print("########                                                             ########")
                print("########           Last name:                                        ########")
                print("########           First name:                                       ########")
                print("########           Date of birth:                                    ########")
                print("########           Place of birth:                                   ########")
                print("########           E-Mail:                                           ########")
                print("########           Department:                                       ########")
                print("########                                                             ########")
                print("########                        1) Enter                             ########")
                print("########                                                             ########")
                print("########                                                             ########")
                print("#############################################################################")
                number = input("Enter 1 to add user:")
                if int(number) == 1:
                    print('Success')
                    sys.exit
                else:
                    print('Sorry, your choice is wrong can you try again please!')
            elif int(number) == 3:
                print("#############################################################################")
                print("########                                                             ########")
                print("########                       WELCOME ADMIN                          ########")
                print("######## ----------------------------------------------------------- ########")
                print("########      Create By : SINGH Manveer & GEORGE Mukilventhan        ########")
                print("######## ----------------------------------------------------------- ########")
                print("########                                                             ########")
                print("########                    search User:                             ########")
                print("########                                                             ########")
                print("########           Last name:                                        ########")
                print("########           First name:                                       ########")
                print("########                                                             ########")
                print("########                        1) Enter                             ########")
                print("########                                                             ########")
                print("########                                                             ########")
                print("#############################################################################")
                number = input("Enter 1 to search user:")
                if int(number) == 1:
                    print('Success')
                    print('The mail address is:')
                    print('The mail department:')
                    sys.exit
                else:
                    print('Sorry, your choice is wrong can you try again please!')
            elif int(number) == 4:
                print("#############################################################################")
                print("########                                                             ########")
                print("########                       WELCOME ADMIN                          ########")
                print("######## ----------------------------------------------------------- ########")
                print("########      Create By : SINGH Manveer & GEORGE Mukilventhan        ########")
                print("######## ----------------------------------------------------------- ########")
                print("########                                                             ########")
                print("########                    Delete User:                             ########")
                print("########                                                             ########")
                print("########           Last name:                                        ########")
                print("########           First name:                                       ########")
                print("########                                                             ########")
                print("########                        1) Enter                             ########")
                print("########                                                             ########")
                print("########                                                             ########")
                print("#############################################################################")
                number = input("Enter 1 to delete user:")
                if int(number) == 1:
                    print('Success')
                    sys.exit
                else:
                    print('Sorry, your choice is wrong can you try again please!')
            elif int(number) == 5:
                print('You will exit the menu')
                sys.exit
            else:
                print('Sorry, your choice is wrong can you try again please!')
        elif int(number) == 2:
            print('You will exit the menu')
            sys.exit
        else:
            print('Sorry, your choice is wrong can you try again please!')
    elif int(number) == 2:
        print('You will exit the menu')
        sys.exit
    else:
        print('Sorry, your choice is wrong can you try again please!')


elif int(number) == 2:
    print("#############################################################################")
    print("########                                                             ########")
    print("########                         WELCOME USER                        ########")
    print("######## ----------------------------------------------------------- ########")
    print("########      Create By : SINGH Manveer & GEORGE Mukilventhan        ########")
    print("######## ----------------------------------------------------------- ########")
    print("########                                                             ########")
    print("########                    Choose a option:                         ########")
    print("########                                                             ########")
    print("########           1) CREATION       |   2) CONNECTION               ########")
    print("########                                                             ########")
    print("########                        3) Exit                              ########")
    print("########                                                             ########")
    print("########                                                             ########")
    print("#############################################################################")
    number = input("Enter a number from 1 to 3: ")
    if int(number) == 1:
        print("#############################################################################")
        print("########                                                             ########")
        print("########                       WELCOME USER                          ########")
        print("######## ----------------------------------------------------------- ########")
        print("########      Create By : SINGH Manveer & GEORGE Mukilventhan        ########")
        print("######## ----------------------------------------------------------- ########")
        print("########                                                             ########")
        print("########                    My information :                         ########")
        print("########                                                             ########")
        print("########           Last name:                                        ########")
        print("########           First name:                                       ########")
        print("########           Date of birth:                                    ########")
        print("########           Place of birth:                                   ########")
        print("########           E-Mail:                                           ########")
        print("########           Department:                                       ########")
        print("########                                                             ########")
        print("########                        1) Enter                             ########")
        print("########                                                             ########")
        print("########                                                             ########")
        print("#############################################################################")
        number = input("Enter 1 to submit the form:")
        if int(number) == 1:
            print("#############################################################################")
            print("########                                                             ########")
            print("########                       WELCOME USER                          ########")
            print("######## ----------------------------------------------------------- ########")
            print("########      Create By : SINGH Manveer & GEORGE Mukilventhan        ########")
            print("######## ----------------------------------------------------------- ########")
            print("########                                                             ########")
            print("########                    Your account is created                  ########")
            print("########                                                             ########")
            print("########           LOGIN:                                          ########")
            print("########           Your password:                                    ########")
            print("########                                                             ########")
            print("########              Thank you to note this information             ########")
            print("########              they will be useful to connect                 ########")
            print("########                        1) Exit                              ########")
            print("########                                                             ########")
            print("########                                                             ########")
            print("#############################################################################")
            number = input("Enter 1 to exit the form:")
            if int(number) == 1:
                print('You will exit the menu')
                sys.exit
            else:
                print('Sorry, your choice is wrong can you try again please!')
    elif int(number) == 2:
        print("#############################################################################")
        print("########                                                             ########")
        print("########                       WELCOME USER                          ########")
        print("######## ----------------------------------------------------------- ########")
        print("########      Create By : SINGH Manveer & GEORGE Mukilventhan        ########")
        print("######## ----------------------------------------------------------- ########")
        print("########                                                             ########")
        print("########                   Login                                     ########")
        print("########            ID:                                              ########")
        print("########            Password:                                        ########")
        print("########                                                             ########")
        print("########                        1) Enter                              ########")
        print("########                                                             ########")
        print("########                                                             ########")
        print("#############################################################################")
        number = input("Enter 1 to login:")
        if int(number) == 1:
            print("#############################################################################")
            print("########                                                             ########")
            print("########                     WELCOME USER                            ########")
            print("######## ----------------------------------------------------------- ########")
            print("########      Create By : SINGH Manveer & GEORGE Mukilventhan        ########")
            print("######## ----------------------------------------------------------- ########")
            print("########                                                             ########")
            print("########                    Choose a option:                         ########")
            print("########                                                             ########")
            print("########      1) My information    |  3) Search a user               ########")
            print("########                 2) Modify my password                       ########")
            print("########                                                             ########")
            print("########                        4) Exit                              ########")
            print("########                                                             ########")
            print("#############################################################################")
            number = input("Enter a number from 1 to 5: ")
            if int(number) == 1:
                print("#############################################################################")
                print("########                                                             ########")
                print("########                       WELCOME USER                          ########")
                print("######## ----------------------------------------------------------- ########")
                print("########      Create By : SINGH Manveer & GEORGE Mukilventhan        ########")
                print("######## ----------------------------------------------------------- ########")
                print("########                                                             ########")
                print("########                   My information                            ########")
                print("########                                                             ########")
                print("########           Last name:                                        ########")
                print("########           First name:                                       ########")
                print("########           Date of birth:                                    ########")
                print("########           Place of birth:                                   ########")
                print("########           E-Mail:                                           ########")
                print("########           Department:                                       ########")
                print("########                                                             ########")
                print("########                        1) Enter                             ########")
                print("########                                                             ########")
                print("########                                                             ########")
                print("#############################################################################")
                number = input("Enter 1 to exit:")
                if int(number) == 1:
                    print('Success')
                    sys.exit
                else:
                    print('Sorry, your choice is wrong can you try again please!')
            elif int(number) == 2:
                print("#############################################################################")
                print("########                                                             ########")
                print("########                         WELCOME USER                        ########")
                print("######## ----------------------------------------------------------- ########")
                print("########      Create By : SINGH Manveer & GEORGE Mukilventhan        ########")
                print("######## ----------------------------------------------------------- ########")
                print("########                                                             ########")
                print("########                    Choose a option:                         ########")
                print("########                                                             ########")
                print("########           1) Create my password                             ########")
                print("########           2) Generate the password                          ########")
                print("########                        3) Exit                              ########")
                print("########                                                             ########")
                print("########                                                             ########")
                print("#############################################################################")
                if int(number) == 1:
                    print('create my password')
                elif int(number) == 2:\
                    print('Generate my password')
                else:
                    print('Sorry, your choice is wrong can you try again please!')
            elif int(number) == 3:
                print("#############################################################################")
                print("########                                                             ########")
                print("########                       WELCOME USER                          ########")
                print("######## ----------------------------------------------------------- ########")
                print("########      Create By : SINGH Manveer & GEORGE Mukilventhan        ########")
                print("######## ----------------------------------------------------------- ########")
                print("########                                                             ########")
                print("########                    search User:                             ########")
                print("########                                                             ########")
                print("########           Last name:                                        ########")
                print("########           First name:                                       ########")
                print("########                                                             ########")
                print("########                        1) Enter                             ########")
                print("########                                                             ########")
                print("########                                                             ########")
                print("#############################################################################")
                number = input("Enter 1 to search user:")
                if int(number) == 1:
                    print('Success')
                    print('The mail address is:')
                    print('The mail department:')
                    sys.exit
                else:
                    print('Sorry, your choice is wrong can you try again please!')
            elif int(number) == 4:
                print('You will exit the menu')
                sys.exit
            else:
                print('Sorry, your choice is wrong can you try again please!')
    elif int(number) == 3:
        print('You will exit the menu')
        sys.exit
    else:
        print('Sorry, your choice is wrong can you try again please!')



elif int(number) == 3:
    print('You will exit the menu')
    sys.exit
else:
    print(bcolors.Red+'Sorry, your choice is wrong can you try again please!')


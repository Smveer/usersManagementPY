class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR
import sys
##MAIN MENU

print ("#############################################################################")
print ("########                                                             ########")
print ("########               GESTION UTILISATEUR IN PYTHON                 ########")
print ("######## ----------------------------------------------------------- ########")
print ("########      Create By : SINGH Manveer & GEORGE Mukilventhan        ########")
print ("######## ----------------------------------------------------------- ########")
print ("########                                                             ########")
print ("########                    Choose a option:                         ########")
print ("########                                                             ########")
print ("########           1) ADMIN        |   2) USER                       ########")
print ("########                                                             ########")
print ("########                        3) Exit                              ########")
print ("########                                                             ########")
print ("########                                                             ########")
print ("#############################################################################")
number = input("Enter a number from 1 to 3: ")
if int(number) == 1:
    print("#############################################################################")
    print("########                                                             ########")
    print("########                       WELCOME ADMIN                         ########")
    print("######## ----------------------------------------------------------- ########")
    print("########      Create By : SINGH Manveer & GEORGE Mukilventhan        ########")
    print("######## ----------------------------------------------------------- ########")
    print("########                                                             ########")
    print("########                    Choose a option:                         ########")
    print("########                                                             ########")
    print("########                    1) CONNECTION                            ########")
    print("########                                                             ########")
    print("########                    2) Exit                                  ########")
    print("########                                                             ########")
    print("########                                                             ########")
    print("#############################################################################")
    number = input("Enter a number from 1 to 2: ")
    if int(number) == 1:
        print("#############################################################################")
        print("########                                                             ########")
        print("########                       WELCOME ADMIN                         ########")
        print("######## ----------------------------------------------------------- ########")
        print("########      Create By : SINGH Manveer & GEORGE Mukilventhan        ########")
        print("######## ----------------------------------------------------------- ########")
        print("########                                                             ########")
        print("########                   Login                                     ########")
        print("########            ID:                                              ########")
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
                print('add')
            elif int(number) == 2:
                print('modify')
            elif int(number) == 3:
                print('search')
            elif int(number) == 4:
                print('Deleted')
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
            print("########           Your ID:                                          ########")
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
                print('info')
            elif int(number) == 2:
                print('Modify')
            elif int(number) == 3:
                print('Search')
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
    print('Sorry, your choice is wrong can you try again please!')


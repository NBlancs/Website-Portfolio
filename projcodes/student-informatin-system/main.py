
# SORRY FOR THE FUCKLOAD OF LIBRARIES I IMPORTED 
# ALSO THE USERNAME IS "admin" AND THE PASSWORD IS "369" YOU MAY NOT SEE THE PASS BUT JUST TYPE 369 AND PRESS ENTER AND IT WILL WORK LIKE MAGIC

import re
import time
import sys
from os import name, system 
from getpass import getpass


#  GREETINGS PAGE
def greetings():
    print('\u001b[35m')
    print(

   """

   _____ _______ _    _ _____  ______ _   _ _______    _______     _______ _______ ______ __  __   _____ _   _ ______ ____  _____  __  __       _______ _____ ____  _   _ 
  / ____|__   __| |  | |  __ \|  ____| \ | |__   __|  / ____\ \   / / ____|__   __|  ____|  \/  | |_   _| \ | |  ____/ __ \|  __ \|  \/  |   /\|__   __|_   _/ __ \| \ | |
 | (___    | |  | |  | | |  | | |__  |  \| |  | |    | (___  \ \_/ / (___    | |  | |__  | \  / |   | | |  \| | |__ | |  | | |__) | \  / |  /  \  | |    | || |  | |  \| |
  \___ \   | |  | |  | | |  | |  __| | . ` |  | |     \___ \  \   / \___ \   | |  |  __| | |\/| |   | | | . ` |  __|| |  | |  _  /| |\/| | / /\ \ | |    | || |  | | . ` |
  ____) |  | |  | |__| | |__| | |____| |\  |  | |     ____) |  | |  ____) |  | |  | |____| |  | |  _| |_| |\  | |   | |__| | | \ \| |  | |/ ____ \| |   _| || |__| | |\  |
 |_____/   |_|   \____/|_____/|______|_| \_|  |_|    |_____/   |_| |_____/   |_|  |______|_|  |_| |_____|_| \_|_|    \____/|_|  \_\_|  |_/_/    \_\_|  |_____\____/|_| \_|
                                                                                                                                                                          
                                                                                                                                                                          
                                                                                                                                                                                                                                                                                                                                                                                                                                                         
   """
    )
    print('\033[0;0m')


# FOR CLEARING THE PAGE WHEN THE USER IS DONE INPUTTING USERNAME AND PASSWORD
def clear_terminal ():
    if name == 'nt':  
        system('cls')
    else: 
        system('clear')



# AUTHENTICATION PAGE
def auth():
    while True:

        greetings()

        print("\033[1m") # IGNORE THIS WEIRD LOOKING PRINT COMMANDS, THIS ONLY CHANGES THE COLOR OF THE TEXT
        print("\033[1;37m")

        username: str = input('Username : ')
        password: str = getpass('Password: ')
        print("\n")


        print("\033[1;32m")
        # LOADING ANIMATION CAUSE WHY NOT?
        if username == 'admin' and password == '369':
            animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

            for i in range(len(animation)):
                time.sleep(0.2)
                sys.stdout.write("\r" + animation[i % len(animation)])
                sys.stdout.flush()

            print("\n")
            print('\033[0;0m') 
            print('\033[92mAuthentication Success! ')
            print('Press ENTER to continue ')

            input()
            clear_terminal()
            return

        print('\033[91m Username or password not found!\n Press ENTER to continue ')

        input()
        clear_terminal()



# MAIN MENU PAGE
def main_menu():
    student = {
        2023301373: ("Lui", [90, 91, 83, 78, 93]),
        2023302832: ("Nahoy", [97, 93, 94, 95, 89]),
        2023301375: ("Callanta", [90, 91, 83, 78, 93]),
        2023502831: ("Nikul", [89, 79, 91, 86, 90])
    }

    while True:
        try:
            print("\033[0;32m")
            print("Type 'logout' to Logout")
            usr_input = input("Enter student ID: ")

            if usr_input.lower() == 'logout':
                print("Logging out...")
                auth()
                break

            if re.match(r'^\d+$', usr_input):
                usr_chc = int(usr_input)
                if usr_chc in student:
                    name, grades = student[usr_chc]
                    max_grade = max(grades)
                    print(f"The maximum grade of the student ID {usr_chc} is: {max_grade}")
                else:
                    print('Student not found!')
            else:
                print("Invalid input. Please enter a numeric student ID.")

        except ValueError:
            print("\nError Input, Try Again!")


# THIS IS HERE SO THAT WHEN YOU ARE DONE AUTHENTICATING YOURSELF YOU ARE THEN TRANSPORTED TO THE MAIN MENU PAGE
if __name__ == '__main__':
    auth()

    while True:
        main_menu()


# MADE WITH LOVE MWAH MWAH MWAH
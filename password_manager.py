#!/usr/bin/python3
import time
import sys

def prompt_user():
    input("Enter your Master password: ")


def view_existing_passwords():
    with open('account_password.txt', 'r') as file_object:
        for line in file_object:
            print(line.rstrip())


def add_new_password():
    """Allow user to add a new password."""
    print(f"{'Add New Account':*^50}")
    print(f"{'Press Q to quit':^50}")

    while True:
        account = input(f"\n{'Account Name: ':>20}")
        password = input(f"{'Password: ':>20}")
        with open('account_password.txt', 'a', encoding='utf-8') as file_object:
            file_object.write(account +  + {password} + '\n')

def pause_and_return():
    input("Press Enter to return to main Menu.")
    clear_screen()

def clear_screen():
    """uses ANSI escape codes to clear terminal screen"""
    sys.stdout.write("\033[H\033[J")
    sys.stdout.flush()

def quit_application():
    """Quits the application"""
    print("\nExiting the Application...\n")
    time.sleep(2)
    quit()

def main():
    while True:
        print(f'\n\n{"WELCOME TO PASSWORD MANAGER":*^50}')
        print(f"\n{'1. Add a New Password':^50}")
        print(f"{'2. View Existing Passwords':^54}")
        print(f"{'3. Quit':^35}")

        option = int(input(f"\n{'Select an Option: ':>32}"))
        if option == 1:
            clear_screen()
            add_new_password()
            pause_and_return()
        elif option == 2:
            clear_screen()
            view_existing_passwords()
            pause_and_return()
        elif option == 3:
            clear_screen()
            quit_application()
            pause_and_return()
        else:
            print("Invalid Option!")
            continue
    

if __name__ == '__main__':
    main()


#!/usr/bin/python3
import time
import sys
from cryptography.fernet import Fernet


def prompt_user():
    input("Enter your Master password: ")


def view_existing_passwords():
    print(f"{'Your accounts':>^30}\n")
    try:
        with open('account_password.txt', 'r') as file_object:
            for line in file_object:
                print(line.rstrip())
    except FileNotFoundError:
        print("\nFile not found!!")
    except Exception as e:
        print(f"Error: {e}")


def add_new_acount():
    """Allow user to add a new password."""
    print(f"{'Add New Account':>^50}")
    print(f"{'Press Q go back':^50}")

    while True:
        account = input(f"\n{'Account Name: ':>20}")
        if account.lower() == 'q':
            main()
        password = input(f"{'Password: ':>20}")
        if account.lower() == 'q':
            main()
        with open('account_password.txt', 'a', encoding='utf-8') as file_object:
            file_object.write(account + f"{password:>20}" + '\n')

def pause_and_return():
    input("\nPress Enter to return to main Menu.")
    clear_screen()

def clear_screen():
    """uses ANSI escape codes to clear terminal screen"""
    sys.stdout.write("\033[H\033[J")
    sys.stdout.flush()

def quit_application():
    """Quits the application"""
    print(f"\n{'Exiting the Application...':>40}")
    time.sleep(2)
    quit()

def main():
    clear_screen()
    while True:
        print(f'\n{"WELCOME TO PASSWORD MANAGER":>^50}')
        print(f"\n{'1. Add a new account🔑':^50}")
        print(f"{'2. View existing accounts':^54}")
        print(f"{'3. Quit':^35}")

        try:
            option = int(input(f"{'Select an Option: ':>32}"))
            if option == 1:
                clear_screen()
                add_new_acount()
                pause_and_return()
            elif option == 2:
                clear_screen()
                view_existing_passwords()
                pause_and_return()
            elif option == 3:
                quit_application()
            else:
                clear_screen()
                print("\nInvalid Option!")
                time.sleep(2)
                clear_screen()
                continue
        except ValueError:
            clear_screen()
            print("\nInvalid value!!")
            time.sleep(2)
            clear_screen()

    

if __name__ == '__main__':
    main()


#!/usr/bin/env python3.6
from passlocker import User,Credentials
import random #Generate random numbers for various distributions including integer and floats.
import string #string module allows you to create and customize your own string

def create_user(username,password):
    '''
    Function to create a new user
    '''
    new_user = User(username,password)
    return new_user


def save_user(user):
    '''
    Function to save new user
    '''
    user.save_user()


def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()

def create_new_credential(account,username,password):
    """
    Function to create a new credential for a given user
    """
    new_credential = Credentials(account,username,password)
    return new_credential
def save_credentials(credentials):
    """
    Function to save Credentials to the credentials list
    """
    credentials. save_details()
def display_accounts_details():
    """
    Function that returns all the saved credential.
    """
    return Credentials.display_credentials()

def delete_credential(credentials):
    """
    Function to delete a Credentials from credentials list
    """
    credentials.delete_credentials()

def find_credential(account):
    """
    Function that finds a Credentials by an account name and returns the Credentials that belong to that account
    """
    return Credentials.find_credential(account)

def main():
    print("Welcome to your Password Locker \n Enter one of the following codes to proceed.\n NU --- Create New User Account  \n LI ---  Login  \n")
    if short_code == "nu":
        print("Sign Up")
        print('*' * 40)
        username = input("User_name: ")
        while True:
            print(" TP - To create your own pasword:\n GP - To generate random Password")
            password_Choice = input().lower().strip()
            if password_Choice == 'tp':
                password = input("Enter Password\n")
                break
            elif password_Choice == 'gp':
                def random_password(string_length):
                            letters = string.ascii_letters
                            return "".join(random.choice(letters) for i in range(string_length))
                            print(f"Your random password for {username} is:", random_password(8))
                
            else:
                print("Invalid password please try again")
        save_user(create_new_user(username,password))
        print("*"*40)
        print(f"Hello {username}, Your account has been created succesfully! Your password is: {password}")
        print("*"*50)
    elif short_code == "li":
        print("*"*70)
        print("Enter your User name and your Password to log in:")
        print('*' * 70-)
        username = input("User name: ")
        password = input("password: ")
        login = login_user(username,password)
        if login_user == login:
            print(f"Hello {username}.Welcome To Password Locker App")  
            print('\n')
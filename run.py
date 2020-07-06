#!/usr/bin/env python3.6
from passlocker import User,Credentials


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


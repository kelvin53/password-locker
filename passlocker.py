import random #Generate random numbers for various distributions including integer and floats.
import string #string module allows you to create and customize your own string

class User:
    """
    Class that generates new instances of users.
    """

    user_list = [] # Empty user list

    def __init__(self, username, password):
        """
        method that defines the user properties.
        """
        self.username = username
        self.password = password


    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)

        
class Credentials:
    """
    Class that generates new instances of credentials.
    """

    credentials_list = [] # Empty credentials list

    def __init__(self,account,username, password):
        """
        method that defines the credentials properties.
        """
        self.account = account
        self.username = username
        self.password = password

    def save_credential(self):
        """
        method to store a new credential to the credentials list
        """
        Credentials.credentials_list.append(self)

    def delete_credential(self):

        '''
        delete_credential method deletes a saved credential from the credentials_list
        '''

        Credentials.credentials_list.remove(self)  


    @classmethod
    def find_credential(cls,account):
        '''
        Method that takes in a account and returns a credential that matches that account.

        Args:
            account: account name to search for
        Returns :
            Credentials that matches the account.
        '''

        for credential in cls.credentials_list:
            if credential.account == account:
                return credential 

    @classmethod
    def display_credentials(cls):
        """
        Method that returns all items in the credentials list

        """
        return cls.credentials_list
    
    def generatePassword(stringLength=8):
        """Generate a random password string of letters and digits and special characters"""
        password = string.ascii_uppercase + string.ascii_lowercase + string.digits + "~!@#$%^&*"
        return ''.join(random.choice(password) for i in range(stringLength))
 


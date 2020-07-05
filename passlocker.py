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

        




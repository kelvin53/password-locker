import unittest # Importing the unittest module
from passlocker import User # Importing the User class
from passlocker import Credentials #Importing the Credentials class
class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the User class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User('KelvinKoskei','kelvinKIPkoskei') # create user object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.username,"KelvinKoskei")
        self.assertEqual(self.new_user.password,"kelvinKIPkoskei")


    def test_save_user(self):
        '''
        test_save_user is a test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list),1)


#setup and class creation up here
class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the Credentials class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = Credentials('twitter','KI Prono','kelvinKIPkost') # create credential object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        
        self.assertEqual(self.new_credential.account,"twitter")
        self.assertEqual(self.new_credential.username,"KI Prono")
        self.assertEqual(self.new_credential.password,"kelvinKIPkost")


# other test cases here
    def test_save_credential(self):
        '''
        test_save_credential test case to test if the credential object is saved into
         the credential list
        '''
        self.new_credential.save_credential() # saving the new credential
        self.assertEqual(len(Credentials.credentials_list),1)


    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credentials.credentials_list = []


    def test_save_multiple_credentials(self):
            '''
            test_save_multiple_credentials to check if we can save multiple credential
            objects to our credentials_list
            '''
            self.new_credential.save_credential()
            test_save_credential = Credentials("Test","ronny","kEgcsd") # new credential
            test_save_credential.save_credential()
            self.assertEqual(len(Credentials.credentials_list),2)




if __name__ == '__main__':
    unittest.main()
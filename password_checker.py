class PasswordChecker:
    # DO NOT MODIFY THIS METHOD
    def __init__(self, password):
        self.password = password
    
    # to use password variable, use self.password in your code
    '''
    for example, if you want to check the length of the password, you can use
    if len(self.password) > 8:
        print("Password is long enough")
    else:
        print("Password is too short")
    
    see how self.password is used instead of password? 
    that's how you will access it in your code

    also for the project, make sure you use print statements to print out the results to the user
    '''
    def composition_check(self):
        # check if password contains at least one uppercase letter, one lowercase letter, and one number
        # return True if it does, False if it doesn't
        # YOUR CODE HERE
        return False
    
    def length_check(self):
        # check if password is at least 8 characters long
        # return True if it is, False if it isn't (techinically i already did this one for you)
        # YOUR CODE HERE
        return False
    
    def special_char_check(self):
        # check if password contains at least one special character
        # return True if it does, False if it doesn't
        # YOUR CODE HERE
        # hint: you are allowed to use string methods in this one, like how i showed you guys .upper() and .lower() there are other methods if you search them up
        return False

    def common_password_check(self):
        # check if password is a common password
        # return True if it is, False if it isn't
        # YOUR CODE HERE
        # hint: you will have to use the file common_passwords.txt (you can also add more passwords to this file if you want) i've stored the file to the variable common_passwords
        # hint: you will have to use a for loop to iterate through the file
        common_passwords = open("common_passwords.txt", "r")


        return False

    def password_strength(self):
        # check if password is strong
        # return True if it is, False if it isn't
        # YOUR CODE HERE
        # hint: you will have to use all of the methods you've created above
        return False
    
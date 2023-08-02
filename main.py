'''
DO NOT MODIFY THIS FILE
'''

from password_checker import PasswordChecker

def main():
    # DO NOT MODIFY THIS METHOD
    password = input("Enter a password: ")
    password_checker = PasswordChecker(password)
    print(password_checker.password_strength())

if __name__ == "__main__":
    main()

# Importing random function
from random import *

# take the user password
user_password = input("Pl enter the passowrd: ")

# make a list of digits option of the password
password = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z','w',
           'A','B','C','D','E', 'F','G','H','I', 'J', 'K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
           '1','2','3','4','5','6','7','8','9','0']

# check the guess pass with user password
guess_password = ""
while (guess_password != user_password):
    guess_password = ""

    for letter in range(len(user_password)):
        guess = password[randint(0,60)]
        guess_password = str(guess) + str(guess_password)
        print(guess_password)


# print the password while matched
print("your password is: ", guess_password)
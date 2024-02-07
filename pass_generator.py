#import modules
import string
import random
def main():
    #ask for password length input
    pass_length = int(input("How long do you need the password to be?"))
    pass_generator(pass_length)
#create function to generate pass
def pass_generator(pass_length):
    #create password varidable
    password = ""
    #while the password length is less than length input 
    while len(password) < pass_length:
        #generate a random character
        rand_char = random.choice(string.ascii_letters)
        #generate a random integer
        rand_int = random.randint(0, 10)
        #generate a special character
        rand_special = random.choice("!@#$%^&*")
        #add the random character to the password variable 
        password = password + rand_char + str(rand_int) + str(rand_special)
    #print the password variable
    print(password)

main()
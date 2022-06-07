
from random import randint
import random
import string

from numpy import pad
def password():
    letter1 = random.choice('qwertyuiopasdfghjklzxcvbnm') #generate the 1 letter
    letter2 = random.choice('QWERTYUIOPASDFGHJKLZXCVBNM') #generate the 2 letter
    letter3 = random.choice('qwertyuiopasdfghjklzxcvbnm') #Generates the 3 letter
    letter4 = random.choice('qwertyuiopasdfghjklzxcvbnm') #Generates the 4 letter
    letter5 = random.choice('qwertyuiopasdfghjklzxcvbnm') #Generates the 5 letter
    Password1=random.choice('1234567890') #Generatess random number between 0 to 9
    Password2=random.choice('1234567890') #Generatess random number between 0 to 9
    Password3=random.choice('1234567890') #Generatess random number between 0 to 9
    Password4=random.choice('1234567890') #Generatess random number between 0 to 9
    Password5=random.choice('1234567890') #Generatess random number between 0 to 9
    special=random.choice('!@#$%^&*()_+=-') #Generatess random special characters
    all = letter1 + letter2 + letter3 + letter4 + letter5 + Password1 + Password2 + Password3 + Password4 + Password5 + special
    print(all)
    file=open("PASSWORD.txt", "w")
    file.write(all)
    file.close()
    input()
password()



from logging import root
from random import randint
import string

from numpy import pad
string.ascii_letters
string.ascii_lowercase
string.ascii_uppercase
def password():
    letter1 = random.choice('qwertyuiopasdfghjklzxcvbnm')
    letter2 = random.choice('QWERTYUIOPASDFGHJKLZXCVBNM')
    letter3 = random.choice('qwertyuiopasdfghjklzxcvbnm')
    letter4 = random.choice('qwertyuiopasdfghjklzxcvbnm')
    letter5 = random.choice('qwertyuiopasdfghjklzxcvbnm')
    Password1=random.choice('1234567890')
    Password2=random.choice('1234567890')
    Password3=random.choice('1234567890')
    Password4=random.choice('1234567890')
    Password5=random.choice('1234567890')
    special=random.choice('!@#$%^&*()_+=-')
    all = letter1 + letter2 + letter3 + letter4 + letter5 + Password1 + Password2 + Password3 + Password4 + Password5 + special
    print(all)
    file=open("C:/Users/nitay\Desktop/PASSWORD.txt", "w")
    file.write(all)
    file.close
password()


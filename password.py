
import random
def generate():
    password={}
    for i in range(2,14):
        random__ = random.choice("1234567890qwertyuiopASDFGHJKLzxcvbnm!@#$%^&*()")
        password[str(i)] = random__

    #new__lst=(str(password)[1:-1])
    new__lst = (str(password)[1:-1])
    new__lst=new__lst.replace('\'','').replace(',','').replace(":",'').replace(' ','')
    new__lst = new__lst[:len(new__lst)//2]
    print("New password:",new__lst)
    input()

generate()


import random
password={}
for i in range(0,10):
    random__ = random.choice("1234567890qwertyuiopasdfghjklzxcvnm!@#$%^&*()QWERTYUIOPASDFGHJKLZXFGHM")
    password[str(i)] = random__

new__lst=(str(password)[1:-1])
new__lst=new__lst.replace('\'','').replace(',','').replace(":",'').replace(' ','')
print("New password:",new__lst)
input()

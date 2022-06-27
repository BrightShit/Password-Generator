from tkinter import *
import random
lst = []
window = Tk()
window.geometry("300x250")
window.configure(bg="#347aeb")
# Generating a random password
window.title("Password generator")
def generate_password():
    generate_button['state'] = 'disabled'
    for i in range(0,20):
        lst.insert(i,random.choice("1234567890qwertyuiopASDFGHJKLzxcvbnm!@#$%^&*()"))
    E = Label(window,width=35,borderwidth=5,text=lst)
    E.pack()
    save_button.pack()
def quit():
    window.quit()


def save():
    file = open("Password.txt","w")
    for letter in lst:
        file.write(str(letter))
    file.close()
    save_label=Label(window,text="Password Saved")
    save_label.pack()


generate_button=Button(window,text="Click here to generate a password",padx=20,pady=10,command=generate_password)
quit_button = Button(window,text="Quit",command=quit)
save_button=Button(window,text="Save Password",command=save)
generate_button.pack()
quit_button.pack()
window.mainloop()

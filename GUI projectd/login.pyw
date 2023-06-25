from tkinter import*
import tkinter.messagebox as tmsg
from tkinter import messagebox
import os
import subprocess
import ast
from PIL import Image, ImageTk


root = Tk()

root_width = 900
root_height = 500


Screen_width = 1280#root.winfo_screenmmwidth()
Screen_height = 700#root.winfo_screenmmheight()

x_axis = (Screen_width / 2) - (root_width / 2)
y_axis = (Screen_height / 2) - (root_height / 2)

root.geometry("{}x{}+{}+{}".format(root_width, root_height, int(x_axis), int(y_axis)))
root.title("Login Page")
#root.geometry("900x500+300+200")
root.wm_iconbitmap("assets\pass23.ico")
root.configure(bg="#fff")
root.resizable(False, False)

def signin():
    username = user.get()
    Password = password.get() 

    file = open('datasheet.txt', 'r')         # print(r.keys())
                                                        # print(r.values())
    d = file.read()
    r = ast.literal_eval(d)
    file.close()

    if username in r.keys() and Password == r[username]: #  username=='Dadus' and Password=='Dadusbhai23@':
        root.destroy()
        os.system('python final_pr.pyw')
        username.delete(0, 'end')
        Password.delete(0, 'end')
        pid = os.getpid()
        os.kill(pid, 9)
        #---------------------------------
        screen = Toplevel(root)
#=================================end of the final project========================================
    else:
        messagebox.showerror('Invalid', 'invalid user or password')
    #------------------------------------------------------------------------------------------
    # elif username!='Dadus' or Password!='Dadusbhai23@':
    #     messagebox.showerror("Something is Wrong !", "Invalid UserName and Password")

    # elif username!='Dadus':
    #     messagebox.showerror("Something is Wrong !", "Invalid UserName")    

    # elif Password!='Dadusbhai23@':
    #     messagebox.showerror("Something is Wrong !", "Invalid Password")        
def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Username')

def signup():
    root.destroy()
    os.system('python new_signup.pyw')
    user.delete(0, 'end')
    password.delete(0, 'end')
    pid = os.getpid()
    os.kill(pid, 9)
    

img = PhotoImage(file='assets\login.png')
Label(root, image= img, bg="white").place(x=50, y=50)

frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70 )

heading = Label(frame, text="Log in", fg="#57a1f8", bg="white", font=("Microsoft YaHei UI Light", 25, "bold"))
heading.place(x=100, y=5)

user = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
user.place(x=30, y=80)
user.insert(0, 'username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

# line for a box after user name 
Frame(frame, width=295, height=2, bg="black").place(x=23, y=107)

def on_enter(e):
    password.delete(0, 'end')

def on_leave(e):
    name = password.get()
    if name == '':
        password.insert(0, 'Password#23')

password = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
password.place(x=30, y=150)#y =150
password.insert(0, 'Password#23')
password.bind('<FocusIn>', on_enter)
password.bind('<FocusOut>', on_leave)
# line for a box after user name 
Frame(frame, width=295, height=2, bg="black").place(x=23, y=177) # y= 177

Button(frame, width=29, text="Log in",command=signin ,cursor='hand2',font=("Microsoft YaHei UI Light", 13,"bold"), bg="#57a1f8", fg="white", border=0).place(x=30, y= 230 )
label = Label(frame, text="Don't have an account?", fg="black", bg="white", font=("Microsoft YaHei UI Light", 11))
label.place(x=66, y= 280)

sign_up = Button(frame, width=6, text="Sign UP",command=signup, border=0, bg="white", fg="#57a1f8", cursor='hand2', font=("Microsoft YaHei UI Light", 11))
sign_up.place(x=234, y=280)

label = Label(root, text="This Software is made By Krishna (Dadus) . . .  :) ", fg="black", bg="white", font=("Microsoft YaHei UI Light", 11))
label.place(x=285, y=455)



root.mainloop()
from tkinter import*
from tkinter import messagebox
import tkinter.messagebox as tmsg
import os
import subprocess
from PIL import Image, ImageTk
import ast

root = Tk()

#=====================================================================#
root_width = 1025
root_height = 650

Screen_width = 1280#root.winfo_screenmmwidth()
Screen_height = 650#root.winfo_screenmmheight()

x_axis = (Screen_width / 2) - (root_width / 2)
y_axis = (Screen_height / 2) - (root_height / 2)

root.geometry("{}x{}+{}+{}".format(root_width, root_height, int(x_axis), int(y_axis)))
#======================================================================#
root.title("Paassword Saver")
#root.geometry("1025x650+300+200")
root.wm_iconbitmap("assets\paa.ico")
root.configure(bg="#fff")
root.resizable(False, False)
#=========================================================================================#
def getvals():
    print("The Site Name is :", sitenameloginvalue.get())
    print("The Userlogin Name is :", userloginnamevalue.get())
    print("The Passlogin is :", passloginvalue.get())

    with open("data/password.txt", "a") as f:
        f.write(f"Site name : {sitenameloginvalue.get()} ," + f"Userlogin Name : {userloginnamevalue.get()} ," + f"Passlogin : {passloginvalue.get()}\n\n")
        tmsg.showinfo("passlogin Saved", f"Your Userlogin name and Passlogin is saved for '{sitenameloginvalue.get()}' Site")
    sitenamelogin.delete(0, 'end')
    userlogin.delete(0, 'end')
    passlogin.delete(0, 'end')

def logout():
    # Open login.py file
    tmsg.showinfo("Log Out", "Click ok to Log Out !")
    subprocess.Popen(['python', 'login.pyw'])
    # Close passlogin_saver.py file
    pid = os.getpid()
    os.kill(pid, 9)
    tmsg.showinfo("Log Out", "Click ok to Log Out !")
    
#==================================================================================================================#
def viewpass():
    os.system('python showpass.py')
#==================================================================================================================#
img = Image.open("assets\packimg.png")
width, height = img.size
img = ImageTk.PhotoImage(img.resize((width, height), Image.ANTIALIAS))
Label(root, image=img, bg="white").place(x=6, y=6, relwidth=1, relheight=1)

heading = Label(root, text="Save the passlogin", fg="#0C3C62", bg="#aacbff", font=("Microsoft YaHei UI Light", 23, "bold"))
heading.place(x=424, y=150)


#---------------------------------------------------#
sitenameloginvalue = StringVar()
userloginnamevalue = StringVar()
passloginvalue = StringVar()
#-----------------------------------------------------------------------------------------------------------#
def on_enter(e):
    sitenamelogin.delete(0, 'end')

def on_leave(e):
    name = sitenamelogin.get()
    if name == '':
        sitenamelogin.insert(0, 'Enter the site name here')

sitenamelogin = Entry(root, width=26, fg="black", textvariable=sitenameloginvalue,border=0, bg="white", font=("Microsoft YaHei UI Light", 15))
sitenamelogin.place(x=450, y=245)#y =150
sitenamelogin.insert(0, 'Enter the site name here')
sitenamelogin.bind('<FocusIn>', on_enter)
sitenamelogin.bind('<FocusOut>', on_leave)

#---------------- d
hide = Frame(root, width=200, height=16, bg="#aacbff").place(x=437, y=290)
#-------------------------------------------------S----------------------------------------------------------#
under = Frame(root, width=315, height=2, bg="black").place(x=437, y=279)
#-----------------------------------------------------------------------------------------------------------#
def on_enter(e):
    userlogin.delete(0, 'end')

def on_leave(e):
    name = userlogin.get()
    if name == '':
        userlogin.insert(0, 'Userloginname')
userlogin = Entry(root, width=26, fg="black", textvariable=userloginnamevalue,border=0, bg="white", font=("Microsoft YaHei UI Light", 15))
userlogin.place(x=450, y=350)
userlogin.insert(0, 'userloginname')
userlogin.bind('<FocusIn>', on_enter)
userlogin.bind('<FocusOut>', on_leave)
#-----------------------------------------------------------------------------------------------------------#
under = Frame(root, width=315, height=2, bg="black").place(x=437, y=380)
#-----------------------------------------------------------------------------------------------------------#
def on_enter(e):
    passlogin.delete(0, 'end')

def on_leave(e):
    name = passlogin.get()
    if name == '':
        passlogin.insert(0, 'Passlogin#23')

passlogin = Entry(root, width=26, fg="black", textvariable=passloginvalue,border=0, bg="white", font=("Microsoft YaHei UI Light", 15))
passlogin.place(x=450, y=410)#y =150
passlogin.insert(0, 'Passlogin#23')
passlogin.bind('<FocusIn>', on_enter)
passlogin.bind('<FocusOut>', on_leave)
#-----------------------------------------------------------------------------------------------------------#
under = Frame(root, width=315, height=2, bg="black").place(x=437, y=445)
#-----------------------------------------------------------------------------------------------------------#width=44, pady=12,

Button(root, width=31, pady=12, text="Save Userlogin Name & Passlogin",command=getvals,bg="#007dfe",font=("Microsoft YaHei UI Light", 11 ,"bold"), fg="white", border=0).place(x=437, y=488)
label = Label(root, text="This Software is made By Krishna (Dadus) . . .  :) ", fg="black", bg="white", font=("Microsoft YaHei UI Light", 11))
label.place(x=407, y=605)

Button(text="Log Out", command=logout, bg='#007dfe',border=0, fg='white', font="comicsansms 14 bold").grid(row=6, column=2, padx=900, pady=20)
Button(text="View your Passlogin", command=viewpass, bg='#007dfe',border=0, fg='white', font="comicsansms 14 bold").place(x=30,  y=20)


root.mainloop()
from tkinter import*
from tkinter import messagebox
import tkinter.messagebox as tmsg
import os
import subprocess
from PIL import Image, ImageTk
import ast


root = Tk()
# root.geometry("850x670")
root_width = 850
root_height = 670

Screen_width = 1280#root.winfo_screenmmwidth()
Screen_height = 660#root.winfo_screenmmheight()

x_axis = (Screen_width / 2) - (root_width / 2)
y_axis = (Screen_height / 2) - (root_height / 2)

root.geometry("{}x{}+{}+{}".format(root_width, root_height, int(x_axis), int(y_axis)))
#======================================================================#
root.title("Paassword Saver")
#root.geometry("1025x650+300+200")
root.wm_iconbitmap("assets\paa.ico")
root.configure(bg="#fff")
root.resizable(False, False)
#-------------------------------------------------------------------------------------------#
img = Image.open("assets\sa (1).png")
#img = Image.open("assets\sa (2).png")
width, height = img.size
img = ImageTk.PhotoImage(img.resize((width, height), Image.ANTIALIAS))
Label(root, image=img, bg="white").place(x=6, y=6, relwidth=1, relheight=1)

heading = Label(root, text="Create a Account", fg="#0C3C62", bg="#aacbff", font=("Microsoft YaHei UI Light", 23, "bold"))
heading.place(x=250, y=140)

#---------------------1) hide to extra bracket----------------------------------------------------------------------------#
heading = Label(root, text="Save the password", fg="#aacbff", bg="#aacbff", font=("Microsoft YaHei UI Light", 23, "bold"))
heading.place(x=250, y=270)
#---------------------2) hide to extra bracket-----------------------------------------------------------------------------------#
heading = Label(root, text="Save the password", fg="#aacbff", bg="#aacbff", font=("Microsoft YaHei UI Light", 17, "bold"))
heading.place(x=265, y=446)
#--------------- ALL Fuction are here----------------------------#

def signup():
    username = user.get()
    password = passwordi.get()
    confirm = passwordii.get()
    if password == confirm:
        try:
            file = open('datasheet.txt','r+')
            d = file.read()
            r = ast.literal_eval(d)

            dict2 = {username:password}
            r.update(dict2)
            file.truncate()
            file.close()

            file = open('datasheet.txt', 'w')
            w = file.write(str(r))
            messagebox.showinfo('Signup', 'Successfully Sign Up')

            os.mkdir(f"User {username}")
            # Assuming "User {username}" directory already exists
            directory_name = f"User {username}"
            file_path = os.path.join(directory_name, f"{username}.txt")

            # Create the new text file
            with open(file_path, 'w') as file:
                file.write(f"This all passwords are saved by {username}\n")
            user.delete(0, 'end')
            passwordi.delete(0, 'end')
            passwordii.delete(0, 'end')    

            
        except:
            file = open('datasheet.txt', 'w')
            pp = str({'Username':'password'})
            file.write(pp)
            file.close()
    else:
        messagebox.showerror('Invalid', "Both Password should match")
def signin():
    root.destroy()
    os.system('python login.pyw')
    user.delete(0, 'end')
    passwordi.delete(0, 'end')
    passwordii.delete(0, 'end')
    pid = os.getpid()
    os.kill(pid, 9)
    
#------------------------------------------------------------------------------
def on_enter(e):
    user.delete(0, 'end')
def on_leave(e):
    if user.get() =='':
        user.insert(0, 'Username')
user = Entry(root, width=21, fg='black', border=0, bg="white", font=('Microsoft Yahei UI Light', 15))
user.place(x=270, y=220) #x=250, y=270)
user.insert(0, 'Username')
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)
Frame(root, width=262, height=2, bg='black').place(x=265, y=254)
#---------------------------------------------------------------------------------------------
def on_enter(e):
    passwordi.delete(0, 'end')
def on_leave(e):
    if passwordi.get() =='':
        passwordi.insert(0, 'Enter the Password')
passwordi = Entry(root, width=22, fg='black', border=0, bg="white", font=('Microsoft Yahei UI Light', 15))
passwordi.place(x=270, y=340)
passwordi.insert(0, 'Enter the Password')
passwordi.bind("<FocusIn>", on_enter)
passwordi.bind("<FocusOut>", on_leave)
Frame(root, width=262, height=2, bg='black').place(x=265, y=374)
#-----------------------------------------------------------------------------
def on_enter(e):
    passwordii.delete(0, 'end')
def on_leave(e):
    if passwordii.get() =='':
        passwordii.insert(0, 'Confirm Password')
passwordii = Entry(root, width=22, fg='black', border=0, bg="white", font=('Microsoft Yahei UI Light', 15))
passwordii.place(x=270, y=402)
passwordii.insert(0, 'Confirm Password')
passwordii.bind("<FocusIn>", on_enter)
passwordii.bind("<FocusOut>", on_leave)
Frame(root, width=262, height=2, bg='black').place(x=265, y=436)
#----------------------------------------------------------------------------

Button(root, width=23, pady=7, text='Sign Up', font=('Microsoft YaHei UI Light', 13, 'bold'), bg="#007dfe", fg='white', border=0, command=signup).place(x=266, y=479)

label = Label(root, text="I have an account !", fg='black', bg='#aacbff', font=('Microsoft YaHei UI Light', 10, 'bold'))
label.place(x=295, y=535)

signin = Button(root, width=6, text="Sign in", font=('Microsoft YaHei UI Light', 11, 'bold'), border =0, bg='#aacbff', cursor='hand2', fg='#0C3C62', command=signin)
signin.place(x=430, y=532)
    
label = Label(root, text="This Software is made By Krishna (Dadus) . . .  :) ", fg="black", bg="white", font=("Microsoft YaHei UI Light", 11))
label.place(x=250, y=605)




root.mainloop()
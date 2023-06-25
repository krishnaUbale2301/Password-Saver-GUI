from tkinter import*
from tkinter import messagebox
import ast

root =Tk()
root.title("Gign UP")
root.configure(bg='#fff')
root.resizable(False, False)
root.geometry('925x500+300+200')
#====================================================================
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
        except:
            file = open('datasheet.txt', 'w')
            pp = str({'Username':'password'})
            file.write(pp)
            file.close()
    else:
        messagebox.showerror('Invalid', "Both Password should match")
def sign():
    root.destroy()
    
    # if password == confirm:
    #     try:
    #         file = open('datasheet.txt','r+')
    #         d=file.read()
    #         r.ast.literal_eval(d)

    #         dict2={username:password}
    #         r.update(dict2)
    #         file.truncaste()
    #         file.close()

    #         file = open('datasheet.txt', 'w')
    #         w=file.write(str(r))
            
    #         messagebox.showinfo('Signup', 'Successfully Sign Up')
    #     except:
    #         fille = open('datasheet.txt', 'w')
    #         pp = str=str({'Username':'password'})
    #         file.write(pp)
    #         file.close()

    # else:
    #     messagebox.showerror('Invalid', "Both Password should match")
#====================================================================
img = PhotoImage(file='login.png')
Label(root, image=img, border=0, bg='white').place(x=50, y=90)

frame = Frame(root, width=350, height=390, bg="#fff")
frame.place(x=480, y=50)

heading = Label(frame, text="Sign Up", fg="#57a1f8", bg="white", font=('Microsoft Yahei UI Light', 23, 'bold'))
heading.place(x=100, y=5)
#---------------------------------------------------------------------
def on_enter(e):
    user.delete(0, 'end')
def on_leave(e):
    if user.get() =='':
        user.insert(0, 'Username')
user = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft Yahei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)
#---------------------------------------------------------------------------------------------
def on_enter(e):
    passwordi.delete(0, 'end')
def on_leave(e):
    if passwordi.get() =='':
        passwordi.insert(0, 'Enter the Password')
passwordi = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft Yahei UI Light', 11))
passwordi.place(x=30, y=150)
passwordi.insert(0, 'Enter the Password')
passwordi.bind("<FocusIn>", on_enter)
passwordi.bind("<FocusOut>", on_leave)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)
#-----------------------------------------------------------------------------
def on_enter(e):
    passwordii.delete(0, 'end')
def on_leave(e):
    if passwordii.get() =='':
        passwordii.insert(0, 'Confirm Password')
passwordii = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft Yahei UI Light', 11))
passwordii.place(x=30, y=220)
passwordii.insert(0, 'Confirm Password')
passwordii.bind("<FocusIn>", on_enter)
passwordii.bind("<FocusOut>", on_leave)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=247 )
#----------------------------------------------------------------------------

Button(frame, width=39, pady=7, text='Sign Up', bg="#57a1f8", fg='white', border=0, command=signup).place(x=35, y=280)
label = Label(frame, text="I have an account", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
label.place(x=90, y=340)

signin = Button(frame, width=6, text="Sign in", border =0, bg='white', cursor='hand2', fg='#57a1f8', command=sign)
signin.place(x=200, y=340)




root.mainloop()

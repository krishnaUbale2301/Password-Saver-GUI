# from tkinter import*

# root = Tk()

# root.geometry("400x600")

# # codes = []
# def write():
#     with open("User_1.txt") as f:
#         code = f.read()
#         # codes.append(code)  


# f0 = Frame(root, width=400, height=70).pack()
# Label(f0, text="Your Saved Passwords ", font=("lucida", 17 ,"bold")).place(x=70, y=20)


# f1 = Frame(root, width=350, height=500, pady=2, padx=2).place()
# Label(f1, text=write, padx=22, pady=22).pack(side="left")


#ginee------------------------------------->

# from tkinter import*

# root = Tk()
# root.geometry("400x600")

# def write():
#     with open("User_1.txt") as f:
#         code = f.read()
#         return code

# f0 = Frame(root, width=400, height=70)
# f0.pack()

# Label(f0, text="Your Saved Passwords ", font=("lucida", 17 ,"bold")).place(x=70, y=20)

# f1 = Frame(root, width=350, height=500)
# f1.place()

# Label(f1, text=write(), font=("lucida", 17 ,"bold")).place(x=20, y=20)

# root.mainloop()

# import tkinter as tk
#---------------------------------------chat gpt--------------------------------------#
from tkinter import*

root = Tk()
def read_file():
    try:
        with open('data\password.txt', 'r') as file:
            text = file.read()
            text_entry.insert('1.0', text)
    except FileNotFoundError:
        text_entry.insert('1.0', 'File not found.')

root.title('Text Viewer')
root.geometry("600x600")

# Create the frame
frame = Frame(root)
frame.pack(pady=10)


# Create the text widget
text_entry = Text(frame, width=72, height=33)
text_entry.pack()

# Create the button to read the file
read_button = Button(root, text='Read File', command=read_file)
read_button.pack(pady=10)

# Start the main loop
root.mainloop()







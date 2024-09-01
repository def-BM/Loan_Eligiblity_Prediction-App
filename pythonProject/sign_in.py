from tkinter import *
from tkinter import messagebox
import mysql.connector

root = Tk()
root.geometry("925x500+300+200")
root.title("Loan Eligibility Prediction App")
root.configure(bg='#00ffff')
root.resizable(False, False)

# Working of signup button
def SignUp():
    root.destroy()
    import sign_up

# Eye button to hide
def Hide():
    openeye.config(file='closeye.png')
    pin.config(show='*')
    hide_button.config(command=Show)

# Eye button to show
def Show():
    openeye.config(file='openeye.png')
    pin.config(show='')
    hide_button.config(command=Hide)

# Working of signin button and connection of database
def signin():
    if user.get()=='' or pin.get()=='':
        messagebox.showerror('Erorr','Enter username or password.')
    else:
        try:
            # Database Connection
            connection = mysql.connector.connect(host="localhost",user="root",password=r"p@$$%sql27",database='py_project')
            mycursor = connection.cursor()
        except:
            messagebox.showerror('Error','Database connectivity issue, Try again !')

        mycursor.execute('use py_project')
        mycursor.execute('select * from userdata where username=%s and password=%s',(user.get(),pin.get()))

        row = mycursor.fetchone()
        if row == None:
            messagebox.showerror('Error','Invalid username or password !')
        else:
            messagebox.showinfo('Success','Login is Successful.')
            connection.close()
            root.destroy()
            import main

# Adding Image to mian window
img1 = PhotoImage(file='l2.png')
Label(root, image=img1, bg='#00ffff').place(x=0, y=0)

img = PhotoImage(file='l1.png')
Label(root, image=img, bg='#00ffff').place(x=50, y=150)

# Adding label on window
Label(root, text="Welcome to Loan Predictor", bg='#00ffff', fg='red', font=('Microsoft YaHei UI Light', 32, 'bold')).place(x=200,y=20)

# Creating frame on window
frame = Frame(width=350, height=350, bg='#00ffff')
frame.place(x=480, y=100)

heading = Label(frame, text="Sign in", fg='#57a1f8', bg='#00ffff', font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=100, y=5)

# User Id Frame
def on_enter(e):
    if user.get() == 'Username':
        user.delete(0, 'end')
def on_leave(e):
    name = user.get()
    if name == "":
        user.insert(0, 'Username')

user = Entry(frame, width=25, fg='black',border=0, bg='#00ffff', font=('Microsoft YaHei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

# Password Frame
def on_enter(e):
    if pin.get()=='Password':
        pin.delete(0, 'end')
def on_leave(e):
    name = pin.get()
    if name == "":
        pin.insert(0, 'Password')

pin = Entry(frame, width=25, fg='black',border=0, bg='#00ffff', font=('Microsoft YaHei UI Light', 11))
pin.place(x=30, y=150)
pin.insert(0, 'Password')
pin.bind('<FocusIn>', on_enter)
pin.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2,bg='black').place(x=25, y=177)

# Eye Button
openeye = PhotoImage(file='openeye.png')
hide_button = Button(frame, image=openeye, bg='#00ffff', bd=0, activebackground='#00ffff', cursor='hand2', command= Hide)
hide_button.place(x=300, y=150)

# Sign in Button
Button(frame, width=39, pady=7, text='sign in', bg='#57a1f8', fg='white', activeforeground='white', activebackground='#57a1f8', border=0, cursor='hand2', command=signin).place(x=35, y=207)

label = Label(frame, text="Don't have an account?", fg='black', bg='#00ffff', font=('Microsoft YaHei UI Light', 9))
label.place(x=75, y=270)
# Sign up Button
sign_up = Button(frame, width=6, text='sign up', bg='#00ffff', fg='#57a1f8', activeforeground='#57a1f8', activebackground='#00ffff', border=0, cursor='hand2', command=SignUp)
sign_up.place(x=215, y=270)

root.mainloop()
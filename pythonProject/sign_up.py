from tkinter import *
from tkinter import messagebox
import mysql.connector

window = Tk()
window.geometry("925x500+300+200")
window.title("Loan Eligibility Prediction App")
window.configure(bg='#00ffff')
window.resizable(False, False)

def clear():
    user.delete(0,'end')
    pin.delete(0,'end')
    con_pin.delete(0,'end')

# Database Connectivity and signup page working
def Database():
    # conditions to check while entering the username and password
    if user.get() == '' or pin.get() == '' or con_pin.get() == '':
        messagebox.showerror('Error','Fill all the informations.')
    elif user.get() == 'Username' or pin.get() == 'Password':
        messagebox.showerror('Error', 'Fill all the informations.')
    elif pin.get() != con_pin.get():
        messagebox.showerror('Error','Conform password is not match.')
    elif len(pin.get()) < 8:
        messagebox.showerror('Erorr','Password must be of 8 digit.')
    else:
        # connection of database
        try:
            connection = mysql.connector.connect(host="localhost",user="root",password=r"p@$$%sql27",database='py_project')
            mycursor = connection.cursor()
        except:
            messagebox.showerror('Error','Database connectivity issue, Try again !')
            return

        # Creating Table userdata
        try:
           mycursor.execute('''CREATE TABLE userdata (
            username VARCHAR(255) NOT NULL,password VARCHAR(255) NOT NULL,
            CONSTRAINT chk_password_length CHECK (LENGTH(password) >= 8),
            CONSTRAINT unique_password UNIQUE (password))''')
        except:
            mycursor.execute('use py_project')
        
        mycursor.execute('select * from userdata where username=%s',(user.get(),))

        row = mycursor.fetchone()
        if row != None:
            messagebox.showerror('Error','Username already exist.')
        else:
            # Inserting Values into table
            mycursor.execute('insert into UserData(username,password) values(%s, %s)',(user.get(), pin.get()))
            connection.commit()
            connection.close()
            messagebox.showinfo('Success','Registration is successful.')
            clear()
            window.destroy()
            import sign_in

# Working of Back Button
def SignIn():
    window.destroy()
    import sign_in

# Adding image to main window
img = PhotoImage(file='signup.png')
Label(window, image=img, bg='#00ffff', border=0).place(x=50, y=50)

# Creating a Frame on window
frame = Frame(window, width=350, height=390, bg='#00ffff')
frame.place(x=480, y=50)

heading = Label(frame, text="Sign up", fg='#57a1f8', bg='#00ffff', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100, y=5)

# User Id Frame
def on_enter(e):
    if user.get()=='Username':
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
Frame(frame, width=295, height=2,bg='black').place(x=25, y=107)

# Password Frame
def on_enter(e):
    if pin.get()=='Password':
        pin.delete(0,'end')

def on_leave(e):
    name = pin.get()
    if name == "":
        pin.insert(0, 'Password')

pin = Entry(frame, width=25, fg='black', border=0, bg='#00ffff', font=('Microsoft YaHei UI Light', 11))
pin.place(x=30, y=150)
pin.insert(0, 'Password')
pin.bind('<FocusIn>', on_enter)
pin.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

# Confirm Password
def on_enter(e):
    if con_pin.get()=='Conform Password':
        con_pin.delete(0, 'end')

def on_leave(e):
    name = con_pin.get()
    if name == "":
        con_pin.insert(0, 'Conform Password')

con_pin = Entry(frame, width=25, fg='black',border=0, bg='#00ffff', font=('Microsoft YaHei UI Light', 11))
con_pin.place(x=30, y=220)
con_pin.insert(0, 'Conform Password')
con_pin.bind('<FocusIn>', on_enter)
con_pin.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=247)

# Sign Up Button
Button(frame, width=39, pady=7, text='sign up', bg='#57a1f8', fg='white', activebackground='#57a1f8', activeforeground='white', border=0, command=Database).place(x=35, y=280)

# Back Button
back = Button(window, text='🡐', bg='#00ffff', fg='black', activebackground='#00ffff', border=0, cursor='hand2', font=(20), command=SignIn)
back.place(x=0, y=5)

# Tips for user to create password
label1=Label(window,text='• Create a Strong Password. ', font=('Microsoft YaHei UI Light', 11),bg='#00ffff',fg='red')
label1.place(x=50,y=330)
label2=Label(window,text='• Password Should contain 8 digit. ', font=('Microsoft YaHei UI Light', 11),bg='#00ffff',fg='red')
label2.place(x=50,y=360)
label3=Label(window,text='• Password contain some special charecter. eg. !@#$%^&* ', font=('Microsoft YaHei UI Light', 11),bg='#00ffff',fg='red')
label3.place(x=50,y=390)
label4=Label(window,text='• Remeber your password. ', font=('Microsoft YaHei UI Light', 11),bg='#00ffff',fg='red')
label4.place(x=50,y=420)

window.mainloop()
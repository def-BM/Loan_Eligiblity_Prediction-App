from tkinter import *
from tkinter import messagebox
import mysql.connector

# ----------------- CONFIG -----------------
BG_COLOR = "#e3f2fd"
CARD_COLOR = "#ffffff"
ACCENT = "#1976d2"
TEXT_DARK = "#0d47a1"

window = Tk()
window.geometry("925x500+300+200")
window.title("Loan Eligibility Prediction App - Sign Up")
window.configure(bg=BG_COLOR)
window.resizable(False, False)

# ----------------- HELPERS -----------------
def clear():
    user_entry.delete(0, 'end')
    pwd_entry.delete(0, 'end')
    cpwd_entry.delete(0, 'end')

def create_table_if_not_exists(cursor):
    # Simple, clean table structure
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS userdata (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) NOT NULL UNIQUE,
            password VARCHAR(255) NOT NULL
        )
    """)

# ----------------- DB & SIGNUP LOGIC -----------------
def Database():
    username = user_entry.get().strip()
    pwd = pwd_entry.get().strip()
    cpwd = cpwd_entry.get().strip()

    # Basic validations
    if username == '' or pwd == '' or cpwd == '':
        messagebox.showerror('Error', 'Fill all the information.')
        return
    if pwd != cpwd:
        messagebox.showerror('Error', 'Confirm password does not match.')
        return
    if len(pwd) < 8:
        messagebox.showerror('Error', 'Password must be at least 8 characters.')
        return

    # Connect to DB
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=r"p@$$%sql27",
            database='py_project'
        )
        mycursor = connection.cursor()
    except Exception as e:
        messagebox.showerror('Error', f'Database connectivity issue:\n{e}')
        return

    # Ensure table exists
    create_table_if_not_exists(mycursor)

    # Check if username already exists
    mycursor.execute('SELECT * FROM userdata WHERE username = %s', (username,))
    row = mycursor.fetchone()
    if row is not None:
        messagebox.showerror('Error', 'Username already exists.')
        connection.close()
        return

    # Insert new user
    mycursor.execute(
        'INSERT INTO userdata(username, password) VALUES (%s, %s)',
        (username, pwd)
    )
    connection.commit()
    connection.close()

    messagebox.showinfo('Success', 'Registration successful.')
    clear()
    window.destroy()
    import sign_in  # go back to login screen

# ----------------- BACK TO SIGN IN -----------------
def go_to_signin():
    window.destroy()
    import sign_in

# ----------------- UI SETUP -----------------

# Left side illustration / tips
left_frame = Frame(window, bg=BG_COLOR)
left_frame.place(x=0, y=0, relheight=1, width=420)

try:
    img = PhotoImage(file='signup.png')
    Label(left_frame, image=img, bg=BG_COLOR, border=0).place(x=40, y=60)
except Exception:
    # if image not found, no crash
    Label(left_frame, text="Loan Eligibility\nPrediction App",
          font=('Microsoft YaHei UI Light', 20, 'bold'),
          bg=BG_COLOR, fg=TEXT_DARK).place(x=50, y=120)

Label(left_frame, text='• Create a strong password',
      font=('Microsoft YaHei UI Light', 11),
      bg=BG_COLOR, fg='red').place(x=50, y=330)

Label(left_frame, text='• Password should be at least 8 characters',
      font=('Microsoft YaHei UI Light', 11),
      bg=BG_COLOR, fg='red').place(x=50, y=360)

Label(left_frame, text='• Use some special characters e.g. !@#$%^&*',
      font=('Microsoft YaHei UI Light', 11),
      bg=BG_COLOR, fg='red').place(x=50, y=390)

Label(left_frame, text='• Remember your password',
      font=('Microsoft YaHei UI Light', 11),
      bg=BG_COLOR, fg='red').place(x=50, y=420)

# Right side card for form
card = Frame(window, width=420, height=420, bg=CARD_COLOR, bd=0, highlightthickness=0)
card.place(x=460, y=40)

heading = Label(card, text="Create Account",
                fg=TEXT_DARK, bg=CARD_COLOR,
                font=('Microsoft YaHei UI Light', 22, 'bold'))
heading.place(x=105, y=20)

# Username
Label(card, text="Username", bg=CARD_COLOR, fg='gray25',
      font=('Microsoft YaHei UI Light', 11)).place(x=40, y=90)

user_entry = Entry(card, width=30, fg='black', border=0,
                   bg=CARD_COLOR, font=('Microsoft YaHei UI Light', 11))
user_entry.place(x=40, y=115)
Frame(card, width=320, height=1, bg='gray70').place(x=40, y=137)

# Password
Label(card, text="Password", bg=CARD_COLOR, fg='gray25',
      font=('Microsoft YaHei UI Light', 11)).place(x=40, y=155)

pwd_entry = Entry(card, width=30, fg='black', border=0,
                  bg=CARD_COLOR, font=('Microsoft YaHei UI Light', 11), show='*')
pwd_entry.place(x=40, y=180)
Frame(card, width=320, height=1, bg='gray70').place(x=40, y=202)

# Confirm password
Label(card, text="Confirm Password", bg=CARD_COLOR, fg='gray25',
      font=('Microsoft YaHei UI Light', 11)).place(x=40, y=220)

cpwd_entry = Entry(card, width=30, fg='black', border=0,
                   bg=CARD_COLOR, font=('Microsoft YaHei UI Light', 11), show='*')
cpwd_entry.place(x=40, y=245)
Frame(card, width=320, height=1, bg='gray70').place(x=40, y=267)

# Sign up button
signup_btn = Button(card, width=32, pady=8, text='Sign up',
                    bg=ACCENT, fg='white', activebackground=ACCENT,
                    activeforeground='white', border=0,
                    font=('Microsoft YaHei UI Light', 11, 'bold'),
                    cursor='hand2', command=Database)
signup_btn.place(x=40, y=300)

# Already a user?
Label(card, text="Already have an account?",
      bg=CARD_COLOR, fg='gray25',
      font=('Microsoft YaHei UI Light', 10)).place(x=85, y=350)

signin_btn = Button(card, text="Sign in",
                    bg=CARD_COLOR, fg=ACCENT, border=0,
                    font=('Microsoft YaHei UI Light', 10, 'bold'),
                    cursor='hand2', command=go_to_signin)
signin_btn.place(x=250, y=347)

# Back arrow (top-left)
back = Button(window, text='🡐', bg=BG_COLOR, fg='black',
              activebackground=BG_COLOR, border=0,
              cursor='hand2', font=("Arial", 18, "bold"),
              command=go_to_signin)
back.place(x=5, y=5)

window.mainloop()
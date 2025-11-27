from tkinter import *
from tkinter import messagebox
import mysql.connector

# ----------------- CONFIG -----------------
BG_COLOR = "#e3f2fd"
CARD_COLOR = "#ffffff"
ACCENT = "#1976d2"
TEXT_DARK = "#0d47a1"

root = Tk()
root.geometry("925x500+300+200")
root.title("Loan Eligibility Prediction App - Sign In")
root.configure(bg=BG_COLOR)
root.resizable(False, False)

# ----------------- NAVIGATION -----------------
def go_to_signup():
    root.destroy()
    import sign_up

# ----------------- EYE BUTTON HANDLERS -----------------
def hide_password():
    try:
        eye_img.config(file='closeye.png')
    except Exception:
        pass
    pwd_entry.config(show='*')
    eye_button.config(command=show_password)

def show_password():
    try:
        eye_img.config(file='openeye.png')
    except Exception:
        pass
    pwd_entry.config(show='')
    eye_button.config(command=hide_password)

# ----------------- SIGN IN LOGIC -----------------
def signin():
    username = user_entry.get().strip()
    pwd = pwd_entry.get().strip()

    if username == '' or pwd == '':
        messagebox.showerror('Error', 'Enter username and password.')
        return

    try:
        # Database Connection
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

    try:
        mycursor.execute(
            'SELECT * FROM userdata WHERE username=%s AND password=%s',
            (username, pwd)
        )
        row = mycursor.fetchone()
    except Exception as e:
        messagebox.showerror('Error', f'Query failed:\n{e}')
        connection.close()
        return

    if row is None:
        messagebox.showerror('Error', 'Invalid username or password!')
        connection.close()
    else:
        messagebox.showinfo('Success', 'Login successful.')
        connection.close()
        root.destroy()
        import main   # open main loan prediction window

# ----------------- UI: LEFT SIDE -----------------

left_frame = Frame(root, bg=BG_COLOR)
left_frame.place(x=0, y=0, relheight=1, width=420)

# Only heading and one illustration image (no overlapping)
Label(left_frame,
      text="Welcome to\nLoan Predictor",
      bg=BG_COLOR,
      fg=TEXT_DARK,
      font=('Microsoft YaHei UI Light', 26, 'bold')
      ).place(x=60, y=40)

try:
    # your main illustration
    img_illustration = PhotoImage(file='l1.png')
    Label(left_frame, image=img_illustration, bg=BG_COLOR).place(x=40, y=150)
except Exception:
    # fallback if image not found
    Label(left_frame,
          text="(Image not found)",
          bg=BG_COLOR,
          fg="gray",
          font=('Microsoft YaHei UI Light', 10)
          ).place(x=40, y=180)

# ----------------- UI: RIGHT SIDE CARD -----------------

card = Frame(root, width=420, height=380, bg=CARD_COLOR, bd=0, highlightthickness=0)
card.place(x=460, y=60)

heading = Label(card, text="Sign In",
                fg=TEXT_DARK, bg=CARD_COLOR,
                font=('Microsoft YaHei UI Light', 22, 'bold'))
heading.place(x=150, y=20)

# Username label + entry
Label(card, text="Username",
      bg=CARD_COLOR, fg='gray25',
      font=('Microsoft YaHei UI Light', 11)
      ).place(x=40, y=90)

user_entry = Entry(card, width=30, fg='black', border=0,
                   bg=CARD_COLOR, font=('Microsoft YaHei UI Light', 11))
user_entry.place(x=40, y=115)
Frame(card, width=320, height=1, bg='gray70').place(x=40, y=137)

# Password label + entry
Label(card, text="Password",
      bg=CARD_COLOR, fg='gray25',
      font=('Microsoft YaHei UI Light', 11)
      ).place(x=40, y=160)

pwd_entry = Entry(card, width=25, fg='black', border=0,
                  bg=CARD_COLOR, font=('Microsoft YaHei UI Light', 11),
                  show='*')
pwd_entry.place(x=40, y=185)
Frame(card, width=320, height=1, bg='gray70').place(x=40, y=207)

# Eye button for password show/hide
try:
    eye_img = PhotoImage(file='openeye.png')
except Exception:
    eye_img = PhotoImage()  # empty if not found

eye_button = Button(card, image=eye_img,
                    bg=CARD_COLOR, bd=0,
                    activebackground=CARD_COLOR,
                    cursor='hand2', command=hide_password)
eye_button.place(x=330, y=178)

# Sign in button
signin_btn = Button(card, width=32, pady=8, text='Sign in',
                    bg=ACCENT, fg='white',
                    activebackground=ACCENT,
                    activeforeground='white',
                    border=0, cursor='hand2',
                    font=('Microsoft YaHei UI Light', 11, 'bold'),
                    command=signin)
signin_btn.place(x=40, y=240)

# Sign up text + button
Label(card, text="Don't have an account?",
      bg=CARD_COLOR, fg='gray25',
      font=('Microsoft YaHei UI Light', 10)
      ).place(x=85, y=295)

signup_btn = Button(card, text="Sign up",
                    bg=CARD_COLOR, fg=ACCENT,
                    border=0, cursor='hand2',
                    font=('Microsoft YaHei UI Light', 10, 'bold'),
                    command=go_to_signup)
signup_btn.place(x=250, y=292)

# Back arrow (top-left)
back = Button(root, text='🡐', bg=BG_COLOR, fg='black',
              activebackground=BG_COLOR, border=0,
              cursor='hand2', font=("Arial", 18, "bold"),
              command=go_to_signup)
back.place(x=5, y=5)

root.mainloop()
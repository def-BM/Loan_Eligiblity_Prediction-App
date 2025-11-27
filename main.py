from tkinter import *
from tkinter import messagebox
import pandas as pd
import joblib
import re

# ----------------- CONFIG -----------------
BG_COLOR = "#e3f2fd"
CARD_COLOR = "#ffffff"
ACCENT = "#1976d2"
TEXT_DARK = "#0d47a1"

# ----------------- LOAD TRAINED MODEL -----------------
# These files should be created by your notebook training code
model = joblib.load("loan_eligibility_model.pkl")
scaler = joblib.load("loan_scaler.pkl")
feature_names = joblib.load("model_features.pkl")   # list/Index of columns after get_dummies

# ----------------- MAIN WINDOW -----------------
bm = Tk()
bm.geometry("1000x600+260+100")
bm.title("Loan Eligibility Prediction App")
bm.configure(bg=BG_COLOR)
bm.resizable(False, False)

title_lbl = Label(
    bm, text="Loan Eligibility Form",
    bg=BG_COLOR, fg=TEXT_DARK,
    font=('Microsoft YaHei UI Light', 24, 'bold')
)
title_lbl.place(x=340, y=20)

# Main card frame
form = Frame(bm, width=920, height=480, bg=CARD_COLOR, bd=0, highlightthickness=0)
form.place(x=40, y=80)

# ----------------- CHECK BUTTON LOGIC -----------------
def Check():
    # Basic empty checks
    if (loan_id.get().strip() == '' or
        name.get().strip() == '' or
        name2.get().strip() == '' or
        age.get().strip() == '' or
        gender.get().strip() == '' or
        dependent.get().strip() == '' or
        applicant_salary.get().strip() == '' or
        coapplicant_salary.get().strip() == '' or
        loan_amount.get().strip() == '' or
        term.get().strip() == '' or
        married_var.get() == 0 or
        occupation_var.get() == 0 or
        edu_var.get() == 0 or
        credit_var.get() == 0 or
        area_var.get() == 0):
        messagebox.showerror('Error', 'Fill all the information.')
        return

    # Numeric validations
    try:
        age_val = int(age.get())
        app_inc = float(applicant_salary.get())
        coapp_inc = float(coapplicant_salary.get())
        loan_amt = float(loan_amount.get())
        term_years = float(term.get())
    except ValueError:
        messagebox.showerror('Error', 'Age, incomes, loan amount and term must be numeric.')
        return

    total_income = app_inc + coapp_inc

    if age_val < 18 or age_val > 70:
        messagebox.showerror('Error', 'You are not eligible due to age limit.')
        return

    # Loan ID pattern check
    if not re.match(r'^LP\d{6}$', loan_id.get().strip()):
        messagebox.showerror('Error', 'Please enter correct Loan ID (e.g. LP123456).')
        return

    # -------- MAP RADIO VALUES TO ORIGINAL CATEGORIES --------
    married_val = 'Yes' if married_var.get() == 1 else 'No'

    edu_val = 'Graduate' if edu_var.get() == 1 else 'Not Graduate'

    self_emp_val = 'Yes' if occupation_var.get() == 1 else 'No'

    credit_hist_val = 1.0 if credit_var.get() == 1 else 0.0

    if area_var.get() == 1:
        area_val = 'Urban'
    elif area_var.get() == 2:
        area_val = 'Semiurban'
    else:
        area_val = 'Rural'

    # Loan term: form is in YEARS, dataset in MONTHS
    term_months = term_years * 12

    gender_val = gender.get().strip().title()  # "Male"/"Female" etc.

    # -------- BUILD USER ROW (same columns as original data before dummies) --------
    user_raw = {
        'Gender': gender_val,
        'Married': married_val,
        'Dependents': dependent.get().strip(),   # "0","1","2","3+"
        'Education': edu_val,
        'Self_Employed': self_emp_val,
        'ApplicantIncome': app_inc,
        'CoapplicantIncome': coapp_inc,
        'LoanAmount': loan_amt,
        'Loan_Amount_Term': term_months,
        'Credit_History': credit_hist_val,
        'Property_Area': area_val
    }

    user_df = pd.DataFrame([user_raw])

    # -------- APPLY SAME ONE-HOT ENCODING --------
    user_encoded = pd.get_dummies(user_df, drop_first=True)

    # Add any missing columns (set to 0), ensure same order as training
    for col in feature_names:
        if col not in user_encoded.columns:
            user_encoded[col] = 0

    user_encoded = user_encoded[feature_names]

    # -------- SCALE & PREDICT --------
    user_scaled = scaler.transform(user_encoded)
    pred = model.predict(user_scaled)[0]

    # If your model supports predict_proba, you can show confidence too:
    try:
        proba = model.predict_proba(user_scaled)[0][1] * 100
        msg = f"Loan Status: {'Eligible ✅' if pred == 1 else 'Not Eligible ❌'}\n\nModel confidence: {proba:.1f}%"
    except Exception:
        msg = f"Loan Status: {'Eligible ✅' if pred == 1 else 'Not Eligible ❌'}"

    messagebox.showinfo('Result', msg)

# ----------------- FORM WIDGETS -----------------

# Row 1: First name, Last name, Loan ID
label1 = Label(form, text='First Name', bg=CARD_COLOR, fg='black',
               font=('Microsoft YaHei UI Light', 11, 'bold'))
label1.place(x=20, y=10)
name = Entry(form, width=25, fg='black', border=1, bg='white',
             font=('Microsoft YaHei UI Light', 11))
name.place(x=20, y=40)

label2 = Label(form, text='Last Name', bg=CARD_COLOR, fg='black',
               font=('Microsoft YaHei UI Light', 11, 'bold'))
label2.place(x=320, y=10)
name2 = Entry(form, width=25, fg='black', border=1, bg='white',
              font=('Microsoft YaHei UI Light', 11))
name2.place(x=320, y=40)

label3 = Label(form, text='Loan ID (e.g. LP123456)', bg=CARD_COLOR, fg='black',
               font=('Microsoft YaHei UI Light', 11, 'bold'))
label3.place(x=620, y=10)
loan_id = Entry(form, width=25, fg='black', border=1, bg='white',
                font=('Microsoft YaHei UI Light', 11))
loan_id.place(x=620, y=40)

# Row 2: Age, Married, Gender
label4 = Label(form, text='Age', bg=CARD_COLOR, fg='black',
               font=('Microsoft YaHei UI Light', 11, 'bold'))
label4.place(x=20, y=90)
age = Entry(form, width=25, fg='black', border=1, bg='white',
            font=('Microsoft YaHei UI Light', 11))
age.place(x=20, y=120)

married_var = IntVar()
label5 = Label(form, text='Married', bg=CARD_COLOR, fg='black',
               font=('Microsoft YaHei UI Light', 11, 'bold'))
label5.place(x=320, y=90)
Radiobutton(form, text='Yes', variable=married_var, value=1,
            bg=CARD_COLOR, fg='black',
            activebackground=CARD_COLOR,
            font=('Microsoft YaHei UI Light', 9, 'bold')).place(x=320, y=120)
Radiobutton(form, text='No', variable=married_var, value=2,
            bg=CARD_COLOR, fg='black',
            activebackground=CARD_COLOR,
            font=('Microsoft YaHei UI Light', 9, 'bold')).place(x=390, y=120)

label6 = Label(form, text='Gender (Male/Female)', bg=CARD_COLOR, fg='black',
               font=('Microsoft YaHei UI Light', 11, 'bold'))
label6.place(x=620, y=90)
gender = Entry(form, width=25, fg='black', border=1, bg='white',
               font=('Microsoft YaHei UI Light', 11))
gender.place(x=620, y=120)

# Row 3: Self-employed, Applicant Income, Coapplicant Income
occupation_var = IntVar()
label7 = Label(form, text='Self Employed', bg=CARD_COLOR, fg='black',
               font=('Microsoft YaHei UI Light', 11, 'bold'))
label7.place(x=20, y=170)
Radiobutton(form, text='Yes', variable=occupation_var, value=1,
            bg=CARD_COLOR, fg='black',
            activebackground=CARD_COLOR,
            font=('Microsoft YaHei UI Light', 9, 'bold')).place(x=20, y=200)
Radiobutton(form, text='No', variable=occupation_var, value=2,
            bg=CARD_COLOR, fg='black',
            activebackground=CARD_COLOR,
            font=('Microsoft YaHei UI Light', 9, 'bold')).place(x=100, y=200)

label8 = Label(form, text='Applicant Income (in Rs.)', bg=CARD_COLOR, fg='black',
               font=('Microsoft YaHei UI Light', 11, 'bold'))
label8.place(x=320, y=170)
applicant_salary = Entry(form, width=25, fg='black', border=1, bg='white',
                         font=('Microsoft YaHei UI Light', 11))
applicant_salary.place(x=320, y=200)

label9 = Label(form, text='Coapplicant Income (in Rs.)', bg=CARD_COLOR, fg='black',
               font=('Microsoft YaHei UI Light', 11, 'bold'))
label9.place(x=620, y=170)
coapplicant_salary = Entry(form, width=25, fg='black', border=1, bg='white',
                           font=('Microsoft YaHei UI Light', 11))
coapplicant_salary.place(x=620, y=200)

# Row 4: Education, Dependents, Loan Amount
edu_var = IntVar()
label10 = Label(form, text='Education', bg=CARD_COLOR, fg='black',
                font=('Microsoft YaHei UI Light', 11, 'bold'))
label10.place(x=20, y=250)
Radiobutton(form, text='Graduate', variable=edu_var, value=1,
            bg=CARD_COLOR, fg='black',
            activebackground=CARD_COLOR,
            font=('Microsoft YaHei UI Light', 9, 'bold')).place(x=20, y=280)
Radiobutton(form, text='Not Graduate', variable=edu_var, value=2,
            bg=CARD_COLOR, fg='black',
            activebackground=CARD_COLOR,
            font=('Microsoft YaHei UI Light', 9, 'bold')).place(x=120, y=280)

label11 = Label(form, text='Dependents (0/1/2/3+)', bg=CARD_COLOR, fg='black',
                font=('Microsoft YaHei UI Light', 11, 'bold'))
label11.place(x=320, y=250)
dependent = Entry(form, width=25, fg='black', border=1, bg='white',
                  font=('Microsoft YaHei UI Light', 11))
dependent.place(x=320, y=280)

label12 = Label(form, text='Loan Amount', bg=CARD_COLOR, fg='black',
                font=('Microsoft YaHei UI Light', 11, 'bold'))
label12.place(x=620, y=250)
loan_amount = Entry(form, width=25, fg='black', border=1, bg='white',
                    font=('Microsoft YaHei UI Light', 11))
loan_amount.place(x=620, y=280)

# Row 5: Term, Credit History, Property Area
label13 = Label(form, text='Loan Amount Term (in years)', bg=CARD_COLOR, fg='black',
                font=('Microsoft YaHei UI Light', 11, 'bold'))
label13.place(x=20, y=330)
term = Entry(form, width=25, fg='black', border=1, bg='white',
             font=('Microsoft YaHei UI Light', 11))
term.place(x=20, y=360)

credit_var = IntVar()
label15 = Label(form, text='Credit History', bg=CARD_COLOR, fg='black',
                font=('Microsoft YaHei UI Light', 11, 'bold'))
label15.place(x=320, y=330)
Radiobutton(form, text='1', variable=credit_var, value=1,
            bg=CARD_COLOR, fg='black',
            activebackground=CARD_COLOR,
            font=('Microsoft YaHei UI Light', 9, 'bold')).place(x=320, y=360)
Radiobutton(form, text='0', variable=credit_var, value=2,
            bg=CARD_COLOR, fg='black',
            activebackground=CARD_COLOR,
            font=('Microsoft YaHei UI Light', 9, 'bold')).place(x=370, y=360)

area_var = IntVar()
label16 = Label(form, text='Property Area', bg=CARD_COLOR, fg='black',
                font=('Microsoft YaHei UI Light', 11, 'bold'))
label16.place(x=620, y=330)
Radiobutton(form, text='Urban', variable=area_var, value=1,
            bg=CARD_COLOR, fg='black',
            activebackground=CARD_COLOR,
            font=('Microsoft YaHei UI Light', 9, 'bold')).place(x=620, y=360)
Radiobutton(form, text='Semiurban', variable=area_var, value=2,
            bg=CARD_COLOR, fg='black',
            activebackground=CARD_COLOR,
            font=('Microsoft YaHei UI Light', 9, 'bold')).place(x=710, y=360)
Radiobutton(form, text='Rural', variable=area_var, value=3,
            bg=CARD_COLOR, fg='black',
            activebackground=CARD_COLOR,
            font=('Microsoft YaHei UI Light', 9, 'bold')).place(x=820, y=360)

# Check Button
check = Button(
    bm, text='Check Eligibility', width=25, pady=8,
    bg=ACCENT, fg='white',
    activeforeground='white', activebackground=ACCENT,
    border=0, cursor='hand2',
    font=('Microsoft YaHei UI Light', 11, 'bold'),
    command=Check
)
check.place(x=380, y=550)

bm.mainloop()
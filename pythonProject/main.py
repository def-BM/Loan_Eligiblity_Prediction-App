from tkinter import *
from tkinter import messagebox
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import re

bm = Tk()
bm.geometry("925x500+300+200")
bm.title("Loan Eligibility Prediction App")
bm.configure(bg='#00ffff')
bm.resizable(False, False)

# Working on Check Button
def Check():
    amount = float(applicant_salary.get()) + float(coapplicant_salary.get())

    if loan_id.get() =='' or gender.get() =='' or married_var.get() =='' or dependent.get() =='' or edu_var.get()=='' or occupation_var.get()=='' or applicant_salary.get()=='' or coapplicant_salary.get()=='' or loan_amount.get()=='' or term.get()=='' or credit_var.get()=='' or area_var.get()=='' or name.get()=='' or name2.get()=='' or age.get()=='':
        messagebox.showerror('Error', 'Fill all the information.')
    elif int(age.get())<18 or int(age.get())>70:
        messagebox.showerror('Error','You are not eligible due to age limit.')
    elif not re.match(r'^LP\d{6}$', loan_id.get()) :
        messagebox.showerror('Error','Please enter correct loan id')
    elif float(loan_amount.get()) > 10 * amount:
        messagebox.showerror('Error','You are not eligible, your income is insufficient.')
    else:
        # Load the dataset
        data = pd.read_csv('train.csv')

        # Convert categorical variables into numerical variables using one-hot encoding
        data = pd.get_dummies(data, columns=['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed','Property_Area'])

        # Fill missing values
        data['LoanAmount'].fillna(data['LoanAmount'].mean(), inplace=True)
        data['Loan_Amount_Term'].fillna(data['Loan_Amount_Term'].mean(), inplace=True)
        data['Credit_History'].fillna(data['Credit_History'].mode()[0], inplace=True)

        # Split features and target variable
        X = data.drop(columns=['Loan_ID', 'Loan_Status'])
        y = data['Loan_Status']

        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train the model
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        # Function to predict eligibility of a user
        def predict_eligibility(user_data):
            # Preprocess user data
            user_df = pd.DataFrame([user_data], columns=X.columns)
            # user_df = pd.get_dummies(user_df)

            # Ensure the user data has the same columns as the training data
            missing_cols = set(X.columns) - set(user_df.columns)
            for col in missing_cols:
                user_df[col] = 0

            # Make prediction
            prediction = model.predict(user_df)
            return prediction[0]

        # user data usage
        user_data = {'Loan_ID': loan_id.get(), 'Gender': gender.get(), 'Married': married_var.get(),'Dependents': dependent.get(), 'Education': edu_var.get(), 'Self_Employed': occupation_var.get(),
                     'ApplicantIncome': applicant_salary.get(), 'CoapplicantIncome': coapplicant_salary.get(), 'LoanAmount': loan_amount.get(), 'Loan_Amount_Term': term.get(),
                     'Credit_History': credit_var.get(), 'Property_Area': area_var.get()}

        eligibility = predict_eligibility(user_data)
        messagebox.showinfo('Information',f'Is eligible? {eligibility}')


label1= Label(bm, text='First Name ',bg='#00ffff', fg='black', font=('Microsoft YaHei UI Light', 11, 'bold')).place(x=10,y=0)
name = Entry(bm, width=25, fg='black',border=1, bg='white', font=('Microsoft YaHei UI Light', 11))
name.place(x=10, y=30)
Frame(bm, width=204, height=1, bg='black').place(x=10, y=55)

label2= Label(bm, text='Last Name', bg='#00ffff', fg='black', font=('Microsoft YaHei UI Light', 11, 'bold')).place(x=300,y=0)
name2 = Entry(bm, width=25, fg='black',border=1, bg='white', font=('Microsoft YaHei UI Light', 11))
name2.place(x=300, y=30)
Frame(bm, width=204, height=1, bg='black').place(x=300, y=55)

label3= Label(bm, text='Loan Id (eg. LPxxxxxx)', bg='#00ffff', fg='black', font=('Microsoft YaHei UI Light', 11, 'bold')).place(x=600,y=0)
loan_id = Entry(bm, width=25, fg='black',border=1, bg='white', font=('Microsoft YaHei UI Light', 11))
loan_id.place(x=600, y=30)
Frame(bm, width=204, height=1, bg='black').place(x=600, y=55)

label4= Label(bm, text='Age', bg='#00ffff', fg='black', font=('Microsoft YaHei UI Light', 11, 'bold')).place(x=10,y=100)
age = Entry(bm, width=25, fg='black',border=1, bg='white', font=('Microsoft YaHei UI Light', 11))
age.place(x=10, y=130)
Frame(bm, width=204, height=1, bg='black').place(x=10, y=155)

married_var= IntVar()
label5= Label(bm, text='Married', bg='#00ffff', fg='black', font=('Microsoft YaHei UI Light', 11, 'bold')).place(x=300,y=100)
married= Radiobutton(bm, text='Yes', variable=married_var, value=1, bg='#00ffff', fg='black',activebackground='#00ffff', font=('Microsoft YaHei UI Light', 9, 'bold')).place(x=300, y=130)
married= Radiobutton(bm, text='No', variable=married_var, value=2, bg='#00ffff', fg='black', activebackground='#00ffff', font=('Microsoft YaHei UI Light', 9, 'bold')).place(x=380, y=130)

label6= Label(bm, text='Gender', bg='#00ffff', fg='black', font=('Microsoft YaHei UI Light', 11, 'bold')).place(x=600,y=100)
gender = Entry(bm, width=25, fg='black',border=1, bg='white', font=('Microsoft YaHei UI Light', 11))
gender.place(x=600, y=130)
Frame(bm, width=204, height=1, bg='black').place(x=600, y=155)

occupation_var = IntVar()
label7= Label(bm, text='Self Employed', bg='#00ffff', fg='black', font=('Microsoft YaHei UI Light', 11, 'bold')).place(x=10,y=200)
occupation= Radiobutton(bm, text='Yes', variable=occupation_var, value=1, bg='#00ffff', fg='black', activebackground='#00ffff', font=('Microsoft YaHei UI Light', 9, 'bold')).place(x=10, y=230)
occupation= Radiobutton(bm, text='No', variable=occupation_var, value=2, bg='#00ffff', fg='black', activebackground='#00ffff', font=('Microsoft YaHei UI Light', 9, 'bold')).place(x=90, y=230)


label8= Label(bm, text='Applicant Income', bg='#00ffff', fg='black', font=('Microsoft YaHei UI Light', 11, 'bold')).place(x=300,y=200)
applicant_salary = Entry(bm, width=25, fg='black', border=1, bg='white', font=('Microsoft YaHei UI Light', 11))
applicant_salary.place(x=300, y=230)
Frame(bm, width=204, height=1, bg='black').place(x=300, y=255)

label9= Label(bm, text='Coaaplicant Income',bg='#00ffff',fg='black', font=('Microsoft YaHei UI Light', 11, 'bold')).place(x=600, y=200)
coapplicant_salary = Entry(bm, width=25, fg='black', border=1, bg='white', font=('Microsoft YaHei UI Light', 11))
coapplicant_salary.place(x=600, y=230)
Frame(bm, width=204, height=1, bg='black').place(x=600, y=255)

edu_var = IntVar()
label10= Label(bm, text='Education', fg='black', bg='#00ffff', font=('Microsoft YaHei UI Light', 11, 'bold')).place(x=10, y=300)
edu = Radiobutton(bm, text='Graduated', variable=edu_var, value=1, bg='#00ffff', fg='black', activebackground='#00ffff', font=('Microsoft YaHei UI Light', 9, 'bold')).place(x=10, y=330)
edu = Radiobutton(bm, text='Not Graduated', variable=edu_var, value=2, bg='#00ffff', fg='black', activebackground='#00ffff', font=('Microsoft YaHei UI Light', 9, 'bold')).place(x=120, y=330)

label11= Label(bm, text='Dependents', bg='#00ffff', fg='black', font=('Microsoft YaHei UI Light', 11, 'bold')).place(x=300,y=300)
dependent = Entry(bm, width=25, fg='black', border=1, bg='white', font=('Microsoft YaHei UI Light', 11))
dependent.place(x=300, y=330)
Frame(bm, width=204, height=1, bg='black').place(x=300, y=355)

label12= Label(bm, text='Loan Amount', bg='#00ffff', fg='black', font=('Microsoft YaHei UI Light', 11, 'bold')).place(x=600,y=300)
loan_amount = Entry(bm, width=25, fg='black', border=1, bg='white', font=('Microsoft YaHei UI Light', 11))
loan_amount.place(x=600, y=330)
Frame(bm, width=204, height=1, bg='black').place(x=600, y=355)

label13 = Label(bm, text='Loan Amount Term (In Years)', bg='#00ffff', fg='black', font=('Microsoft YaHei UI Light', 11, 'bold')).place(x=10, y=400)
term = Entry(bm, width=25, fg='black', border=1, bg='white', font=('Microsoft YaHei UI Light', 11))
term.place(x=10, y=430)
Frame(bm, width=204, height=1, bg='black').place(x=10, y=455)

credit_var = IntVar()
label15 = Label(bm, text='Credit History', bg='#00ffff', fg='black',font=('Microsoft YaHei UI Light', 11, 'bold')).place(x=300, y=400)
credit = Radiobutton(bm, text='1', variable=credit_var, value=1, bg='#00ffff', fg='black',activebackground='#00ffff', font=('Microsoft YaHei UI Light', 9, 'bold')).place(x=300, y=430)
credit = Radiobutton(bm, text='0', variable=credit_var, value=2, bg='#00ffff', fg='black', activebackground='#00ffff', font=('Microsoft YaHei UI Light', 9, 'bold')).place(x=350, y=430)

area_var = IntVar()
label16 = Label(bm, text='Property Area', bg='#00ffff', fg='black', font=('Microsoft YaHei UI Light', 11, 'bold')).place(x=600, y=400)
area = Radiobutton(bm, text='Urban', variable=area_var, value=1, bg='#00ffff', fg='black', activebackground='#00ffff', font=('Microsoft YaHei UI Light', 9, 'bold')).place(x=600, y=430)
area = Radiobutton(bm, text='Semiurban', variable=area_var, value=2, bg='#00ffff', fg='black', activebackground='#00ffff', font=('Microsoft YaHei UI Light', 9, 'bold')).place(x=700, y=430)
area = Radiobutton(bm, text='Rural', variable=area_var, value=3, bg='#00ffff', fg='black', activebackground='#00ffff', font=('Microsoft YaHei UI Light', 9, 'bold')).place(x=800, y=430)

# label14 = Label(bm, text='Property Area', bg='#00ffff', fg='black', font=('Microsoft YaHei UI Light', 11, 'bold')).place(x=600, y=400)
# area = Entry(bm, width=25, fg='black', border=1, bg='white', font=('Microsoft YaHei UI Light', 11))
# area.place(x=600, y=430)
# Frame(bm, width=204, height=1, bg='black').place(x=600, y=455)

# Check Button
check = Button(bm, text='Check', width=20, pady=7, bg='#57a1f8', fg='white', activeforeground='white', activebackground='#57a1f8', border=0, cursor='hand2', command=Check).place(x=420, y=450)

bm.mainloop()

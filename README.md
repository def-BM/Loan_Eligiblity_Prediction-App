📌 Loan Eligibility Prediction App

A machine-learning–based desktop application built using Python, Tkinter GUI, and Random Forest Classifier to predict whether a loan applicant is eligible for a loan based on financial and demographic details.

🚀 Features

✔ User authentication system (Sign Up & Sign In) using MySQL
✔ Predicts loan eligibility using a trained ML Model
✔ Clean modern UI designed with Tkinter
✔ Performs automatic data preprocessing, scaling & one-hot encoding
✔ Displays eligibility result with prediction confidence score

🧠 Machine Learning Model

The ML model was trained using the Loan Prediction Dataset (train.csv).

🔍 Steps in Training:
ML Phase	        Details
Pre-processing	    Handling missing values & categorical encoding
Feature Scaling	    StandardScaler
Algorithm	        Random Forest Classifier
Split	            80% Training — 20% Testing
Output	            Saves trained model and scaler using joblib

📂 Model Files Generated
File	                        Purpose
loan_eligibility_model.pkl	    Trained classifier
loan_scaler.pkl	                Scaler used for numerical features
model_features.pkl	            Preserves feature order for correct prediction

📦 Technology Stack
Layer	                    Technologies
Frontend / UI	            Python Tkinter
Backend	                    Python
Machine Learning	        Pandas, NumPy, Scikit-Learn
Authentication Database	    MySQL
Deployment Type	            Desktop App

📁 Folder Structure
Loan Eligibility Prediction App/
│── train.csv
│── loan_eligibility_model.pkl
│── loan_scaler.pkl
│── model_features.pkl
│── sign_up.py
│── sign_in.py
│── main.py
│── README.md
│── /assets  (icons / images for GUI)

🔐 Database Setup (MySQL)

Create database:

CREATE DATABASE py_project;


Create table (this is auto-created inside the app if missing):

CREATE TABLE userdata (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);


🔍 Passwords are stored as plain text only for project demonstration purpose.
In production, hashing (e.g., bcrypt) should be used.

▶ How to Run the Application
1️⃣ Install dependencies
pip install pandas numpy scikit-learn joblib mysql-connector-python

2️⃣ Train Model (only once)

Run your Jupyter Notebook / training script to generate:

loan_eligibility_model.pkl
loan_scaler.pkl
model_features.pkl

3️⃣ Start the application
python sign_in.py

🧪 Sample Test Cases
✔ Eligible Case
Field	            Value
Loan_ID	            LP123456
Gender	            Male
Married	            Yes
Education	        Graduate
Self_Employed	    No
ApplicantIncome	    6500
CoapplicantIncome	2000
LoanAmount	        120
Loan_Amount_Term	30 years
Credit_History	    1
Property_Area	    Urban

❌ Not Eligible Case
Field	            Value
Loan_ID	            LP987654
Gender	            Male
Married	            No
Education	        Not Graduate
Self_Employed	    No
ApplicantIncome	    2000
CoapplicantIncome	0
LoanAmount	        250
Loan_Amount_Term	15 years
Credit_History	    0
Property_Area	    Rural

🎯 Project Outcome

This application demonstrates:

End-to-end ML model training & deployment

GUI integration with ML system

User authentication + prediction system

Industry-style project structure suitable for academic submission

🧑‍💻 Author

Developer: Brijesh Maurya
Role: Final Year IT Engineering Student
Interest Areas: Machine Learning, Data Science, Generative AI
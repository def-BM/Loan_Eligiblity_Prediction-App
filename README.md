# Loan Eligibility Prediction App

Loan Eligibility Prediction App is a machine learning based desktop application built using Python, Tkinter GUI, and Random Forest Classifier to predict whether a loan applicant is eligible for a loan based on financial and demographic information.

---

## Features

- User authentication system (Sign Up and Sign In) using MySQL  
- Predicts loan eligibility using a trained Machine Learning model  
- Modern and clean Tkinter GUI  
- Automatic preprocessing, scaling and one hot encoding  
- Shows eligibility result along with prediction confidence score  

---

## Machine Learning Model

The ML model is trained on the Loan Prediction Dataset (train.csv) and achieved 85 percent accuracy.

### Training Phases
| Phase | Description |
|-------|-------------|
| Pre-processing | Handling missing values and categorical encoding |
| Scaling | StandardScaler |
| Algorithm | Random Forest Classifier |
| Train-Test Split | 80 percent Training / 20 percent Testing |
| Export Model | Model and scaler saved using joblib |

### Output Model Files
| File | Purpose |
|------|---------|
| loan_eligibility_model.pkl | Trained classifier |
| loan_scaler.pkl | Scaler for numerical features |
| model_features.pkl | Saves feature order for correct prediction |

---

## Technology Stack

| Layer | Technologies |
|--------|-------------|
| Frontend / UI | Python Tkinter |
| Backend | Python |
| Machine Learning | Pandas, NumPy, Scikit-Learn |
| Authentication Database | MySQL |
| Deployment Type | Desktop Application |

---

## Folder Structure

```
Loan Eligibility Prediction App/
│ train.csv
│ loan_eligibility_model.pkl
│ loan_scaler.pkl
│ model_features.pkl
│ sign_up.py
│ sign_in.py
│ main.py
│ README.md
└─ assets/    # icons or images for GUI
```

---

## Database Setup (MySQL)

Create database:
```
CREATE DATABASE py_project;
```

Create table (auto-creates in app if missing):
```
CREATE TABLE userdata (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);
```

Note: Passwords are stored as plain text only for demonstration. For production, hashing should be used.

---

## How to Run the Application

1. Install required libraries
```
pip install pandas numpy scikit-learn joblib mysql-connector-python
```

2. Train the model (only once)
Run Jupyter Notebook or training script to generate:
```
loan_eligibility_model.pkl
loan_scaler.pkl
model_features.pkl
```

3. Start the application
```
python sign_in.py
```

---

## Sample Test Cases

### Eligible Example
| Field | Value |
|-------|-------|
| Loan_ID | LP123456 |
| Gender | Male |
| Married | Yes |
| Education | Graduate |
| Self_Employed | No |
| ApplicantIncome | 6500 |
| CoapplicantIncome | 2000 |
| LoanAmount | 120 |
| Loan_Amount_Term | 30 years |
| Credit_History | 1 |
| Property_Area | Urban |

### Not Eligible Example
| Field | Value |
|-------|-------|
| Loan_ID | LP987654 |
| Gender | Male |
| Married | No |
| Education | Not Graduate |
| Self_Employed | No |
| ApplicantIncome | 2000 |
| CoapplicantIncome | 0 |
| LoanAmount | 250 |
| Loan_Amount_Term | 15 years |
| Credit_History | 0 |
| Property_Area | Rural |

---

## Project Outcome

This project demonstrates:
- End to end ML model training and deployment
- Integration of GUI with a machine learning system
- User authentication with prediction system
- Academic final year project level implementation

---

## Author

Developer: Brijesh Maurya  
Final Year IT Engineering Student  
Interest Areas: Machine Learning, Data Science, Generative AI


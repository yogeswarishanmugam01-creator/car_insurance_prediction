# 🚗 Car Insurance Purchase Prediction using Machine Learning

# Problem Statement

Insurance companies need to identify potential customers who are likely to purchase car insurance.
Manually analyzing customer demographics and behavior is time-consuming and inaccurate.

# Objective:

To build a machine learning system that predicts whether a customer will buy car insurance based on features such as age, vehicle age, annual premium, vintage, gender, vehicle damage history, etc.

# Dataset Information

The dataset contains customer demographics and vehicle information.
Common columns include:

Feature	Description

Age	Customer age
Gender	Male/Female
Driving_License	1 = has license, 0 = no license
Vehicle_Age	< 1, 1–2, > 2 years
Vehicle_Damage	Yes/No
Annual_Premium	Insurance premium amount
Vintage	Number of days customer has been associated
Response	Target variable (1 = purchased, 0 = not purchased)

# Machine Learning Model Used

Random Forest Classifier
Why this model?
Performs well on tabular data
Handles both categorical & numerical variables
Robust to noise and overfitting
Provides high accuracy
Works well even with relatively small datasets

# Preprocessing Steps

Label Encoding for categorical columns
Standard Scaling for numerical columns
Train-Test split (80-20 split)
Model saved using Joblib

# Project Structure
car_insurance_prediction/
│── app.py
│── predict.py
│── train_model.py
│── main.py
│── requirements.txt
│── Procfile
│── README.md
│
├── models/
│     ├── insurance_predictor.pkl
│     ├── label_encoders.pkl
│     └── scaler.pkl
│
├── templates/
│     ├── index.html
│     └── result.html
│
├── data/
│     └── insurance_data.csv
│
└── static/    (optional

# Flask Web Application

The app provides a user-friendly UI where users can input:
Age
Gender
Vehicle Age
Vehicle Damage
Annual Premium
Driving License
Vintage
The backend loads the trained model and returns:
Prediction: Will purchase / Will not purchase
Probability: Likelihood score

# How to Run the Project Locally

1. Install Dependencies
Open terminal inside the project folder:
pip install -r requirements.txt

2. Run the Flask Application
python app.py

3. Open Browser
Visit:
http://localhost:5000

4. Fill the form → Submit → View Prediction

# Deployment (Render)

This project can be deployed on Render for real-time use.
Required Deployment Files:
app.py
requirements.txt
Procfile
Procfile content:
web: gunicorn app:app
After deployment, you will receive a permanent URL such as:
https://car-insurance-api.onrender.com

# Model Performance

Accuracy: ~ 80–90%
Precision, Recall, F1-score: Good for both classes
Confusion Matrix: Indicates correct classification for majority cases

# Challenges Faced

Handling categorical encoding
Deployment errors due to dependency mismatches
GitHub push issues with large files
Setting up Render with Procfile and correct requirements

# Conclusion

Successfully built an ML-based prediction system
Provides accurate prediction of car insurance purchase likelihood
Integrated with a web UI using Flask
Hosted online for easy access
Can be extended with dashboards, database storage, and deeper analytics

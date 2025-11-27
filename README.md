Car Insurance Purchase Prediction Using Machine Learning

📝 Project Overview

This project predicts whether a customer will purchase car insurance based on their demographic and vehicle-related details. A machine learning model (Random Forest Classifier) is used to classify customers based on the likelihood of purchase.
A Flask web application is built to allow users to input details and view predictions.
The project can be deployed on Render to access through a permanent online URL.


---

🎯 Problem Statement

Insurance companies want to identify customers who are more likely to purchase vehicle insurance.
Manually analyzing customer information is inefficient and prone to errors.

Objective:

To develop a machine learning-based system that:

Predicts whether a customer will buy car insurance

Helps organizations optimize marketing and customer targeting

Provides real-time predictions through a web interface



---

1.Frontend Tools

HTML5-Form structure	             Standard for web content
CSS3/Bootstrap-Styling               Responsive design, professional UI
JavaScript-Form validation           Client-side input checks
Flask Templates-Dynamic renderin     Python integration, simplicity

2. Backend Tools

Python 3.10-Core programming	Rich ML ecosystem
Flask-Web framework	        Lightweight, Python-native
scikit-learn-Machine learning	Robust classification algorithms
pandas-Data handling	        Efficient data manipulation
joblib-Model persistence	Fast serialization for ML models
ngrok-Public sharing	        Secure tunneling for demos

🧵 Dataset Information

The dataset contains customer demographic and vehicle-related information.

Features:

Feature	Description

Age	Age of the customer
Gender	Male/Female
Driving_License	1 = Has license, 0 = Does not
Vehicle_Age	<1, 1-2, >2 years
Vehicle_Damage	Yes/No
Annual_Premium	Yearly insurance premium
Vintage	Days customer has been associated
Response	Target (1 = Purchased, 0 = Not Purchased)


Dataset size: ~1000+ rows (synthetic or original insurance dataset)


---

🤖 Machine Learning Model

Model Used:

⭐ Random Forest Classifier

Why Random Forest?

Works well with mixed data types

High accuracy and strong generalization

Handles non-linearity

Resistant to overfitting


Preprocessing Steps

Label Encoding of categorical features

Standard Scaler for numerical features

Train-Test split (80–20 split)

Model saved using Joblib (insurance_predictor.pkl)



---

🏗️ Project Structure

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
└── static/    (optional)


---

🌐 Flask Web Application

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



---

💻 How to Run the Project Locally

1️⃣ Install Dependencies

Open terminal inside the project folder:

pip install -r requirements.txt

2️⃣ Run the Flask Application

python app.py

3️⃣ Open Browser

Visit:

http://localhost:5000

4️⃣ Fill the form → Submit → View Prediction


---

☁️ Deployment (Render)

This project can be deployed on Render for real-time use.

Required Deployment Files:

app.py

requirements.txt

Procfile


Procfile content:

web: gunicorn app:app

After deployment, you will receive a permanent URL such as:

https://car-insurance-api.onrender.com


---

📊 Model Performance

Accuracy: ~ 80–90%

Precision, Recall, F1-score: Good for both classes

Confusion Matrix: Indicates correct classification for majority cases



---

🚧 Challenges Faced

Handling categorical encoding

Deployment errors due to dependency mismatches

GitHub push issues with large files

Setting up Render with Procfile and correct requirements



---

📌 Conclusion

Successfully built an ML-based prediction system

Provides accurate prediction of car insurance purchase likelihood

Integrated with a web UI using Flask

Hosted online for easy access

Can be extended with dashboards, database storage, and deeper analytics

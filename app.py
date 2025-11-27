import os
import joblib
import pandas as pd
from flask import Flask, request, render_template
from sklearn.preprocessing import LabelEncoder, StandardScaler

app = Flask(__name__)

# Load model and preprocessing objects
def load_artifacts():
    model_path = os.path.join('models', 'insurance_predictor.pkl')
    label_encoders_path = os.path.join('models', 'label_encoders.pkl')
    scaler_path = os.path.join('models', 'scaler.pkl')
    
    model = joblib.load(model_path)
    label_encoders = joblib.load(label_encoders_path)
    scaler = joblib.load(scaler_path)
    
    return model, label_encoders, scaler

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Load model and preprocessing objects
        model, label_encoders, scaler = load_artifacts()
        
        # Get form data
        data = {
            'Age': int(request.form['Age']),
            'Gender': request.form['Gender'],
            'Driving_License': int(request.form['Driving_License']),
            'Vehicle_Age': request.form['Vehicle_Age'],
            'Vehicle_Damage': request.form['Vehicle_Damage'],
            'Annual_Premium': int(request.form['Annual_Premium']),
            'Vintage': int(request.form['Vintage'])
        }
        
        # Preprocess input data
        input_df = pd.DataFrame([data])
        
        # Label encode categorical features
        categorical_cols = ['Gender', 'Vehicle_Age', 'Vehicle_Damage']
        for col in categorical_cols:
            input_df[col] = label_encoders[col].transform(input_df[col])
        
        # Scale numerical features
        numerical_cols = ['Age', 'Annual_Premium', 'Vintage']
        input_df[numerical_cols] = scaler.transform(input_df[numerical_cols])
        
        # Make prediction
        prediction = model.predict(input_df)[0]
        probability = model.predict_proba(input_df)[0, 1]
        
        # Prepare result
        result = {
            'prediction': 'Will purchase' if prediction == 1 else 'Will not purchase',
            'probability': f"{probability:.2%}"
        }
        
        return render_template('result.html', result=result)
    
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == '__main__':
    # Ensure required directories exist
    os.makedirs('models', exist_ok=True)
    os.makedirs('templates', exist_ok=True)
    
    # Run the app
    app.run(debug=True)
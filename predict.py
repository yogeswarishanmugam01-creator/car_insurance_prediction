import pandas as pd
import joblib

# Load model and preprocessing objects
model = joblib.load('models/insurance_predictor.pkl')
label_encoders = joblib.load('models/label_encoders.pkl')
scaler = joblib.load('models/scaler.pkl')

def predict_insurance(input_data):
    # Convert to DataFrame
    input_df = pd.DataFrame([input_data])
    
    # Preprocess
    for col in label_encoders:
        input_df[col] = label_encoders[col].transform(input_df[col])
    
    numerical_cols = ['Age', 'Annual_Premium', 'Vintage']
    input_df[numerical_cols] = scaler.transform(input_df[numerical_cols])
    
    # Predict
    prediction = model.predict(input_df)
    probability = model.predict_proba(input_df)[:, 1]
    
    return prediction[0], probability[0]

# Example usage
if __name__ == "__main__":
    example_data = {
        'Age': 45,
        'Gender': 'Male',
        'Driving_License': 1,
        'Vehicle_Age': '1-2',
        'Vehicle_Damage': 'Yes',
        'Annual_Premium': 60000,
        'Vintage': 150
    }
    
    pred, prob = predict_insurance(example_data)
    print(f"Prediction: {'Will purchase' if pred == 1 else 'Will not purchase'}")
    print(f"Probability: {prob:.2f}")
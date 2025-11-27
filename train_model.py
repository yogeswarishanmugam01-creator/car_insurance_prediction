import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib

# Load data
df = pd.read_csv('data/insurance_data.csv')

# Preprocessing
# Handle categorical data
categorical_cols = ['Gender', 'Vehicle_Age', 'Vehicle_Damage']
label_encoders = {}

for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# Save label encoders
joblib.dump(label_encoders, 'models/label_encoders.pkl')

# Normalize numerical features
numerical_cols = ['Age', 'Annual_Premium', 'Vintage']
scaler = StandardScaler()
df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

# Save scaler
joblib.dump(scaler, 'models/scaler.pkl')

# Split data
X = df.drop('Response', axis=1)
y = df['Response']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("Model Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Save model
joblib.dump(model, 'models/insurance_predictor.pkl')
print("\nModel saved to models/insurance_predictor.pkl")
import pandas as pd
import numpy as np

# Create synthetic data
np.random.seed(42)
n_samples = 1000

data = {
    'Age': np.random.randint(18, 70, n_samples),
    'Gender': np.random.choice(['Male', 'Female'], n_samples),
    'Driving_License': np.random.choice([0, 1], n_samples, p=[0.1, 0.9]),
    'Vehicle_Age': np.random.choice(['<1', '1-2', '>2'], n_samples),
    'Vehicle_Damage': np.random.choice(['Yes', 'No'], n_samples),
    'Annual_Premium': np.random.normal(50000, 15000, n_samples).astype(int),
    'Vintage': np.random.randint(10, 300, n_samples),
    'Response': np.random.choice([0, 1], n_samples, p=[0.7, 0.3])  # Target
}

df = pd.DataFrame(data)
df.to_csv('data/insurance_data.csv', index=False)
print("Synthetic dataset created!")
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('data/insurance_data.csv')

# Basic info
print("=== Dataset Info ===")
print(df.info())

print("\n=== Missing Values ===")
print(df.isnull().sum())

print("\n=== Descriptive Statistics ===")
print(df.describe())

# Visualizations
plt.figure(figsize=(10, 6))
sns.countplot(x='Response', data=df)
plt.title('Distribution of Insurance Purchases')
plt.savefig('notebooks/purchase_distribution.png')
plt.close()

# Correlation matrix (for numerical features)
numerical_df = df.select_dtypes(include=['int64', 'float64'])
plt.figure(figsize=(10, 8))
sns.heatmap(numerical_df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.savefig('notebooks/correlation_matrix.png')
plt.close()

print("\nExploratory analysis complete. Check the notebooks folder for visualizations.")
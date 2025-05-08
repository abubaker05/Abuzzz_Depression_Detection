import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load dataset
df = pd.read_csv('depression_data.csv')

# Features and target
X = df.drop('depression', axis=1)
y = df['depression']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("✅ Model trained and saved as model.pkl")

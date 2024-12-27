from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Assuming `data` is already loaded and preprocessed as shown before

# Define features and target
X = data.drop(columns=['Risk_Level'])  # Exclude the 'Risk_Level' column from features
y = data['Risk_Level']  # Target: Risk levels (High, Medium, Low)

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalize the features
X_train = scaler.fit_transform(X_train)  # Use previously trained scaler
X_test = scaler.transform(X_test)

# Train a Random Forest model to predict risk levels
risk_model = RandomForestClassifier(n_estimators=100, random_state=42)
risk_model.fit(X_train, y_train)

# Predict risk levels
y_pred_risk = risk_model.predict(X_test)

# Evaluate model performance
print(classification_report(y_test, y_pred_risk))

# Save the trained risk model
joblib.dump(risk_model, 'risk_model.pkl')

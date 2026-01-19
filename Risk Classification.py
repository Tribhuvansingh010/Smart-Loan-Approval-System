from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

X = data.drop(columns=['Risk_Level']) 
y = data['Risk_Level']  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train = scaler.fit_transform(X_train)  
X_test = scaler.transform(X_test)
risk_model = RandomForestClassifier(n_estimators=100, random_state=42)
risk_model.fit(X_train, y_train)
y_pred_risk = risk_model.predict(X_test)


print(classification_report(y_test, y_pred_risk))

joblib.dump(risk_model, 'risk_model.pkl')


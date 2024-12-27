from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained models
model = joblib.load('loan_approval_model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/apply', methods=['POST'])
def apply():
    # Get the data from the form submission (JSON format expected)
    data = request.json
    
    # Prepare the data for prediction
    input_data = pd.DataFrame([data])
    input_data_scaled = scaler.transform(input_data)

    # Predict loan approval
    loan_approval = model.predict(input_data_scaled)

    if loan_approval == 1:
        return jsonify({'status': 'Approved'}), 200
    else:
        return jsonify({'status': 'Rejected'}), 400

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load('loan_approval_model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/apply', methods=['POST'])
def apply():
 
    data = request.json
    
    input_data = pd.DataFrame([data])
    input_data_scaled = scaler.transform(input_data)

    loan_approval = model.predict(input_data_scaled)

    if loan_approval == 1:
        return jsonify({'status': 'Approved'}), 200
    else:
        return jsonify({'status': 'Rejected'}), 400

if __name__ == '__main__':
    app.run(debug=True)


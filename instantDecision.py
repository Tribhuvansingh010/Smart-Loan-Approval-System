# Import necessary libraries
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Render a simple HTML form
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Instant Loan Decision</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 0; padding: 20px; }
            .container { max-width: 500px; margin: 0 auto; }
            .form-group { margin-bottom: 15px; }
            label { display: block; margin-bottom: 5px; }
            input { width: 100%; padding: 8px; }
            button { padding: 10px 15px; background-color: #007BFF; color: white; border: none; cursor: pointer; }
            button:hover { background-color: #0056b3; }
            .decision { margin-top: 20px; font-weight: bold; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Instant Loan Decision</h1>
            <form id="loanForm">
                <div class="form-group">
                    <label for="name">Name:</label>
                    <input type="text" id="name" name="name" required>
                </div>
                <div class="form-group">
                    <label for="amount">Loan Amount:</label>
                    <input type="number" id="amount" name="amount" required>
                </div>
                <div class="form-group">
                    <label for="income">Monthly Income:</label>
                    <input type="number" id="income" name="income" required>
                </div>
                <button type="button" onclick="getDecision()">Get Decision</button>
            </form>
            <div id="decision" class="decision"></div>
        </div>

        <script>
            async function getDecision() {
                const name = document.getElementById('name').value;
                const amount = document.getElementById('amount').value;
                const income = document.getElementById('income').value;

                const response = await fetch('/decision', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ name, amount, income })
                });

                const result = await response.json();
                document.getElementById('decision').textContent = `Decision: ${result.decision}`;
            }
        </script>
    </body>
    </html>
    '''

@app.route('/decision', methods=['POST'])
def decision():
    data = request.get_json()
    name = data.get('name')
    amount = float(data.get('amount', 0))
    income = float(data.get('income', 0))

    # Simple logic to determine loan approval
    if income >= amount * 2:
        return jsonify({ 'decision': 'Approved' })
    else:
        return jsonify({ 'decision': 'Rejected' })

if __name__ == '__main__':
    app.run(debug=True)

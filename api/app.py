from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/add/<int:num1>/<int:num2>', methods=['GET'])
def add(num1, num2):
    result = num1 + num2
    return jsonify({'status': 200, 'result': result})

@app.route('/api/subtract/<int:num1>/<int:num2>', methods=['GET'])
def subtract(num1, num2):
    result = num1 - num2
    return jsonify({'status': 200, 'result': result})

@app.route('/api/multiply/<int:num1>/<int:num2>', methods=['GET'])
def multiply(num1, num2):
    result = num1 * num2
    return jsonify({'status': 200, 'result': result})

@app.route('/api/divide/<int:num1>/<int:num2>', methods=['GET'])
def divide(num1, num2):
    if num2 == 0:
        return jsonify({'status': 400, 'error': 'Division by zero is not allowed'})
    result = num1 / num2
    return jsonify({'status': 200, 'result': result})

# Ensure the app runs properly on Vercel
if __name__ == '__main__':
    app.run()




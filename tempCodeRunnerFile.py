# app.py
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace with the actual E-Courts API endpoint
E_COURTS_API_URL = 'https://apis.akshit.me/eciapi/16'

@app.route('/get_court_data', methods=['GET'])
def get_court_data():
    # Extract parameters from the request
    case_number = request.args.get('case_number')
    
    if not case_number:
        return jsonify({'error': 'Case number is required'}), 400
    
    try:
        # Make a request to the E-Courts API
        response = requests.get(f'{E_COURTS_API_URL}?case_number={case_number}')
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Assuming the API returns JSON data
        data = response.json()
        return jsonify(data)
    
    except requests.RequestException as e:
        return jsonify({'error': 'Error fetching court data: ' + str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
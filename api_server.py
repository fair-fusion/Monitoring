# Script code for a Python server that exposes an API endpoint to fetch the temperature data from the sensor 
# reader script. The data is constantly written to a csv file called data.csv. 
# This server will handle incoming requests from the React app and return the temperature data.
import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

def load_data():
    """
    Loads the temperature data from the csv file.
    Returns:
        data (pandas.DataFrame): The temperature data.    
    """
    # Read the csv file into a pandas dataframe and return it. 
    try:
        data = pd.read_csv('data.csv')
        return data
    except FileNotFoundError:
        return None

# API endpoint to fetch temperature data
@app.route('/temperature', methods=['GET'])
def get_temperature():
    """
    Load temperature and get the latest reading. The reading is returned as a dictionary.  
    """
    data = load_data()
    if data is not None:
        # Get the latest temperature reading
        latest_reading = data.tail(1)
        temperature = latest_reading['temperature'].values[0]
        return jsonify({'temperature': temperature})
    else:
        return jsonify({'error': 'No data available'}), 404

# API endpoint to fetch historical temperature data
@app.route('/temperature/history', methods=['GET'])
def get_temperature_history():
    """
    This endpoint returns the historical temperature readings. The readings are returned as a list of dictionaries. 
    Each dictionary contains the timestamp and the temperature reading. The readings are sorted in descending order. 
    """
    data = load_data()
    if data is not None:
        # Get the historical temperature readings
        temperature_history = data.to_dict(orient='records')
        return jsonify(temperature_history)
    else:
        return jsonify({'error': 'No data available'}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
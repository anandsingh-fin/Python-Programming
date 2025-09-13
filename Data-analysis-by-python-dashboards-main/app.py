from flask import Flask, render_template, jsonify
import pandas as pd
import os # Import the os module

# --- Setup Paths ---
# Get the absolute path of the directory where this script is located
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
# Define the path to the static folder and the CSV file
STATIC_DIR = os.path.join(BASE_DIR, 'static')
CSV_PATH = os.path.join(STATIC_DIR, 'swiggy.csv')

# Initialize the Flask application
app = Flask(__name__)

# Define the main route to serve the dashboard's HTML page
@app.route('/')
def index():
    """Renders the main dashboard page."""
    return render_template('index.html')

# Define an API endpoint to serve the restaurant data as JSON
@app.route('/data')
def get_data():
    """Reads the CSV file using an absolute path and returns its content as JSON."""
    try:
        
        df = pd.read_csv(CSV_PATH)
        
        df = df.fillna('')
        
        data = df.to_dict(orient='records')
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": f"Data file not found at {CSV_PATH}"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd

app = Flask(__name__)

# Load the saved model
model = joblib.load('crime_xgb_model.pkl')

# Define label mapping
label_mapping = {
    0: "BATTERY - SIMPLE ASSAULT",
    1: "BURGLARY",
    2: "SHOPLIFTING - PETTY THEFT ($950 & UNDER)",
    3: "THEFT OF IDENTITY",
    4: "VEHICLE - STOLEN"
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """
    Predict crime type based on input data.
    """
    try:
        # Get form data
        data = request.form.to_dict(flat=True)

        # Expected fields and their types
        expected_fields = {
            'Lat': float,
            'Lon': float,
            'Hour': int,
            'Minute': int,
            'Day': int,
            'Month': int,
            'Area Name': int,
            'Premis Desc': int,
            'Time Period': int,
            'Day of Week': int
        }

        # Validate and convert input data
        converted_data = {}
        for field, dtype in expected_fields.items():
            if field not in data or data[field] == '':
                return jsonify({"error": f"Missing or empty input for {field}"}), 400
            try:
                converted_data[field] = dtype(data[field])
            except ValueError:
                return jsonify({"error": f"Invalid format for {field}. Expected {dtype.__name__}."}), 400

        # Convert to DataFrame
        df = pd.DataFrame([converted_data])

        # Make prediction
        prediction = model.predict(df)[0]

        # Map prediction to crime description
        predicted_crime = label_mapping.get(int(prediction), "Unknown Crime")

        return jsonify({"prediction": predicted_crime})

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)

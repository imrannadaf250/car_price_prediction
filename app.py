from flask import Flask, request, render_template_string
import pickle
import pandas as pd
import os

app = Flask(__name__)

# Load the trained pipeline
MODEL_FILE = "LinearRegressionModel.pkl"
DATA_FILE = "Cleaned_Car_data.csv"

with open(MODEL_FILE, "rb") as file:
    model = pickle.load(file)

# Load cleaned data only to create dropdown values
car_data = pd.read_csv(DATA_FILE)

# The notebook trained the model with these columns:
# name, company, year, kms_driven, fuel_type
car_names = sorted(car_data["name"].dropna().astype(str).unique().tolist())
companies = sorted(car_data["company"].dropna().astype(str).unique().tolist())
fuel_types = sorted(car_data["fuel_type"].dropna().astype(str).unique().tolist())

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Car Price Prediction</title>
    <style>
        * { box-sizing: border-box; }
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #111827, #1f2937);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 25px;
        }
        .card {
            width: 100%;
            max-width: 560px;
            background: white;
            border-radius: 18px;
            padding: 30px;
            box-shadow: 0 15px 40px rgba(0,0,0,.30);
        }
        h1 {
            text-align: center;
            margin: 0 0 8px;
            color: #111827;
        }
        .subtitle {
            text-align: center;
            color: #6b7280;
            margin-bottom: 25px;
        }
        label {
            display: block;
            font-weight: 600;
            margin: 14px 0 7px;
            color: #374151;
        }
        input, select {
            width: 100%;
            padding: 12px 13px;
            border: 1px solid #d1d5db;
            border-radius: 9px;
            font-size: 15px;
            outline: none;
        }
        input:focus, select:focus {
            border-color: #2563eb;
        }
        button {
            width: 100%;
            margin-top: 22px;
            padding: 13px;
            border: 0;
            border-radius: 9px;
            background: #2563eb;
            color: white;
            font-size: 16px;
            font-weight: 700;
            cursor: pointer;
        }
        button:hover { background: #1d4ed8; }
        .result {
            margin-top: 22px;
            padding: 16px;
            border-radius: 10px;
            background: #ecfdf5;
            color: #065f46;
            text-align: center;
            font-size: 21px;
            font-weight: 700;
        }
        .error {
            margin-top: 18px;
            padding: 13px;
            border-radius: 10px;
            background: #fef2f2;
            color: #991b1b;
        }
        .note {
            margin-top: 18px;
            font-size: 12px;
            color: #6b7280;
            text-align: center;
        }
    </style>
</head>
<body>
<div class="card">
    <h1>🚗 Car Price Prediction</h1>
    <div class="subtitle">Enter car details to estimate the used-car price</div>

    <form method="POST">
        <label>Car Name</label>
        <select name="name" required>
            <option value="">Select car</option>
            {% for item in car_names %}
                <option value="{{ item }}" {% if form.get('name') == item %}selected{% endif %}>{{ item }}</option>
            {% endfor %}
        </select>

        <label>Company</label>
        <select name="company" required>
            <option value="">Select company</option>
            {% for item in companies %}
                <option value="{{ item }}" {% if form.get('company') == item %}selected{% endif %}>{{ item }}</option>
            {% endfor %}
        </select>

        <label>Year</label>
        <input type="number" name="year" min="1995" max="2025"
               value="{{ form.get('year', '') }}" required>

        <label>Kilometers Driven</label>
        <input type="number" name="kms_driven" min="0"
               value="{{ form.get('kms_driven', '') }}" required>

        <label>Fuel Type</label>
        <select name="fuel_type" required>
            <option value="">Select fuel type</option>
            {% for item in fuel_types %}
                <option value="{{ item }}" {% if form.get('fuel_type') == item %}selected{% endif %}>{{ item }}</option>
            {% endfor %}
        </select>

        <button type="submit">Predict Price</button>
    </form>

    {% if prediction is not none %}
        <div class="result">
            Estimated Price: ₹{{ "{:,.0f}".format(prediction) }}
        </div>
    {% endif %}

    {% if error %}
        <div class="error">{{ error }}</div>
    {% endif %}

    <div class="note">
        Prediction is based on the trained Linear Regression pipeline.
    </div>
</div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    error = None
    form = request.form

    if request.method == "POST":
        try:
            name = request.form["name"]
            company = request.form["company"]
            year = int(request.form["year"])
            kms_driven = int(request.form["kms_driven"])
            fuel_type = request.form["fuel_type"]

            # Keep exactly the same column order used in the notebook.
            input_data = pd.DataFrame(
                [[name, company, year, kms_driven, fuel_type]],
                columns=["name", "company", "year", "kms_driven", "fuel_type"]
            )

            prediction = float(model.predict(input_data)[0])

            # Avoid displaying a negative price if an unusual input is entered.
            prediction = max(0, prediction)

        except Exception as e:
            error = f"Could not make prediction: {str(e)}"

    return render_template_string(
        HTML,
        car_names=car_names,
        companies=companies,
        fuel_types=fuel_types,
        prediction=prediction,
        error=error,
        form=form
    )


if __name__ == "__main__":
    app.run(debug=True)

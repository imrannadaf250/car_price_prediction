# 🚗 Car Price Prediction Web Application

A machine learning web application that predicts the estimated price of a used car from basic car details.

## 📌 Project Overview

This project uses a trained **Linear Regression pipeline** and a Flask web application to provide car price predictions through a simple web interface.

The model takes these inputs:

- Car name
- Company
- Manufacturing year
- Kilometers driven
- Fuel type

The trained model is stored in `LinearRegressionModel.pkl` and loaded by the Flask application.

## 🛠️ Technologies Used

- Python
- Flask
- Pandas
- Scikit-learn
- HTML
- CSS
- Pickle
- Linear Regression

## 📂 Project Structure

```text
car_price/
│
├── app.py
├── LinearRegressionModel.pkl
├── Cleaned_Car_data.csv
├── requirements.txt
├── README.md
└── venv/
```

> `venv/` is a local virtual environment and should normally not be uploaded to GitHub.

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd car_price
```

### 2. Create a virtual environment

```powershell
python -m venv venv
```

### 3. Install dependencies

```powershell
venv\Scripts\python.exe -m pip install -r requirements.txt
```

If you want to activate the environment and PowerShell allows it:

```powershell
venv\Scripts\activate
```

Then:

```powershell
pip install -r requirements.txt
```

## ▶️ Run the Application

```powershell
venv\Scripts\python.exe app.py
```

After Flask starts, open:

```text
http://127.0.0.1:5000
```

## 🔮 How It Works

1. The user enters or selects car details.
2. Flask receives the form data.
3. The data is converted into a Pandas DataFrame.
4. The trained machine learning pipeline processes the input.
5. The model predicts the estimated car price.
6. The prediction is displayed on the webpage.

## 📊 Model Input

The application sends these columns to the trained model:

```text
name
company
year
kms_driven
fuel_type
```

## 💻 Example

```text
Car Name: Maruti Suzuki Swift
Company: Maruti
Year: 2019
Kilometers Driven: 100
Fuel Type: Petrol
```

The model then returns an estimated car price.

## ⚠️ Model Compatibility

The trained `LinearRegressionModel.pkl` was created with **scikit-learn 1.6.1**.

The project therefore uses:

```text
scikit-learn==1.6.1
```

Using the same version helps avoid model-loading compatibility problems.

## 🚀 Future Improvements

- Compare multiple machine learning models.
- Improve the user interface.
- Add prediction history.
- Add price-analysis charts.
- Deploy the application online.
- Add more car features to improve predictions.

## 👨‍💻 Author

**Imran Nadaf**

Python | Data Science | Machine Learning

---

⭐ If you find this project useful, consider giving the repository a star.

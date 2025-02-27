# Lapd-Crime-Prediction-Project
This project predicts criminal activities in Los Angeles using machine learning and LAPD crime datasets. It includes data preprocessing, exploratory data analysis (EDA), predictive modeling (XGBoost, Random Forest), and a Flask-based web application for real-time crime prediction based on geographic and temporal factors.

# 🔍 LAPD Crime Prediction Using Machine Learning  

## 📌 Project Overview  
This project aims to analyze and predict **criminal activities in Los Angeles** using machine learning techniques. It utilizes the **LAPD Crime Data (2020-2024)** to uncover crime trends, predict crime types, and deploy an interactive **Flask-based web application** for real-time crime prediction.  

✅ **Data Cleaning & Preprocessing** (handling missing values, feature engineering)  
✅ **Exploratory Data Analysis (EDA)** (crime trends, high-risk areas, time-based crime patterns)  
✅ **Machine Learning Classification** (XGBoost, Random Forest, Decision Tree, Naive Bayes)  
✅ **Time-Series Forecasting** (to predict future crime trends)  
✅ **Deployment of a Flask Web App** for real-time crime prediction  

---

## 🚀 Technologies Used  
- **Python (Pandas, NumPy, Matplotlib, Seaborn, Scikit-Learn, XGBoost)**  
- **Jupyter Notebook** for data exploration and model training  
- **Flask** for deploying the crime prediction model  
- **Machine Learning Models:**  
  - XGBoost (Best-performing model)  
  - Random Forest  
  - Decision Tree  
  - Naive Bayes  
- **Frontend (HTML + Flask):** Interactive web interface for users  

---
## 📊 Exploratory Data Analysis (EDA)  
Before building models, **EDA** was performed to analyze crime trends over time and across different neighborhoods.  

📌 **Key Insights from EDA:**  
- **Vehicle theft is the most frequent crime** in Los Angeles.  
- **Crime rates are highest in the Central and 77th Street areas.**  
- **Peak crime hours occur between 3 PM – 9 PM, with Friday & Saturday being the most crime-prone days.**  
- **Street locations account for most reported crimes.**  

---

## 🤖 Machine Learning Models  
The project implemented **classification models** to predict crime categories based on location and time.  

📌 **Model Performance:**  
| Model | Accuracy (%) | Best Use Case |  
|------------|--------------|----------------|  
| **XGBoost** | 74.19% | Best overall crime prediction model |  
| **Random Forest** | 72.05% | Robust and interpretable model |  
| **Decision Tree** | 68.14% | Simple and effective for explainability |  
| **Naive Bayes** | 37.17% | Performed poorly on imbalanced data |  

📌 **Time-Series Forecasting:**  
The **Holt-Winters method** was used to forecast crime trends, showing a **steady increase in crimes over time.**  

---

## 🚀 Deployment of the Crime Prediction Model  
A **Flask web application** was developed to predict crime types based on user-provided location and time inputs.  

📌 **How It Works:**  
1️⃣ User enters details like **latitude, longitude, time, and area.**  
2️⃣ Model predicts the **most likely type of crime** at that location.  
3️⃣ The prediction is displayed on the **Flask web interface.**  

📌 **Local Deployment:**  
To run the Flask app locally:  
```bash
python app.py
```

---
📌 Key Learning Outcomes
✅ Crime Data Analysis & Feature Engineering
✅ Predictive Modeling for Crime Type Classification
✅ Time-Series Forecasting for Crime Trends
✅ Building & Deploying a Flask-Based Prediction Model

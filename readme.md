# 🚚 ShipmentSure - AI-Powered Shipment Delay Prediction

## 📌 Overview

ShipmentSure is a Machine Learning-powered web application that predicts whether a shipment will be delivered on time or delayed based on logistics and customer-related factors.

The project was developed as part of the **Infosys Springboard Internship 6.0** and demonstrates the complete Machine Learning lifecycle from data preprocessing to cloud deployment.

## 🎯 Problem Statement

Delayed shipments can lead to:

* Customer dissatisfaction
* Increased operational costs
* Supply chain disruptions
* Reduced business trust

ShipmentSure helps organizations predict shipment delays in advance, enabling proactive decision-making and improved logistics planning.

---

## 🌐 Live Demo

🔗 https://shipmentsure-project.streamlit.app/

---

## 📊 Dataset

**Source:** Supply Chain Logistics Dataset (Kaggle)

**Records:** 10,999

**Target Variable:**

* 0 → On-Time Delivery
* 1 → Delayed Delivery

---

## 🛠 Features Used

### Categorical Features

* Warehouse Block
* Mode of Shipment
* Product Importance
* Gender

### Numerical Features

* Customer Care Calls
* Customer Rating
* Cost of Product
* Prior Purchases
* Discount Offered
* Weight in Grams

---

## ⚙️ Data Preprocessing

* Missing value handling
* One-Hot Encoding
* Feature Scaling using StandardScaler
* Feature Engineering

### Engineered Features

* Cost Weight Ratio
* Discount Cost Ratio
* Calls Per Purchase

---

## 🤖 Machine Learning Models

The following models were trained and evaluated:

| Model               | Accuracy |
| ------------------- | -------- |
| Logistic Regression | 65%      |
| Random Forest       | 66%      |
| XGBoost             | 68%      |

🏆 **Best Model: XGBoost**

---

## 📈 Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix

---

## 🖥 Application Features

✅ User-Friendly Interface

✅ Real-Time Predictions

✅ Probability Score Display

✅ Risk Level Indicator

✅ Confidence Percentage

✅ Responsive Streamlit Dashboard

---

## 🚀 Tech Stack

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Scikit-Learn
* XGBoost
* Matplotlib
* Seaborn

### Deployment

* Streamlit

### Version Control

* GitHub

## 📂 Project Structure

```text
ShipmentSure/
│
├── backend/
│   ├── preprocess.py
│   └── predictor.py
│
├── frontend/
│   └── ui_components.py
│
├── models/
│   ├── ShipmentSure_Model.pkl
│   └── Scaler.pkl
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```


## 🔍 How It Works

1. User enters shipment details.
2. Features are preprocessed.
3. Engineered features are generated.
4. Data is scaled using StandardScaler.
5. XGBoost model predicts shipment status.
6. Prediction results and probabilities are displayed.

---

## 🎓 Internship Information

Developed during:

**Infosys Springboard Internship 6.0**

Project Title:

**ShipmentSure: AI-Enabled On-Time Delivery Predictor**

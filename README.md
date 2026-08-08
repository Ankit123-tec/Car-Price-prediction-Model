# 🚗 Car Price Prediction App

An end-to-end Machine Learning web application that predicts the estimated resale value of used cars based on market features. Built with a **FastAPI** backend to serve the model and a modern **Streamlit** frontend user interface.

---

## 📌 Features

* **Interactive Frontend:** Built with Streamlit, providing an intuitive, multi-column dashboard for inputting vehicle details.
* **REST API Backend:** Built with FastAPI to handle predictions via HTTP JSON requests.
* **Smart Valuation Engine:** Machine Learning regression model processing key vehicle parameters (age, mileage, present price, fuel type, transmission, owner history).
* **Environment Switcher:** Built-in UI toggle to switch seamlessly between local execution (`localhost:8000`) and cloud deployment endpoints.

---

## 🛠️ Tech Stack

* **Frontend:** Streamlit, Requests
* **Backend:** FastAPI, Uvicorn
* **Machine Learning:** Python, Pandas, NumPy, Scikit-Learn
* **Deployment:** Render

---

## 😍 How It look And how it works : 
<img width="1451" height="774" alt="image" src="https://github.com/user-attachments/assets/1c6ce084-34d1-4083-b2e0-da7444a7940f" />

---
## 📁 Repository Structure

```text
├── main.py              # FastAPI backend API
├── app.py               # Streamlit frontend application
├── model.pkl            # Trained Machine Learning model
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation

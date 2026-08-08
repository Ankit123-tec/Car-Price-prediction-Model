import streamlit as st
import requests

# Page Config
st.set_page_config(
    page_title="Car Price Predictor",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        background-color: #FF4B4B;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.6rem 1rem;
    }
    .stButton>button:hover {
        background-color: #FF2B2B;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# API Configuration
DEFAULT_RENDER_URL = "https://car-prediction-lpfl.onrender.com/predict"
DEFAULT_LOCAL_URL = "http://127.0.0.1:8000/predict"

# Sidebar - Settings & Backend Config
with st.sidebar:
    st.header("⚙️ Configuration")
    use_local = st.toggle("Use Local API Endpoint", value=False)
    API_URL = DEFAULT_LOCAL_URL if use_local else DEFAULT_RENDER_URL
    st.caption(f"Active Endpoint:\n`{API_URL}`")
    
    st.divider()
    st.markdown("### ℹ️ About")
    st.info(
        "This tool uses Machine Learning to estimate the resale value "
        "of a vehicle based on market variables."
    )

# Header Section
st.title("🚗 Used Car Price Predictor")
st.markdown("Provide the vehicle details below to estimate its current market value.")
st.divider()

# Input Form in Two Columns
col1, col2 = st.columns(2, gap="large")

with col1:
    st.subheader("📋 Basic Details")
    car_name = st.text_input("Car Model / Name", value="swift", placeholder="e.g. swift, ritz, sx4")
    year = st.number_input("Model Year", min_value=1990, max_value=2026, value=2014, step=1)
    present_price = st.number_input("Original Showroom Price (₹ Lakhs)", min_value=0.0, value=5.59, step=0.10, format="%.2f")
    kms_driven = st.number_input("Kilometers Driven", min_value=0, value=40000, step=1000)

with col2:
    st.subheader("⚙️ Specifications")
    fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])
    seller_type = st.selectbox("Seller Type", ["Dealer", "Individual"])
    transmission = st.selectbox("Transmission Type", ["Manual", "Automatic"])
    
    owner_label = st.selectbox(
        "Previous Owners", 
        ["0 (First Owner)", "1 (Second Owner)", "3 (Third Owner)"]
    )
    owner = int(owner_label.split()[0])

# Construct Payload
payload = {
    "Car_Name": str(car_name),
    "Year": int(year),
    "Present_Price": float(present_price),
    "Kms_Driven": int(kms_driven),
    "Fuel_Type": str(fuel_type),
    "Seller_Type": str(seller_type),
    "Transmission": str(transmission),
    "Owner": int(owner),
}

st.divider()

# Prediction & Results Section
res_col1, res_col2 = st.columns([1, 2], gap="large")

with res_col1:
    predict_btn = st.button("Calculate Valuation 💰", use_container_width=True)

with res_col2:
    if predict_btn:
        with st.spinner("Connecting to model backend..."):
            try:
                res = requests.post(API_URL, json=payload, timeout=25)
                if res.status_code == 200:
                    data = res.json()
                    # 'prediction_price' key ko check list mein add kar diya hai
                    pred = data.get("prediction_price", data.get("prediction", data.get("predicted_price", None)))

                    if pred is not None:
                        # Display estimated price inside a metric callout
                        st.metric(
                            label="Estimated Resale Value", 
                            value=f"₹ {pred:.2f} Lakhs"
                        )
                        st.success("Valuation generated successfully!")
                    else:
                        st.warning("API connected, but return key 'prediction' was not found.")
                        st.json(data)
                else:
                    st.error(f"API Error {res.status_code}")
                    st.code(res.text)
            except requests.exceptions.RequestException as e:
                st.error("Could not reach the prediction service.")
                st.caption("Verify that your server is running or active on Render.")

# Developer Payload Inspector
with st.expander("🔍 View Request Payload Details"):
    st.json(payload)
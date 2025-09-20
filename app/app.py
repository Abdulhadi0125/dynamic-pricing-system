# app.py
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px

# Page config
st.set_page_config(
    page_title="🚖 Dynamic Pricing Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load trained Random Forest pipeline
pipeline = joblib.load("model/best_dynamic_pricing_model.pkl")

# Function to suggest optimal price
def suggest_optimal_price(pipeline, features, price_range=(5, 100), step=1):
    prices = []
    revenues = []
    for p in range(price_range[0], price_range[1] + 1, step):
        feat = features.copy()
        feat["price"] = p
        demand_pred = pipeline.predict(pd.DataFrame([feat]))[0]
        revenue = p * demand_pred
        prices.append(p)
        revenues.append(revenue)
    best_idx = np.argmax(revenues)
    return prices[best_idx], revenues[best_idx], prices, revenues

# Sidebar Inputs
st.sidebar.header("Trip Details")
cab_type = st.sidebar.selectbox("Cab Type", ["Uber", "Lyft"])
name = st.sidebar.selectbox(
    "Cab Name",
    ["Shared","Black","Black SUV","Lux","Lux Black","Lux Black XL",
     "Lyft","Lyft XL","UberX","UberPool","Uber XL","WAV","Taxi"]
)
hour = st.sidebar.slider("Hour of Day", 0, 23, 12, 1)
is_weekend = st.sidebar.selectbox("Weekend?", [0, 1])
surge_multiplier = st.sidebar.selectbox(
    "Surge Multiplier", [1.0, 1.25, 1.5, 1.75, 2.0, 2.5, 3.0]
)

# Prepare input features
features = {
    "cab_type": cab_type,
    "name": name,
    "hour": hour,
    "is_weekend": is_weekend,
    "surge_multiplier": surge_multiplier,
    "price": 10  # placeholder
}

# Compute optimal price and revenue
best_price, best_revenue, prices, revenues = suggest_optimal_price(
    pipeline, features, price_range=(5, 100), step=1
)

# Main layout with columns
st.title("🚖 Uber/Lyft Dynamic Pricing Dashboard")

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Optimal Price & Revenue")
    st.metric("💡 Suggested Optimal Price", f"₹{best_price}")
    st.metric("📈 Expected Revenue", f"₹{best_revenue:.2f}")

with col2:
    st.subheader("Price vs Predicted Revenue")
    fig = px.line(
        x=prices, y=revenues, markers=True,
        labels={'x':'Price (₹)', 'y':'Expected Revenue (₹)'},
        title="Price vs Revenue"
    )
    st.plotly_chart(fig, use_container_width=True)

# Optional: show inputs summary
with st.expander("Trip Input Summary"):
    st.json(features)

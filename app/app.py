# app.py
import os
import streamlit as st
import plotly.express as px
import requests

def main():
    # Page config
    st.set_page_config(
        page_title="🚖 Dynamic Pricing Dashboard",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # API URL (FastAPI backend) via environment variable
    API_HOST = os.getenv("API_HOST", "127.0.0.1")  # default internal host
    API_PORT = os.getenv("API_PORT", "8000")       # default FastAPI port
    API_URL = f"http://{API_HOST}:{API_PORT}/predict"

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

    # Placeholder for results
    best_price = None
    best_revenue = None
    features = {}
    prices = []
    revenues = []

    # Button to trigger prediction
    if st.sidebar.button("Predict"):
        payload = {
            "cab_type": cab_type,
            "name": name,
            "hour": hour,
            "is_weekend": is_weekend,
            "surge_multiplier": surge_multiplier
        }

        # Call API
        try:
            response = requests.post(API_URL, json=payload)
            response.raise_for_status()
            result = response.json()
            best_price = result["suggested_optimal_price"]
            best_revenue = result["expected_revenue"]
            features = result["inputs"]
            prices = result.get("prices", [])
            revenues = result.get("revenues", [])
        except Exception as e:
            st.error(f"Error calling API: {e}")

    # Main layout
    st.title("🚖 Uber/Lyft Dynamic Pricing Dashboard")

    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader("Optimal Price & Revenue")
        if best_price is not None:
            st.metric("💡 Suggested Optimal Price", f"${best_price}")
            st.metric("📈 Expected Revenue", f"${best_revenue:.2f}")
        else:
            st.info("Click 'Predict' to calculate optimal price and revenue.")

    with col2:
        st.subheader("Price vs Predicted Revenue")
        if prices and revenues:
            fig = px.line(
                x=prices, y=revenues, markers=True,
                labels={'x':'Price ($)', 'y':'Expected Revenue ($)'},
                title="Price vs Revenue"
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Price vs Revenue chart will appear here after clicking 'Predict'.")

    with st.expander("Trip Input Summary"):
        if features:
            st.json(features)
        else:
            st.write("No inputs yet. Click 'Predict' to see trip details.")

if __name__ == "__main__":
    main()

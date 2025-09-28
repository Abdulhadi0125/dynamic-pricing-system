# app/api.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import numpy as np

# Load trained Random Forest pipeline
pipeline = joblib.load("model/best_dynamic_pricing_model.pkl")

app = FastAPI(title="🚖 Dynamic Pricing API")

# Request schema (only the 5 parameters)
class TripRequest(BaseModel):
    cab_type: str
    name: str
    hour: int
    is_weekend: int
    surge_multiplier: float

# Helper: suggest optimal price
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

@app.get("/")
def home():
    return {"message": "Dynamic Pricing API is running"}

@app.post("/predict")
def predict_trip(req: TripRequest):
    # Convert request to features dict
    features = {
        "cab_type": req.cab_type,
        "name": req.name,
        "hour": req.hour,
        "is_weekend": req.is_weekend,
        "surge_multiplier": req.surge_multiplier,
        "price": 10  # placeholder
    }

    best_price, best_revenue, prices, revenues = suggest_optimal_price(pipeline, features)

    # Logging for backend
    print("Received request:", req.dict())
    print("Sending response:", {
        "suggested_optimal_price": best_price,
        "expected_revenue": round(best_revenue, 2),
        "inputs": features
    })

    return {
        "suggested_optimal_price": best_price,
        "expected_revenue": round(best_revenue, 2),
        "inputs": features,
        "prices": prices,
        "revenues": [round(r, 2) for r in revenues]
    }

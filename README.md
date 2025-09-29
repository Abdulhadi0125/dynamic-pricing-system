🚖 Dynamic Pricing System for Uber/Lyft

📌 Overview

Ride-hailing companies like Uber and Lyft use dynamic pricing (also called surge pricing) to balance supply and demand. The goal is to:

Suggest the optimal fare for a trip.

Maximize driver revenue while keeping the ride attractive for customers.

This project implements a machine learning-powered pricing system that predicts demand and suggests the optimal ride price in real-time.

Model download: [best_dynamic_pricing_model.pkl (58 MB)](https://drive.google.com/file/d/1Q0D5bjbtM5rW7OU6ZrFNymNR0urBSONU/view?usp=drive_link)

Dataset (optional, 350 MB): [Uber & Lyft Dataset - Boston, MA](https://www.kaggle.com/datasets/brllrb/uber-and-lyft-dataset-boston-ma?resource=download)

Live demo: https://dynamic-pricing-system-fajq.onrender.com/

🛠️ Tech Stack

Frontend → Streamlit
 (interactive dashboard).

Backend API → FastAPI : Python, scikit-learn, joblib
 (model inference).

Libraries: pandas, numpy, matplotlib, plotly, joblib, lightgbm

Model → Trained Random Forest Regressor for demand prediction.

Deployment → Docker + Render
.

⚙️ Architecture
flowchart TD
    A[User: Enters trip details] --> B[Streamlit Frontend]
    B -->|API Request JSON| C[FastAPI Backend]
    C -->|Runs ML Model| D[Dynamic Pricing Model]
    D -->|Optimal Price + Revenue| C
    C -->|Response JSON| B
    B --> E[Interactive Dashboard]

🚀 Features

Enter trip details (cab type, name, time, surge multiplier, weekend).

Predicts optimal fare and expected revenue.

Interactive Price vs Revenue chart.

Deployed online with public demo link.

📊 Dataset

Source: Uber & Lyft rides dataset

Features used:

cab_type

name (cab category)

hour

is_weekend

surge_multiplier

price (target for optimization).

📊 Model

Type: Random Forest Regressor

Training dataset: Uber ride dataset

Evaluation Metrics:

RMSE: 8.82

MAE: 4.40

R²: 0.984

The model predicts demand at different price points, and the app calculates the price that maximizes revenue.


🖥️ Screenshots

<img width="1919" height="849" alt="image" src="https://github.com/user-attachments/assets/9671d7f4-14f8-46d1-aff5-907d1c09c940" />

Trip Inputs	Prediction & Chart

	
🏗️ Run Locally
1️⃣ Clone the repo
git clone https://github.com/<your-username>/dynamic-pricing-system.git
cd dynamic-pricing-system

2️⃣ Install dependencies
pip install -r app/requirements.txt

3️⃣ Run FastAPI backend
uvicorn app.api:app --host 0.0.0.0 --port 8000

4️⃣ Run Streamlit frontend
streamlit run app/app.py --server.port 8501


Then visit → http://localhost:8501

🌍 Deployment (Render)

Containerized with Docker.

Supervisor runs both FastAPI (port 8000) and Streamlit (port 8501).

Hosted on Render:
👉 Live App- https://dynamic-pricing-system-fajq.onrender.com/

📌 Future Improvements

Add weather and traffic data as features.

Store predictions in a database for analytics.

User authentication (driver vs admin dashboards).

Docker Compose for better service management.

👤 Author

Abdul Hadi S

🎓 Final Year ECE Student | Aspiring Data Analyst & ML Engineer

🌐 LinkedIn
 | GitHub

⚡ If you found this project interesting, don’t forget to ⭐ star the repo!

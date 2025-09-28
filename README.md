🚖 DYNAMIC PRICING SYSTEM – UBER/LYFT

A Dynamic Pricing Dashboard that predicts optimal ride prices in real-time to maximize revenue using a Random Forest ML model. Built with Python, scikit-learn, and Streamlit for a fully interactive user experience.

📌 Project Overview

Dynamic pricing is a strategy where prices are adjusted in real-time based on demand, supply, and external factors.
This project simulates a real-world use case for ride-hailing services like Uber and Lyft, predicting the optimal price to maximize revenue for each trip.

Model download: [best_dynamic_pricing_model.pkl (58 MB)](https://drive.google.com/file/d/1Q0D5bjbtM5rW7OU6ZrFNymNR0urBSONU/view?usp=drive_link)

Dataset (optional, 350 MB): [Uber & Lyft Dataset - Boston, MA](https://www.kaggle.com/datasets/brllrb/uber-and-lyft-dataset-boston-ma?resource=download)

🛠️ Features & Functionality

Inputs:

Cab type (Uber / Lyft)

Cab name (e.g., Black SUV, Lux Black XL, etc.)

Hour of the day (0–23)

Weekend flag (0/1)

Surge multiplier (1.0–3.0)

Outputs:

Suggested optimal price

Expected revenue

Interactive Price vs Revenue chart

Summary of input trip features

Bonus Features:

Transparent, modern dashboard design

Interactive Plotly chart for better visualization

📊 Model

Type: Random Forest Regressor

Training dataset: Uber ride dataset

Evaluation Metrics:

RMSE: 8.82

MAE: 4.40

R²: 0.984

The model predicts demand at different price points, and the app calculates the price that maximizes revenue.

🛠️ Tech Stack

Backend & ML: Python, scikit-learn, joblib

Frontend: Streamlit, Plotly

Libraries: pandas, numpy, matplotlib, plotly, joblib, lightgbm

🚀 How to Run Locally

Clone the repository

git clone https://github.com/Abdulhadi0125/dynamic-pricing-system.git
cd dynamic-pricing-system


Create and activate a virtual environment (recommended: Anaconda)

conda create -n dynamic_pricing python=3.12
conda activate dynamic_pricing


Install dependencies

pip install -r app/requirements.txt


Run the Streamlit app

streamlit run app/app.py


Open the URL in your browser (usually http://localhost:8501
).

Optional: You can also run the app using Docker:

docker build -t dynamic-pricing .
docker run -p 8000:8000 -p 8501:8501 dynamic-pricing

🖼️ Screenshots

<img width="1919" height="849" alt="image" src="https://github.com/user-attachments/assets/9671d7f4-14f8-46d1-aff5-907d1c09c940" />


Sidebar inputs for trip features

Suggested optimal price & expected revenue

Interactive Plotly chart for price vs revenue

🔮 Future Improvements

Add weather and traffic features to improve demand prediction

Implement Reinforcement Learning (RL) for advanced dynamic pricing

Add competitor price scraping for real-time e-commerce pricing

Deploy on AWS / GCP / Render for public access

📂 Repository Structure
dynamic-pricing-project/
│
├── app/
│   ├── api.py          # FastAPI backend
│   ├── app.py          # Streamlit frontend
│   └── requirements.txt
│
├── model/
│   └── best_dynamic_pricing_model.pkl
│
├── Dockerfile          # For containerization
├── supervisord.conf    # For running API + Streamlit in one container
├── README.md
└── Rideshare dataset description.docx

✨ Author

Abdul Hadi S.
LinkedIn: linkedin.com/in/abdulhadi2004

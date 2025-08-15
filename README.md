#SolGuard – Energy AI Dashboard

#Rayfield Systems Intern Project

"""Overview"""

SolGuard is an AI-powered solar energy monitoring and analytics dashboard that helps operators:

Predict AC power output using an ensemble of regression models.

Detect anomalies in energy data with an adjustable sensitivity slider.

Generate GPT-powered insights for actionable recommendations.

Visualize energy performance through interactive charts.

Share live dashboards securely using Ngrok.

This system is designed to reduce downtime, improve maintenance planning, and optimize energy yield by automating detection and reporting.

Why This is Needed

Solar energy operators face several challenges:

Energy loss: Equipment faults or inefficiencies can cause 5–20% yearly production losses.

High maintenance costs: Delays in detection can cost $1,000–$5,000 per incident in large-scale systems.

Data overload: Thousands of readings per day make manual analysis impractical.

Forecasting gaps: Inaccurate predictions disrupt grid planning and sales.

SolGuard addresses these with:

Automated ML-based forecasting.

Anomaly detection with Isolation Forest.

AI-driven summaries and recommendations.

A user-friendly Streamlit interface for live monitoring.

Features
1. AC Power Prediction

Uses an ensemble model combining:

Linear Regression (baseline relationships)

Random Forest (non-linear patterns)

Gradient Boosting (error-focused improvement)

AdaBoost (weighted learning for hard cases)

VotingRegressor combines model outputs weighted by past performance.

2. Anomaly Detection

Isolation Forest algorithm.

Adjustable sensitivity (contamination parameter: 0.01 – 0.2).

Highlights unusual spikes/drops in AC power.

3. GPT-Powered Analysis

Summarizes weekly performance.

Explains anomalies.

Suggests maintenance actions.

Recommends optimization strategies.

4. Interactive Dashboard

CSV file upload with required columns:

date, hour, dc_power, daily_yield, total_yield, ac_power


Line charts showing actual vs. predicted AC power.

Red markers for anomalies.

Downloadable CSV of detected anomalies.

5. Live Sharing via Ngrok

Generates secure, temporary HTTPS link for remote viewing.

Optional password protection.

Auto-closes when the server stops.

Data Requirements
Column	Description
date	Date of reading (YYYY-MM-DD)
hour	Hour of the day (0–23)
dc_power	Direct current power reading
daily_yield	Cumulative daily production
total_yield	Lifetime energy production
ac_power	Alternating current power output
Installation
1. Clone the Repository
git clone https://github.com/<your-username>/solguard.git
cd solguard

2. Install Dependencies
pip install streamlit pyngrok scikit-learn matplotlib pandas joblib openai

3. Set Ngrok Auth Token

Replace with your token from Ngrok Dashboard:

ngrok authtoken <YOUR_NGROK_TOKEN>

4. Configure OpenAI API Key

Replace OPENAI_API_KEY in app.py with your actual key:

OPENAI_API_KEY = "sk-xxxxxxxxxxxxxxxx"

Running the App
streamlit run app.py


If Ngrok is set up, you’ll see a public HTTPS URL in the terminal.

Usage

Upload CSV – The app validates required columns.

Adjust Sensitivity – Use the slider to detect more/less anomalies.

View Predictions – Chart compares actual vs. predicted AC power.

Check Alerts – Anomaly list with timestamps and values.

Get AI Summary – GPT explains findings and recommends actions.

Download Reports – Export anomalies as CSV.

Share Live Dashboard – Send Ngrok link to stakeholders.

Failsafes & Reliability

CSV format validation with clear errors.

Graceful handling of missing/invalid data.

Auto-retraining if the model file is missing.

Backup visualizations if chart rendering fails.

Ngrok tunnel auto-closes to maintain security.

Future Improvements

From the Rayfield Systems Demo Day slides:

Cloud-hosted models for scalability.

Advanced GPT summaries with multi-step reasoning.

Enhanced UI (hover, zoom interactions).

Multi-file upload and workflow automation.

Example Workflow

Operator uploads a week’s solar data CSV.

App trains or loads ensemble model.

Predictions generated for AC power.

Isolation Forest flags e.g., 3 anomalies for the week.

GPT summarizes:
"3 anomalies detected on high-temperature afternoons; possible inverter overheating. Recommend fan inspection and panel cleaning."

Operator downloads anomaly report and schedules maintenance.

References

Rayfield System Demo Day Slides, 2025
.

Scikit-learn documentation: https://scikit-learn.org

OpenAI API documentation: https://platform.openai.com/docs

Ngrok: https://ngrok.com

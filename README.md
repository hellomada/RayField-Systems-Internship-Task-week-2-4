# ⚡ **SolGuard – Energy AI Dashboard**  
**_Rayfield Systems Intern Project_**

---

## 📌 **Overview**
**SolGuard** is an **AI-powered solar energy monitoring and analytics dashboard** that helps operators:

- **Predict AC power output** using an ensemble of regression models.  
- **Detect anomalies** in energy data with an adjustable sensitivity slider.  
- **Generate GPT-powered insights** for actionable recommendations.  
- **Visualize energy performance** through interactive charts.  
- **Share live dashboards securely** using Ngrok.  

This system is designed to **reduce downtime**, **improve maintenance planning**, and **optimize energy yield** by automating detection and reporting.  

---

## ❓ **Why This is Needed**
Solar energy operators face several challenges:

- **<ins>Energy loss</ins>** – Equipment faults or inefficiencies can cause **5–20% yearly production losses**.  
- **<ins>High maintenance costs</ins>** – Delays in detection can cost **$1,000–$5,000** per incident in large-scale systems.  
- **<ins>Data overload</ins>** – Thousands of readings per day make manual analysis impractical.  
- **<ins>Forecasting gaps</ins>** – Inaccurate predictions disrupt grid planning and sales.  

**SolGuard** addresses these by combining **automated ML-based forecasting**, **anomaly detection**, and **AI-driven summaries** in a **user-friendly Streamlit interface**.

---

## 🚀 **Features**
### **1. AC Power Prediction**
- Uses an **ensemble model** combining:
  - **Linear Regression** – Baseline relationships.
  - **Random Forest** – Handles non-linear patterns.
  - **Gradient Boosting** – Improves predictions by focusing on errors.
  - **AdaBoost** – Adapts to difficult-to-predict cases.
- **VotingRegressor** combines outputs, weighted by performance.

### **2. Anomaly Detection**
- **Isolation Forest** algorithm.  
- Adjustable **contamination parameter**: `0.01 – 0.2`.  
- Highlights **unusual spikes/drops** in AC power.

### **3. GPT-Powered Analysis**
- Summarizes **weekly performance**.
- Explains **anomalies**.
- Suggests **maintenance actions**.
- Provides **optimization strategies**.

### **4. Interactive Dashboard**
- CSV file upload with **required columns**:

date, hour, dc_power, daily_yield, total_yield, ac_power


- **Charts**: Actual vs. Predicted AC power.
- **Red markers**: Anomalies.
- **Downloadable CSV**: Anomaly list.

### **5. Live Sharing via Ngrok**
- Secure, **temporary HTTPS link**.
- Optional **password protection**.
- Auto-closes when the server stops.

---

## 📊 **Data Requirements**
| Column        | Description                               |
|---------------|-------------------------------------------|
| `date`        | Date of reading (YYYY-MM-DD)              |
| `hour`        | Hour of the day (0–23)                    |
| `dc_power`    | Direct current power reading              |
| `daily_yield` | Cumulative daily production               |
| `total_yield` | Lifetime energy production                |
| `ac_power`    | Alternating current power output          |

---

## ⚙️ **Installation**
### **1. Clone the Repository**
```bash
git clone https://github.com/<your-username>/solguard.git
cd solguard


2. Install Dependencies
pip install streamlit pyngrok scikit-learn matplotlib pandas joblib openai

3. Set Ngrok Auth Token

Replace with your token from Ngrok Dashboard:

ngrok authtoken <YOUR_NGROK_TOKEN>

4. Configure OpenAI API Key

Edit in app.py:

OPENAI_API_KEY = "sk-xxxxxxxxxxxxxxxx"

▶️ Running the App
streamlit run app.py


If Ngrok is set up, you’ll see a public HTTPS URL in the terminal.

🖥️ Usage

Upload CSV – The app validates required columns.

Adjust Sensitivity – Detect more/less anomalies.

View Predictions – Compare actual vs. predicted AC power.

Check Alerts – See anomalies with timestamps and values.

Get AI Summary – GPT explains and recommends actions.

Download Reports – Export anomalies as CSV.

Share Dashboard – Send Ngrok link to stakeholders.

🛡 Failsafes & Reliability

CSV format validation with clear error messages.

Graceful handling of missing/invalid data.

Auto-retraining if the model file is missing.

Backup visualizations if charts fail.

Ngrok tunnel auto-closes to maintain security.

📈 Future Improvements

Cloud-hosted models for scalability.

Advanced GPT summaries with deeper reasoning.

Enhanced UI with hover & zoom.

Multi-file uploads & workflow automation.

🔄 Example Workflow

Operator uploads a week’s solar data.

Model trains/loads.

Predictions generated for AC power.

Example: 3 anomalies detected for the week.

GPT explains:

"3 anomalies detected on high-temperature afternoons; possible inverter overheating. Recommend fan inspection and panel cleaning."

Operator downloads anomaly report and schedules maintenance.

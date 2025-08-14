# -*- coding: utf-8 -*-
"""Final App For Rayfield Systems (Failsafe Version with GPT Actionable Summary)"""

# Install dependencies
!pip install streamlit pyngrok scikit-learn matplotlib pandas joblib openai

# Set ngrok auth token (replace with yours)
!ngrok authtoken 2qFGMWOMeEuHTiLPxw8jEmXaNpb_6eCNm53johjExqNGmDuo4

# Write the Streamlit app code
app_code = """
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest, VotingRegressor, RandomForestRegressor, GradientBoostingRegressor, AdaBoostRegressor
from sklearn.linear_model import LinearRegression
import joblib, io, os
from openai import OpenAI

# ====== Config ======
MODEL_FILENAME = "ensemble_model.joblib"
OPENAI_API_KEY = "add APi key HERE"

# Initialize OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

# ====== Functions ======
def feature_engineering(df):
    try:
        return df[['hour', 'dc_power', 'daily_yield', 'total_yield']]
    except KeyError as e:
        st.error(f"Missing required feature columns: {e}")
        return None

def train_models(x_train, y_train):
    try:
        lr = LinearRegression().fit(x_train, y_train)
        rf = RandomForestRegressor(n_estimators=100, random_state=42).fit(x_train, y_train)
        gbr = GradientBoostingRegressor(n_estimators=100, random_state=42).fit(x_train, y_train)
        adr = AdaBoostRegressor(n_estimators=100, random_state=42).fit(x_train, y_train)
        lr2 = LinearRegression().fit(x_train, y_train)

        ensemble = VotingRegressor([
            ("GBR", gbr),
            ("RFR", rf),
            ("ADR", adr),
            ("LR", lr2)
        ])
        ensemble.fit(x_train, y_train)
        return ensemble
    except Exception as e:
        st.error(f"Model training failed: {e}")
        return None

def gpt_summary(text):
    try:
        # New API syntax
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role":"user","content":text}],
            max_tokens=250
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"GPT summary failed: {e}"

# ====== Main App ======
def main():
    st.set_page_config(page_title="Energy AI Dashboard", layout="wide")
    st.title("⚡ Energy AI Dashboard with GPT Actionable Summary")

    uploaded_file = st.file_uploader(
        "Upload energy CSV with columns ['date','hour','dc_power','daily_yield','total_yield','ac_power']",
        type=["csv"]
    )

    if uploaded_file:
        try:
            df = pd.read_csv(uploaded_file)
        except Exception as e:
            st.error(f"Error reading CSV: {e}")
            return

        required_cols = ['date','hour','dc_power','daily_yield','total_yield','ac_power']
        if not all(col in df.columns for col in required_cols):
            st.error(f"CSV must have columns: {required_cols}")
            return

        try:
            df['date'] = pd.to_datetime(df['date'])
        except Exception as e:
            st.error(f"Date parsing failed: {e}")
            return

        X = feature_engineering(df)
        if X is None:
            return
        y = df['ac_power']

        # ===== Model Training / Loading =====
        try:
            if os.path.exists(MODEL_FILENAME):
                model = joblib.load(MODEL_FILENAME)
                st.info("Loaded pre-trained ensemble model.")
            else:
                with st.spinner("Training model..."):
                    model = train_models(X, y)
                    if model is None:
                        return
                    joblib.dump(model, MODEL_FILENAME)
                    st.success("Model trained and saved.")
        except Exception as e:
            st.error(f"Model loading/training failed: {e}")
            return

        # ===== Predictions =====
        try:
            df['predicted_ac_power'] = model.predict(X)
        except Exception as e:
            st.error(f"Prediction failed: {e}")
            return

        # ===== Anomaly Detection =====
        try:
            iso = IsolationForest(contamination=0.05, random_state=42)
            df['anomaly'] = iso.fit_predict(df[['predicted_ac_power']]) == -1
        except Exception as e:
            st.error(f"Anomaly detection failed: {e}")
            return

        anomaly_count = df['anomaly'].sum()
        summary_text = f"This week, {anomaly_count} anomalies detected in predicted AC power."

        # ===== Layout =====
        col1, col2 = st.columns([3,2])

        with col1:
            st.subheader("Energy Output Chart")
            try:
                fig, ax = plt.subplots(figsize=(10,5))
                ax.plot(df['date'], df['ac_power'], label="Actual AC Power", color='blue')
                ax.plot(df['date'], df['predicted_ac_power'], label="Predicted AC Power", color='green', linestyle='--')
                anomalies = df[df['anomaly']]
                ax.scatter(anomalies['date'], anomalies['predicted_ac_power'], color='red', label='Anomalies', zorder=5)
                ax.set_xlabel("Date")
                ax.set_ylabel("AC Power")
                ax.legend()
                ax.set_title("Actual vs Predicted AC Power with Anomalies")
                st.pyplot(fig)
            except Exception as e:
                st.error(f"Chart rendering failed: {e}")

        with col2:
            st.subheader("Weekly Summary")
            st.markdown(f"**{summary_text}**")

            st.subheader("Anomaly Alerts")
            try:
                if anomaly_count == 0:
                    st.write("No anomalies detected.")
                else:
                    for _, row in anomalies.iterrows():
                        st.write(f"⚠️ Anomaly on {row['date'].date()}: Predicted AC Power = {row['predicted_ac_power']:.2f}")
                    csv_buffer = io.StringIO()
                    anomalies[['date','predicted_ac_power']].to_csv(csv_buffer, index=False)
                    st.download_button(
                        label="Download Anomalies CSV for Zapier",
                        data=csv_buffer.getvalue(),
                        file_name="anomalies_today.csv",
                        mime="text/csv"
                    )

            except Exception as e:
                st.error(f"Anomaly reporting failed: {e}")

            # ===== GPT Summary with Actionable Insights =====
            try:
                st.subheader("AI Analysis Summary")
                rows_text = ""
                for i, row in df.head().iterrows():
                    rows_text += " | ".join(str(v) for v in row.values) + "\\n"

                gpt_input = (
                    f"Analyze the following energy dataset and provide actionable insights.\\n"
                    f"Total anomalies detected: {anomaly_count}\\n"
                    f"First 5 rows of data:\\n{rows_text}\\n"
                    f"Highlight unusual patterns, possible causes, and recommended actions."
                )
                summary_gpt = gpt_summary(gpt_input)
                st.info(summary_gpt)
            except Exception as e:
                st.error(f"GPT summary generation failed: {e}")

if __name__ == "__main__":
    main()
"""

with open("app.py", "w") as f:
    f.write(app_code)

from pyngrok import ngrok
import threading, time

try:
    ngrok.kill()
    public_url = ngrok.connect(8501)
    print(f"Streamlit app URL: {public_url}")
except Exception as e:
    print(f"Ngrok setup failed: {e}")
    public_url = None

def run_streamlit():
    try:
        !streamlit run app.py
    except Exception as e:
        print(f"Streamlit failed to start: {e}")

threading.Thread(target=run_streamlit, daemon=True).start()
time.sleep(5)

try:
    !streamlit run app.py
except Exception as e:
    print(f"Streamlit direct run failed: {e}")

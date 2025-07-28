Dataset Context
The dataset contains solar plant generation data recorded at intervals with key power outputs (DC and AC), daily yield, and cumulative total yield.

Key Metrics / Features for AI/ML
Feature Name	Description	Use Case / Benefits
Rolling 7-day Average DAILY_YIELD	Average daily energy yield over the previous 7 days per plant.	Smooths short-term fluctuations; improves daily output forecasting accuracy.
Hourly % Change in AC_POWER	Percent change of AC power output compared to the previous hour or time interval.	Detects rapid drops/spikes indicating faults or shading events; useful for anomaly detection.
Time Since Last Peak AC_POWER	Time elapsed since the last recorded peak AC power output for each plant.	Helps identify patterns in peak production and predict performance cycles.
DC to AC Power Ratio (Efficiency)	Ratio of AC_POWER to DC_POWER, measuring inverter efficiency per time point.	Monitors inverter health; decreases can flag inefficiencies or failures.
Daily Total Yield Difference	Difference in DAILY_YIELD compared to the previous day per plant.	Detects sudden changes in daily output, useful for automated alerts on underperformance.
Cumulative Yield Growth Rate	Daily percentage increase in TOTAL_YIELD per plant.	Tracks long-term performance trends and degradation over time.
Time-based Features (Hour, Day of Week)	Extracted from DATE_TIME to capture cyclical production patterns linked to sunlight and weather.	Enhances forecasting by incorporating time-dependent variability in production.

How These Features Help Automate Workflows
Forecasting: Rolling averages and time-based features allow regression and time series models to predict plant output more accurately.

Anomaly Detection: Sudden percentage changes in AC power and shifts in efficiency ratios trigger alerts for maintenance teams to inspect possible issues.

Performance Monitoring: Tracking efficiency ratios and cumulative yield growth aids asset managers in identifying when equipment degrades or needs service.

Reporting: Daily yield differences and peak timing help create automated performance summaries and operational reports.

Next Steps
Implement calculations of these features in your data cleaning and preprocessing notebooks.

Visualize these features to validate their behavior and impact.

Use these engineered features as inputs in the AI/ML models planned for Weeks 3–5.


Key Metrics / Features
Rolling 7-day Average DAILY_YIELD

Calculates the average daily energy yield over the past 7 days for each plant.

Helps smooth short-term fluctuations and improves accuracy in forecasting daily output.

Hourly Percentage Change in AC_POWER

Measures the percent change in AC power output compared to the previous hour (or closest time interval).

Useful for detecting sudden drops or spikes that may indicate faults, shading, or other anomalies.

Time Since Last Peak AC_POWER

Tracks the elapsed time since the last recorded peak AC power output for each plant.

Assists in identifying production cycles and predicting upcoming peaks or performance drops.

DC to AC Power Ratio (Efficiency)

The ratio of AC_POWER to DC_POWER at each time point, representing inverter efficiency.

Declines in this ratio can signal inverter malfunctions or efficiency losses needing maintenance.

Daily Total Yield Difference

The difference in DAILY_YIELD compared to the previous day for each plant.

Helps automatically flag unexpected performance changes or potential issues.

Cumulative Yield Growth Rate

The daily percentage increase in TOTAL_YIELD per plant.

Useful for monitoring long-term performance trends and degradation over time.

Time-based Features (Hour of Day, Day of Week)

Extracted from the DATE_TIME column to capture daily and weekly production patterns.

Supports models in accounting for cyclic variations caused by sunlight, weather, and operational schedules.

How These Features Support Automation
Improve forecasting models by incorporating smoothed averages and time cycles.

Enable anomaly detection by identifying sudden output changes and efficiency drops.

Aid performance monitoring for proactive maintenance scheduling.

Facilitate automated reporting through metrics highlighting operational status and trends.

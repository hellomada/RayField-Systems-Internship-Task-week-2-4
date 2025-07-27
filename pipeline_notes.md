# Data Pipeline Components and Notes

| Step               | Tool/Method           | Trigger        | Input                | Output                      |
|--------------------|----------------------|----------------|----------------------|-----------------------------|
| Data Input         | CSV upload            | Manual/Daily   | raw_data.csv         | Raw dataset loaded          |
| Data Cleaning      | pandas (Python)       | Same as input  | raw_data.csv         | cleaned_data.csv            |
| Feature Generation | pandas rolling/groupby| After cleaning | cleaned_data.csv     | features.csv or in-memory   |
| Forecasting Model  | scikit-learn Linear Regression | Post-features | feature set          | forecasted_output.csv       |
| Summary Generation | GPT (OpenAI API)      | Post-forecast  | daily stats          | text_summary.txt or dashboard|
| Output Delivery    | Email / Dashboard     | After all steps| summary, forecasts   | Email reports, dashboard view|

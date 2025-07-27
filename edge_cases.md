# Pipeline Edge Case Handling

1. **New Columns in Input Data**  
   - Automatically ignore unknown columns or log warnings for review.  
   - Use flexible column selection based on expected names.

2. **Missing Data on Holidays or Outages**  
   - Use forward-fill or interpolation to fill gaps.  
   - Flag days with excessive missing data for manual review.

3. **Scaling to Multiple Sites or Turbines**  
   - Design pipeline as modular functions processing one dataset at a time.  
   - Use loops or parallel processing for batch runs over multiple data files.

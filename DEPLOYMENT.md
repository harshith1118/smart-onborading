# Streamlit App Setup Instructions

This file contains instructions and configurations to prevent the Streamlit app from going to sleep.

## Deployment Tips to Prevent Sleep

1. **Use Streamlit Community Cloud Settings:**
   - In your Streamlit Community Cloud app settings, ensure the app is set to "Always rerun" 
   - This can be found in the app settings on Streamlit Community Cloud

2. **Add this to your GitHub README.md:**
   ```
   # Onboarding Training Compliance Tracker
   
   [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](YOUR_APP_URL_HERE)
   
   ## Preventing Sleep Issues
   This app implements several strategies to prevent sleeping:
   - Auto-refresh indicator
   - Optimized configuration settings
   - Efficient data handling
   ```

3. **Configuration Files:**
   - config.toml contains server optimization settings
   - requirements.txt has updated versions for compatibility

4. **Code-level Solutions Implemented:**
   - Visual refresh indicator that updates with current time
   - Hidden elements that change with each page load
   - Efficient data processing to reduce load times

5. **Keep-Alive Script:**
   - A `keep_alive.py` script is included that can be run separately to periodically ping your app
   - Usage: `python keep_alive.py YOUR_APP_URL`
   - The script now also starts the Streamlit app automatically
"""
Keep Alive Script for Streamlit App
This script periodically sends requests to the Streamlit app to prevent it from sleeping.
"""

import requests
import time
import sys
import os
import subprocess
import threading

def start_streamlit_app():
    """Start the Streamlit app in a separate thread"""
    try:
        # Set environment variable to disable telemetry
        env = os.environ.copy()
        env["STREAMLIT_DISABLE_TELEMETRY"] = "true"
        
        # Start Streamlit app
        process = subprocess.Popen([
            sys.executable, "-m", "streamlit", "run", "onboarding_dashboard.py"
        ], env=env)
        
        print("Streamlit app started successfully")
        return process
    except Exception as e:
        print(f"Error starting Streamlit app: {str(e)}")
        return None

def keep_alive(url, interval=300):  # 5 minutes default
    """
    Periodically send requests to keep the Streamlit app alive
    
    Args:
        url (str): The URL of the Streamlit app
        interval (int): Interval in seconds between requests (default: 300 seconds/5 minutes)
    """
    print(f"Starting keep-alive service for {url}")
    print(f"Sending request every {interval} seconds...")
    print("Press Ctrl+C to stop")
    
    try:
        while True:
            try:
                response = requests.get(url, timeout=10)
                if response.status_code == 200:
                    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] App is alive (Status: {response.status_code})")
                else:
                    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Unexpected response (Status: {response.status_code})")
            except requests.exceptions.RequestException as e:
                print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Error: {str(e)}")
            
            time.sleep(interval)
            
    except KeyboardInterrupt:
        print("\nKeep-alive service stopped.")
        sys.exit(0)

if __name__ == "__main__":
    # Default URL - change this to your actual Streamlit app URL
    APP_URL = "http://localhost:8501"  # Change this to your deployed URL
    
    # Check if URL is provided as command line argument
    if len(sys.argv) > 1:
        APP_URL = sys.argv[1]
    
    # Start Streamlit app in background
    print("Starting Streamlit app...")
    app_process = start_streamlit_app()
    
    # Start keep-alive service
    if app_process:
        keep_alive(APP_URL)
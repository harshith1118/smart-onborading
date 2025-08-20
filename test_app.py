"""
Test script to verify the Streamlit app works correctly
"""

import subprocess
import sys
import time
import requests

def test_app():
    """Test if the Streamlit app starts and responds correctly"""
    try:
        # Set environment variable to disable telemetry
        env = {}
        env.update(sys.environ)
        env["STREAMLIT_DISABLE_TELEMETRY"] = "true"
        
        # Start Streamlit app
        print("Starting Streamlit app...")
        process = subprocess.Popen([
            sys.executable, "-m", "streamlit", "run", "onboarding_dashboard.py", "--server.headless=true"
        ], env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Wait a bit for the app to start
        time.sleep(10)
        
        # Check if the app is running
        try:
            response = requests.get("http://localhost:8501", timeout=5)
            if response.status_code == 200:
                print("SUCCESS: Streamlit app is running correctly")
                return True
            else:
                print(f"ERROR: Unexpected status code {response.status_code}")
                return False
        except requests.exceptions.RequestException as e:
            print(f"ERROR: Could not connect to the app: {str(e)}")
            return False
            
    except Exception as e:
        print(f"ERROR: Failed to start the app: {str(e)}")
        return False
    finally:
        # Terminate the process if it's still running
        try:
            if 'process' in locals():
                process.terminate()
                process.wait(timeout=5)
        except:
            pass

if __name__ == "__main__":
    test_app()
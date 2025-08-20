"""
Dependency check script to verify all required packages are installed
"""

import sys

def check_dependencies():
    """Check if all required dependencies are installed"""
    required_packages = [
        'streamlit',
        'pandas',
        'numpy',
        'plotly'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"OK {package} is installed")
        except ImportError:
            print(f"ERROR {package} is missing")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\nMissing packages: {', '.join(missing_packages)}")
        print("Please install them using: pip install -r requirements.txt")
        return False
    else:
        print("\nAll dependencies are installed correctly!")
        return True

if __name__ == "__main__":
    check_dependencies()
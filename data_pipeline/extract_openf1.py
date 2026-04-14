import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("OPENF1_BASE_URL", "https://api.openf1.org/v1")

def get_sessions():
    response = requests.get(f"{BASE_URL}/sessions", timeout=30)
    response.raise_for_status()
    return response.json()

def get_drivers():
    response = requests.get(f"{BASE_URL}/drivers", timeout=30)
    response.raise_for_status()
    return response.json()

def get_laps():
    response = requests.get(f"{BASE_URL}/laps", timeout=30)
    response.raise_for_status()
    return response.json()
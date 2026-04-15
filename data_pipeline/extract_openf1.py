import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("OPENF1_BASE_URL", "https://api.openf1.org/v1")

def get_sessions():
    response = requests.get(f"{BASE_URL}/sessions", timeout=30)
    response.raise_for_status()
    return response.json()

def get_drivers(session_key: int):
    response = requests.get(f"{BASE_URL}/drivers", params={"session_key": session_key}, timeout=30)
    response.raise_for_status()
    return response.json()

def get_laps(session_key: int):
    response = requests.get(f"{BASE_URL}/laps", params={"session_key": session_key}, timeout=30)
    response.raise_for_status()
    return response.json()
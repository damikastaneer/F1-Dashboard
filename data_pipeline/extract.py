import requests

BASE_URL = "https://api.openf1.org/v1"

def get_sessions():
    url = f"{BASE_URL}/sessions"
    response = requests.get(url)
    return response.json()

def get_laps(session_key):
    url = f"{BASE_URL}/laps?session_key={session_key}"
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    sessions = get_sessions()
    print(sessions[:2])
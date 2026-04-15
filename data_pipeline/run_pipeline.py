from data_pipeline.extract_openf1 import get_sessions, get_drivers, get_laps
from data_pipeline.load_openf1 import load_sessions, load_drivers, load_laps

def run():
    sessions = get_sessions()
    sessions_2026 = [s for s in sessions if s.get("year") == 2026]
    sessions_2026 = sessions_2026[:2]

    for session in sessions_2026:
        session_key = session["session_key"]

        drivers = get_drivers(session_key)
        load_drivers(drivers)

        laps = get_laps(session_key)
        load_laps(laps)

        print(f"Loaded session {session_key}")

if __name__ == "__main__":
    run()
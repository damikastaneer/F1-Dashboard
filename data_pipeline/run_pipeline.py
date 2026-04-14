from data_pipeline.extract_openf1 import get_sessions, get_drivers, get_laps
from data_pipeline.load_openf1 import load_sessions, load_drivers, load_laps

def run():
    sessions = get_sessions()
    drivers = get_drivers()
    laps = get_laps()

    print(f"{len(sessions)} sessions opgehaald")
    load_sessions(sessions)
    print(sessions[0])
    print("Sessions loaded into database")

    print(f"{len(laps)} laps opgehaald")
    load_laps(laps)
    print(laps[0])
    print("Laps loaded into database")

    print(f"{len(drivers)} drivers opgehaald")
    load_drivers(drivers)
    print(drivers[0])
    print("Drivers loaded into database")

if __name__ == "__main__":
    run()
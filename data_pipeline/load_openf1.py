from sqlalchemy import text
from db.database import engine

def load_sessions(sessions: list[dict]) -> None:
    query = text("""
        INSERT INTO sessions (
            session_key,
            session_name,
            session_type,
            date_start,
            date_end,
            year,
            country_key,
            country_code,
            country_name,
            location,
            circuit_key,
            circuit_short_name
        )
        VALUES (
            :session_key,
            :session_name,
            :session_type,
            :date_start,
            :date_end,
            :year,
            :country_key,
            :country_code,
            :country_name,
            :location,
            :circuit_key,
            :circuit_short_name
        )
        ON CONFLICT (session_key) DO NOTHING
    """)

    with engine.begin() as conn:
        for s in sessions:
            conn.execute(query, {
                "session_key": s.get("session_key"),
                "session_name": s.get("session_name"),
                "session_type": s.get("session_type"),
                "date_start": s.get("date_start"),
                "date_end": s.get("date_end"),
                "year": s.get("year"),
                "country_key": s.get("country_key"),
                "country_code": s.get("country_code"),
                "country_name": s.get("country_name"),
                "location": s.get("location"),
                "circuit_key": s.get("circuit_key"),
                "circuit_short_name": s.get("circuit_short_name"),
            })


def load_drivers(drivers: list[dict]) -> None:
    query = text("""
        INSERT INTO drivers (
            driver_number,
            first_name,
            last_name,
            full_name,
            headshot_url,
            team_name,
            team_colour,
            country_code,
            broadcast_name,
            name_acronym)
        VALUES (
            :driver_number,
            :first_name,
            :last_name,
            :full_name,
            :headshot_url,
            :team_name,
            :team_colour,
            :country_code,
            :broadcast_name,
            :name_acronym
            )
        ON CONFLICT (driver_number) DO NOTHING
    """)

    with engine.begin() as conn:
        for d in drivers:
            conn.execute(query, {
                "driver_number": d.get("driver_number"),
                "first_name": d.get("first_name"),
                "last_name": d.get("last_name"),
                "full_name": d.get("full_name"),
                "headshot_url": d.get("headshot_url"),
                "team_name": d.get("team_name"),
                "team_colour": d.get("team_colour"),
                "country_code": d.get("country_code"),
                "broadcast_name": d.get("broadcast_name"),
                "name_acronym": d.get("name_acronym"),
            })
    
def load_laps(laps: list[dict]) -> None:
    query = text("""
        INSERT INTO laps (
            lap_number,
            lap_duration,
            date_start,
            session_key,
            driver_number,
            duration_sector_1,
            duration_sector_2,
            duration_sector_3,
            is_pit_out_lap
            )
        VALUES (
            :lap_number,
            :lap_duration,
            :date_start,
            :session_key,
            :driver_number,
            :duration_sector_1,
            :duration_sector_2,
            :duration_sector_3,
            :is_pit_out_lap
        )
        ON CONFLICT (session_key, driver_number, lap_number) DO NOTHING
        """)
    
    with engine.begin() as conn:
        for l in laps:
            if l.get("session_key") is None or l.get("driver_number") is None or l.get("lap_number") is None:
                continue

            conn.execute(query, {
                "lap_number": l.get("lap_number"),
                "lap_duration": l.get("lap_duration"),
                "date_start": l.get("date_start"),
                "session_key": l.get("session_key"),
                "driver_number": l.get("driver_number"),
                "duration_sector_1": l.get("duration_sector_1"),
                "duration_sector_2": l.get("duration_sector_2"),
                "duration_sector_3": l.get("duration_sector_3"),
                "is_pit_out_lap": l.get("is_pit_out_lap"),
            })
    
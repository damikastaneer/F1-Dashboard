CREATE TABLE drivers (
    driver_number INT PRIMARY KEY,
    first_name VARCHAR(30),
    last_name VARCHAR(50),
    full_name VARCHAR(80),
    headshot_url VARCHAR(255),
    team_name VARCHAR(50),
    team_colour VARCHAR(20),
    country_code VARCHAR(10),
    broadcast_name VARCHAR(50) NOT NULL,
    name_acronym VARCHAR(10) NOT NULL
);

CREATE TABLE sessions (
    session_key INT PRIMARY KEY,
    session_name VARCHAR(50) NOT NULL,
    session_type VARCHAR(30) NOT NULL,
    date_start TIMESTAMP NOT NULL,
    date_end TIMESTAMP NOT NULL,
    year INT NOT NULL,
    country_key INT,
    country_code VARCHAR(10),
    country_name VARCHAR(50),
    location VARCHAR(100),
    circuit_key INT,
    circuit_short_name VARCHAR(30)
);


CREATE TABLE laps (
    id SERIAL PRIMARY KEY,
    lap_number INT NOT NULL,
    lap_duration FLOAT,
    date_start TIMESTAMP,
    session_key INT NOT NULL REFERENCES sessions(session_key),
    driver_number INT NOT NULL REFERENCES drivers(driver_number),
    duration_sector_1 FLOAT,
    duration_sector_2 FLOAT,
    duration_sector_3 FLOAT,
    is_pit_out_lap BOOLEAN NOT NULL,
    CONSTRAINT unique_lap_per_driver UNIQUE (session_key, driver_number, lap_number)
);
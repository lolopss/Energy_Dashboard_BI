CREATE DATABASE energy_dashboard;

\c energy_dashboard;

CREATE TABLE energy_consumption (
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    energy_type VARCHAR(50) NOT NULL,
    consumption_kwh INTEGER NOT NULL,
    building_id INTEGER NOT NULL
);
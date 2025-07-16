-- Consommation totale par type d'énergie
SELECT energy_type, SUM(consumption_kwh) AS total_kwh
FROM energy_consumption
GROUP BY energy_type;

-- Consommation quotidienne moyenne
SELECT date, AVG(consumption_kwh) AS avg_kwh
FROM energy_consumption
GROUP BY date
ORDER BY date;

-- Consommation par bâtiment
SELECT building_id, SUM(consumption_kwh) AS total_kwh
FROM energy_consumption
GROUP BY building_id;
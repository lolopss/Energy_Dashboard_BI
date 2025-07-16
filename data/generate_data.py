import pandas as pd
import random
from datetime import datetime, timedelta

# Set random seed for reproducibility
random.seed(42)

start_date = datetime.strptime("2024-01-01", "%Y-%m-%d")
energy_types = ["Electricity (kwh)", "Gas (m3)", "Water (m3)"]
data = []

# Generate 50 data points
for i in range(50):
    date = start_date + timedelta(days=i % 15)
    energy_type = random.choice(energy_types)
    consumption = random.randint(30, 200)
    building_id = 1
    data.append([date.strftime("%Y-%m-%d"), energy_type, consumption, building_id])

# DataFrame conversion
df = pd.DataFrame(data, columns=["date", "energy_type", "consumption", "building_id"])

# Save to CSV file
csv_path = "energy_consumption.csv"
df.to_csv(csv_path, index=False)
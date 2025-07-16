import pandas as pd
import random
from datetime import datetime, timedelta

# Set random seed for reproducibility
random.seed(42)

start_date = datetime.strptime("2024-01-01", "%Y-%m-%d")
energy_types = ["Electricity", "Gas", "Water"]
data = []

# Generate 50 data points
for i in range(50):
    date = start_date + timedelta(days=i % 15)
    energy_type = random.choice(energy_types)
    consumption_kwh = random.randint(30, 200)
    building_id = 1
    data.append([date.strftime("%Y-%m-%d"), energy_type, consumption_kwh, building_id])

# DataFrame conversion
df = pd.DataFrame(data, columns=["date", "energy_type", "consumption_kwh", "building_id"])

# Save to CSV file
csv_path = "energy_consumption.csv"
df.to_csv(csv_path, index=False)
import pandas as pd
import numpy as np
import random
import os

# Ensure output folder exists
os.makedirs("data/raw", exist_ok=True)

# Read bases table
bases_df = pd.read_csv("data/raw/bases.csv")

# Number of fuel log records
num_logs = 120000

vehicle_types = [
    "Tank",
    "Truck",
    "Jeep",
    "Generator",
    "Helicopter",
    "Transport Vehicle"
]

fuel_logs = []

for i in range(num_logs):

    fuel_id = f"F{i+1:06d}"

    # Select a random base
    base = bases_df.sample(1).iloc[0]

    base_id = base["Base_ID"]

    region = base["Region"]

    # Random date in 2025–2026
    date = pd.Timestamp("2025-01-01") + pd.to_timedelta(
        np.random.randint(0,730),
        unit="D"
    )

    vehicle = random.choice(vehicle_types)

    # Fuel consumption depends on vehicle type
    if vehicle == "Tank":
        fuel_consumed = round(np.random.uniform(500,900),2)

    elif vehicle == "Helicopter":
        fuel_consumed = round(np.random.uniform(400,700),2)

    elif vehicle == "Truck":
        fuel_consumed = round(np.random.uniform(200,450),2)

    elif vehicle == "Transport Vehicle":
        fuel_consumed = round(np.random.uniform(180,350),2)

    elif vehicle == "Generator":
        fuel_consumed = round(np.random.uniform(80,180),2)

    else:
        fuel_consumed = round(np.random.uniform(40,120),2)

    # Approximate diesel cost
    fuel_cost = round(fuel_consumed * np.random.uniform(90,100),2)

    fuel_logs.append({
        "Fuel_ID": fuel_id,
        "Date": date,
        "Base_ID": base_id,
        "Region": region,
        "Vehicle_Type": vehicle,
        "Fuel_Consumed_Liters": fuel_consumed,
        "Fuel_Cost_INR": fuel_cost
    })

fuel_df = pd.DataFrame(fuel_logs)

print(fuel_df.head())

print("\nShape:", fuel_df.shape)

fuel_df.to_csv(
    "data/raw/fuel_logs.csv",
    index=False
)

print("\nfuel_logs.csv created successfully!")
import pandas as pd
import numpy as np
import random
import os

# Ensure output folder exists
os.makedirs("data/raw", exist_ok=True)

# Read existing tables
equipment_df = pd.read_csv("data/raw/equipment.csv")
bases_df = pd.read_csv("data/raw/bases.csv")

# Number of maintenance records
num_records = 50000

maintenance_types = [
    "Preventive",
    "Corrective",
    "Emergency",
    "Inspection"
]

technicians = [
    "Team Alpha",
    "Team Bravo",
    "Team Charlie",
    "Team Delta",
    "Team Echo"
]

maintenance = []

for i in range(num_records):

    maintenance_id = f"M{i+1:06d}"

    # Select random equipment
    equipment = equipment_df.sample(1).iloc[0]

    # Select random base
    base = bases_df.sample(1).iloc[0]

    equipment_id = equipment["Equipment_ID"]
    base_id = base["Base_ID"]

    purchase_year = equipment["Purchase_Year"]

    equipment_age = 2026 - purchase_year

    maintenance_type = random.choice(maintenance_types)

    maintenance_date = pd.Timestamp("2025-01-01") + pd.to_timedelta(
        np.random.randint(0,730),
        unit="D"
    )

    # Older equipment generally has higher downtime
    if equipment_age > 15:
        downtime_days = np.random.randint(5,21)
    elif equipment_age > 8:
        downtime_days = np.random.randint(2,10)
    else:
        downtime_days = np.random.randint(0,5)

    maintenance_cost = round(
        downtime_days * np.random.uniform(15000,50000),
        2
    )

    # Failure label (used later for ML)
    if downtime_days >= 8:
        failure = "Yes"
    else:
        failure = "No"

    technician = random.choice(technicians)

    maintenance.append({
        "Maintenance_ID": maintenance_id,
        "Equipment_ID": equipment_id,
        "Base_ID": base_id,
        "Maintenance_Date": maintenance_date,
        "Maintenance_Type": maintenance_type,
        "Downtime_Days": downtime_days,
        "Maintenance_Cost_INR": maintenance_cost,
        "Technician_Team": technician,
        "Failure": failure
    })

maintenance_df = pd.DataFrame(maintenance)

print(maintenance_df.head())

print("\nShape:", maintenance_df.shape)

maintenance_df.to_csv(
    "data/raw/maintenance.csv",
    index=False
)

print("\nmaintenance.csv created successfully!")
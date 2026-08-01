import pandas as pd
import numpy as np
import random
import os

# Ensure output folder exists
os.makedirs("data/raw", exist_ok=True)

# Read bases table
bases_df = pd.read_csv("data/raw/bases.csv")

# Number of mission records
num_missions = 20000

mission_types = [
    "Border Patrol",
    "Training Exercise",
    "Disaster Relief",
    "Reconnaissance",
    "Equipment Transport",
    "Medical Support",
    "Supply Delivery",
    "Surveillance"
]

priorities = [
    "Low",
    "Medium",
    "High",
    "Critical"
]

weather_conditions = [
    "Clear",
    "Rain",
    "Fog",
    "Snow",
    "Storm"
]

mission_status = [
    "Completed",
    "Delayed",
    "Cancelled"
]

missions = []

for i in range(num_missions):

    mission_id = f"MIS{i+1:06d}"

    # Select random base
    base = bases_df.sample(1).iloc[0]

    base_id = base["Base_ID"]
    region = base["Region"]

    mission_type = random.choice(mission_types)

    priority = random.choices(
        priorities,
        weights=[20, 35, 30, 15]
    )[0]

    weather = random.choice(weather_conditions)

    mission_date = pd.Timestamp("2025-01-01") + pd.to_timedelta(
        np.random.randint(0,730),
        unit="D"
    )

    duration_hours = np.random.randint(4,73)

    personnel = np.random.randint(20,401)

    budget = round(
        np.random.uniform(100000,5000000),
        2
    )

    # Success probability based on weather and priority
    if weather in ["Storm", "Snow"]:
        status = random.choices(
            mission_status,
            weights=[65,25,10]
        )[0]

    elif priority == "Critical":
        status = random.choices(
            mission_status,
            weights=[90,8,2]
        )[0]

    else:
        status = random.choices(
            mission_status,
            weights=[85,10,5]
        )[0]

    missions.append({

        "Mission_ID": mission_id,
        "Mission_Date": mission_date,
        "Base_ID": base_id,
        "Region": region,
        "Mission_Type": mission_type,
        "Priority": priority,
        "Weather": weather,
        "Duration_Hours": duration_hours,
        "Personnel_Deployed": personnel,
        "Budget_INR": budget,
        "Mission_Status": status

    })

missions_df = pd.DataFrame(missions)

print(missions_df.head())

print("\nShape:", missions_df.shape)

missions_df.to_csv(
    "data/raw/missions.csv",
    index=False
)

print("\nmissions.csv created successfully!")
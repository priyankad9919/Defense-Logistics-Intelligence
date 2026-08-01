import pandas as pd
import numpy as np
from faker import Faker
import random
import os
fake=Faker()
num_bases=30
regions=[
    'North',
    'South',
    'East',
    'West',
    'Central'
]
mission_types=[
    "Border Security",
    "Training",
    "Logistics",
    "Reconnaissance",
    "Disaster Relief"
]
base_names=[
    "Alpha Base",
    "Bravo Base",
    "Charlie Base",
    "Delta Base",
    "Echo Base",
    "Foxtrot Base",
    "Golf Base",
    "Hotel Base",
    "India Base",
    "Juliet Base",
    "Kilo Base",
    "Lima Base",
    "Mike Base",
    "November Base",
    "Oscar Base",
    "Papa Base",
    "Quebec Base",
    "Romeo Base",
    "Sierra Base",
    "Tango Base",
    "Uniform Base",
    "Victor Base",
    "Whiskey Base",
    "X-ray Base",
    "Yankee Base",
    "Zulu Base",
    "Falcon Base",
    "Eagle Base",
    "Tiger Base",
    "Lion Base"
]
bases=[]
for i in range(num_bases):
    base_id=f"B{i+1:03d}"
    base_name=base_names[i]
    region=random.choice(regions)
    latitude=round(np.random.uniform(8.0,35.0),4)
    longitude=round(np.random.uniform(68.0,97.0),4)
    personnel=np.random.randint(500,5001)
    mission=random.choice(mission_types)
    bases.append({
        "Base_ID": base_id,
        "Base_Name": base_name,
        "Region": region,
        "Latitude": latitude,
        "Longitude": longitude,
        "Personnel": personnel,
        "Mission_Type": mission
    })  
bases_df=pd.DataFrame(bases)
print(bases_df)
bases_df.to_csv("data/raw/bases.csv", index=False)
print("bases.csv created successfully!")

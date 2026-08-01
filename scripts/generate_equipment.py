import pandas as pd
import numpy as np
import random
import os
suppliers_df=pd.read_csv("data/raw/suppliers.csv")
# Number of equipment records
num_equipment = 5000

# Equipment categories
equipment_categories = [
    "Tank",
    "Truck",
    "Drone",
    "Radar",
    "Generator",
    "Communication System",
    "Armored Vehicle",
    "Missile Launcher"
]

# Manufacturers (fictional or public defense manufacturers)
manufacturers = [
    "Bharat Dynamics",
    "HAL",
    "BEL",
    "DRDO",
    "Tata Advanced Systems",
    "L&T Defence",
    "Mahindra Defence",
    "Ashok Leyland Defence"
]

# Equipment status
status_list = [
    "Operational",
    "Maintenance",
    "Out of Service"
]

equipment = []

for i in range(num_equipment):

    equipment_id = f"EQ{i+1:05d}"

    category = random.choice(equipment_categories)

    manufacturer = random.choice(manufacturers)
    supplier = suppliers_df.sample(1).iloc[0]

    supplier_id = supplier["Supplier_ID"]
    purchase_year = np.random.randint(2005, 2026)

    expected_life = np.random.randint(10, 31)

    # Older equipment is more likely to need maintenance
    equipment_age = 2026 - purchase_year

    if equipment_age > 15:
        status = random.choices(
            ["Operational", "Maintenance", "Out of Service"],
            weights=[50, 35, 15]
        )[0]
    else:
        status = random.choices(
            ["Operational", "Maintenance", "Out of Service"],
            weights=[85, 10, 5]
        )[0]

    equipment.append({
        "Equipment_ID": equipment_id,
        "Supplier_ID": supplier_id,
        "Equipment_Name": category,
        "Category": category,
        "Manufacturer": manufacturer,
        "Purchase_Year": purchase_year,
        "Expected_Life": expected_life,
        "Status": status
    })

equipment_df = pd.DataFrame(equipment)

print(equipment_df.head())

print("\nShape:", equipment_df.shape)

equipment_df.to_csv(
    "data/raw/equipment.csv",
    index=False
)

print("\nequipment.csv created successfully!")
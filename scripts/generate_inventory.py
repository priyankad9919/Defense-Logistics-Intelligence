import pandas as pd
import numpy as np
import random
import os

# Ensure output folder exists
os.makedirs("data/raw", exist_ok=True)

# Read existing tables
bases_df = pd.read_csv("data/raw/bases.csv")
equipment_df = pd.read_csv("data/raw/equipment.csv")

# Number of inventory records
num_inventory = 100000

inventory = []

for i in range(num_inventory):

    inventory_id = f"INV{i+1:06d}"

    # Select a random base
    base = bases_df.sample(1).iloc[0]

    # Select a random equipment
    equipment = equipment_df.sample(1).iloc[0]

    base_id = base["Base_ID"]
    equipment_id = equipment["Equipment_ID"]

    # Total quantity available at the base
    quantity = np.random.randint(5, 101)

    # Available quantity cannot exceed total quantity
    available = np.random.randint(0, quantity + 1)

    # Reorder level (minimum stock level)
    reorder_level = np.random.randint(5, 31)

    # Inventory health
    if available <= reorder_level:
        inventory_status = "Low Stock"
    elif available <= quantity * 0.50:
        inventory_status = "Medium Stock"
    else:
        inventory_status = "Healthy"

    inventory.append({
        "Inventory_ID": inventory_id,
        "Base_ID": base_id,
        "Equipment_ID": equipment_id,
        "Quantity": quantity,
        "Available": available,
        "Reorder_Level": reorder_level,
        "Inventory_Status": inventory_status
    })

# Create DataFrame
inventory_df = pd.DataFrame(inventory)

# Preview
print(inventory_df.head())

print("\nShape:", inventory_df.shape)

# Save CSV
inventory_df.to_csv(
    "data/raw/inventory.csv",
    index=False
)

print("\ninventory.csv created successfully!")
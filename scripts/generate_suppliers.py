import pandas as pd
import numpy as np
import random
import os

# Ensure output folder exists
os.makedirs("data/raw", exist_ok=True)

# Number of suppliers
num_suppliers = 300

supplier_names = [
    "Alpha Logistics",
    "Bravo Engineering",
    "Delta Industrial Solutions",
    "Eagle Technologies",
    "Falcon Manufacturing",
    "Prime Defense Systems",
    "Pioneer Equipment",
    "National Engineering",
    "Vertex Industries",
    "Titan Manufacturing",
    "Skyline Technologies",
    "Precision Engineering",
    "Summit Industrial",
    "Dynamic Systems",
    "Frontier Logistics"
]

cities = [
    "Delhi",
    "Mumbai",
    "Kolkata",
    "Chennai",
    "Bengaluru",
    "Hyderabad",
    "Pune",
    "Lucknow",
    "Jaipur",
    "Ahmedabad"
]

equipment_categories = [
    "Vehicles",
    "Electronics",
    "Communication",
    "Generators",
    "Engineering Equipment",
    "Medical Equipment",
    "Drones",
    "Radar Systems"
]

suppliers = []

for i in range(num_suppliers):

    supplier_id = f"SUP{i+1:04d}"

    supplier_name = random.choice(supplier_names) + f" {i+1}"

    city = random.choice(cities)

    category = random.choice(equipment_categories)

    years_experience = np.random.randint(5, 41)

    annual_contract_value = round(
        np.random.uniform(5_000_000, 500_000_000),
        2
    )

    delivery_days = np.random.randint(2, 31)

    quality_rating = round(
        np.random.uniform(3.0, 5.0),
        1
    )

    on_time_delivery = round(
        np.random.uniform(75, 100),
        1
    )

    suppliers.append({

        "Supplier_ID": supplier_id,
        "Supplier_Name": supplier_name,
        "City": city,
        "Equipment_Category": category,
        "Years_Experience": years_experience,
        "Annual_Contract_Value_INR": annual_contract_value,
        "Average_Delivery_Days": delivery_days,
        "Quality_Rating": quality_rating,
        "On_Time_Delivery_Percentage": on_time_delivery

    })

suppliers_df = pd.DataFrame(suppliers)

print(suppliers_df.head())

print("\nShape:", suppliers_df.shape)

suppliers_df.to_csv(
    "data/raw/suppliers.csv",
    index=False
)

print("\nsuppliers.csv created successfully!")
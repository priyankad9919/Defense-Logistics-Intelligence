import os
import pandas as pd

# --------------------------------------------------
# Create output folders
# --------------------------------------------------

os.makedirs("data/processed", exist_ok=True)
os.makedirs("reports", exist_ok=True)

# --------------------------------------------------
# Load datasets
# --------------------------------------------------

print("Loading datasets...")

bases = pd.read_csv("data/raw/bases.csv")
equipment = pd.read_csv("data/raw/equipment.csv")
inventory = pd.read_csv("data/raw/inventory.csv")
fuel = pd.read_csv("data/raw/fuel_logs.csv")
maintenance = pd.read_csv("data/raw/maintenance.csv")
missions = pd.read_csv("data/raw/missions.csv")
suppliers = pd.read_csv("data/raw/suppliers.csv")

# --------------------------------------------------
# Data Quality Report
# --------------------------------------------------

report = []

def log(table, before, after, duplicates):

    report.append({
        "Table": table,
        "Rows Before": before,
        "Rows After": after,
        "Duplicates Removed": duplicates
    })

# --------------------------------------------------
# Generic Cleaning Function
# --------------------------------------------------

def clean_dataframe(df, table_name):

    before = len(df)

    duplicates = df.duplicated().sum()

    df = df.drop_duplicates()

    # Remove leading/trailing spaces
    obj_cols = df.select_dtypes(include="object").columns

    for col in obj_cols:

        df[col] = df[col].astype(str).str.strip()

    # Fill missing numeric values
    num_cols = df.select_dtypes(include=["int64","float64"]).columns

    for col in num_cols:

        df[col] = df[col].fillna(df[col].median())

    # Fill missing text values
    for col in obj_cols:

        df[col] = df[col].fillna("Unknown")

    after = len(df)

    log(table_name, before, after, duplicates)

    return df

# --------------------------------------------------
# Clean every table
# --------------------------------------------------

bases = clean_dataframe(bases, "bases")
equipment = clean_dataframe(equipment, "equipment")
inventory = clean_dataframe(inventory, "inventory")
fuel = clean_dataframe(fuel, "fuel_logs")
maintenance = clean_dataframe(maintenance, "maintenance")
missions = clean_dataframe(missions, "missions")
suppliers = clean_dataframe(suppliers, "suppliers")

# --------------------------------------------------
# Convert dates
# --------------------------------------------------

fuel["Date"] = pd.to_datetime(fuel["Date"])

maintenance["Maintenance_Date"] = pd.to_datetime(
    maintenance["Maintenance_Date"]
)

missions["Mission_Date"] = pd.to_datetime(
    missions["Mission_Date"]
)

# --------------------------------------------------
# Standardize Regions
# --------------------------------------------------

bases["Region"] = bases["Region"].str.title()
fuel["Region"] = fuel["Region"].str.title()
missions["Region"] = missions["Region"].str.title()

# --------------------------------------------------
# Range Validation
# --------------------------------------------------

fuel = fuel[fuel["Fuel_Consumed_Liters"] >= 0]

maintenance = maintenance[
    maintenance["Maintenance_Cost_INR"] >= 0
]

inventory = inventory[
    inventory["Quantity"] >= 0
]

missions = missions[
    missions["Budget_INR"] >= 0
]

# --------------------------------------------------
# Foreign Key Validation
# --------------------------------------------------

valid_base_ids = set(bases["Base_ID"])

fuel = fuel[
    fuel["Base_ID"].isin(valid_base_ids)
]

inventory = inventory[
    inventory["Base_ID"].isin(valid_base_ids)
]

maintenance = maintenance[
    maintenance["Base_ID"].isin(valid_base_ids)
]

missions = missions[
    missions["Base_ID"].isin(valid_base_ids)
]

valid_equipment_ids = set(equipment["Equipment_ID"])

inventory = inventory[
    inventory["Equipment_ID"].isin(valid_equipment_ids)
]

maintenance = maintenance[
    maintenance["Equipment_ID"].isin(valid_equipment_ids)
]

if "Supplier_ID" in equipment.columns:

    valid_supplier_ids = set(suppliers["Supplier_ID"])

    equipment = equipment[
        equipment["Supplier_ID"].isin(valid_supplier_ids)
    ]

# --------------------------------------------------
# Feature Engineering
# --------------------------------------------------

equipment["Equipment_Age"] = (
    2026 - equipment["Purchase_Year"]
)

inventory["Inventory_Utilization"] = (
    inventory["Available"] /
    inventory["Quantity"]
).round(2)

maintenance["Cost_Per_Day"] = (
    maintenance["Maintenance_Cost_INR"] /
    maintenance["Downtime_Days"].replace(0,1)
).round(2)

fuel["Fuel_Cost_Per_Liter"] = (
    fuel["Fuel_Cost_INR"] /
    fuel["Fuel_Consumed_Liters"]
).round(2)

missions["Budget_Per_Person"] = (
    missions["Budget_INR"] /
    missions["Personnel_Deployed"]
).round(2)

# --------------------------------------------------
# Save cleaned files
# --------------------------------------------------

bases.to_csv(
    "data/processed/bases_clean.csv",
    index=False
)

equipment.to_csv(
    "data/processed/equipment_clean.csv",
    index=False
)

inventory.to_csv(
    "data/processed/inventory_clean.csv",
    index=False
)

fuel.to_csv(
    "data/processed/fuel_logs_clean.csv",
    index=False
)

maintenance.to_csv(
    "data/processed/maintenance_clean.csv",
    index=False
)

missions.to_csv(
    "data/processed/missions_clean.csv",
    index=False
)

suppliers.to_csv(
    "data/processed/suppliers_clean.csv",
    index=False
)

# --------------------------------------------------
# Save Report
# --------------------------------------------------

report_df = pd.DataFrame(report)

report_df.to_csv(
    "reports/data_quality_report.csv",
    index=False
)

print("\nCleaning completed successfully!")

print("\nProcessed files saved to data/processed")

print("\nData Quality Report saved to reports/")
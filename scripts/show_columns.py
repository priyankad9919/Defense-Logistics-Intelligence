import pandas as pd

files = [
    "bases_clean.csv",
    "equipment_clean.csv",
    "inventory_clean.csv",
    "fuel_logs_clean.csv",
    "maintenance_clean.csv",
    "missions_clean.csv",
    "suppliers_clean.csv"
]

for file in files:
    df = pd.read_csv(f"data/processed/{file}")
    print("=" * 60)
    print(file)
    print(df.columns.tolist())
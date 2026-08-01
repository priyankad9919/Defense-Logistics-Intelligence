-- Import bases

COPY bases
FROM 'C:/Defense-Logistics-Intelligence/data/processed/bases_clean.csv'
DELIMITER ','
CSV HEADER;

-- Import suppliers

COPY suppliers
FROM 'C:/Defense-Logistics-Intelligence/data/processed/suppliers_clean.csv'
DELIMITER ','
CSV HEADER;

-- Import equipment

COPY equipment
FROM 'C:/Defense-Logistics-Intelligence/data/processed/equipment_clean.csv'
DELIMITER ','
CSV HEADER;

-- Import inventory

COPY inventory
FROM 'C:/Defense-Logistics-Intelligence/data/processed/inventory_clean.csv'
DELIMITER ','
CSV HEADER;

-- Import fuel logs

COPY fuel_logs
FROM 'C:/Defense-Logistics-Intelligence/data/processed/fuel_logs_clean.csv'
DELIMITER ','
CSV HEADER;

-- Import maintenance

COPY maintenance
FROM 'C:/Defense-Logistics-Intelligence/data/processed/maintenance_clean.csv'
DELIMITER ','
CSV HEADER;

-- Import missions

COPY missions
FROM 'C:/Defense-Logistics-Intelligence/data/processed/missions_clean.csv'
DELIMITER ','
CSV HEADER;
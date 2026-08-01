-- Section 1: Basic Business KPIs
-- Query 1 – Total number of military bases
SELECT COUNT(*) AS Total_Bases
FROM bases;
-- Query 2 – Total equipment
SELECT COUNT(*) AS Total_Equipment
FROM equipment;
-- Query 3 – Total suppliers
SELECT COUNT(*) AS Total_Suppliers
FROM suppliers;
-- Query 4 – Total missions
SELECT COUNT(*) AS Total_Missions
FROM missions;
-- Query 5 – Total fuel consumed
SELECT
    ROUND(SUM(Fuel_Consumed_Liters),2) AS Total_Fuel_Consumed
FROM fuel_logs;

-- Section 2: Base Analysis
-- Query 6 – Personnel by region
SELECT
    Region,
    SUM(Personnel) AS Total_Personnel
FROM bases
GROUP BY Region
ORDER BY Total_Personnel DESC;
-- Query 7 – Average personnel
SELECT
    ROUND(AVG(Personnel),2) AS Average_Personnel
FROM bases;
-- Query 8 – Largest bases
SELECT
    Base_Name,
    Personnel
FROM bases
ORDER BY Personnel DESC
LIMIT 10;

-- Section 3: Equipment Analysis
-- Query 9 – Equipment by category
SELECT
    Category,
    COUNT(*) AS Total
FROM equipment
GROUP BY Category
ORDER BY Total DESC;
-- Query 10 – Equipment status
SELECT
    Status,
    COUNT(*) AS Total
FROM equipment
GROUP BY Status;
-- Query 11 – Oldest equipment
SELECT
    Equipment_Name,
    Equipment_Age
FROM equipment
ORDER BY Equipment_Age DESC
LIMIT 10;
-- Query 12 – Average equipment age
SELECT
    ROUND(AVG(Equipment_Age),2)
FROM equipment;

-- Section 4: Inventory Analytics
-- Query 13 – Low stock inventory
SELECT *
FROM inventory
WHERE Inventory_Status='Low Stock';
-- Query 14 – Inventory utilization
SELECT
    ROUND(AVG(Inventory_Utilization),2)
FROM inventory;
-- Query 15 – Highest inventory
SELECT *
FROM inventory
ORDER BY Quantity DESC
LIMIT 10;

-- Section 5: Fuel Analytics
-- Query 16 – Fuel consumption by region
SELECT
    Region,
    ROUND(SUM(Fuel_Consumed_Liters),2) AS Fuel
FROM fuel_logs
GROUP BY Region
ORDER BY Fuel DESC;
-- Query 17 – Fuel cost by vehicle type
SELECT
    Vehicle_Type,
    ROUND(SUM(Fuel_Cost_INR),2) AS Cost
FROM fuel_logs
GROUP BY Vehicle_Type
ORDER BY Cost DESC;
-- Query 18 – Average fuel price
SELECT
    ROUND(AVG(Fuel_Cost_Per_Liter),2)
FROM fuel_logs;

-- Section 6: Maintenance Analytics
-- Query 19 – Average maintenance cost
SELECT
    ROUND(AVG(Maintenance_Cost_INR),2)
FROM maintenance;
-- Query 20 – Equipment failures
SELECT
    Failure,
    COUNT(*)
FROM maintenance
GROUP BY Failure;
-- Query 21 – Maintenance by type
SELECT
    Maintenance_Type,
    COUNT(*) AS Total
FROM maintenance
GROUP BY Maintenance_Type
ORDER BY Total DESC;
-- Query 22 – Highest maintenance cost
SELECT *
FROM maintenance
ORDER BY Maintenance_Cost_INR DESC
LIMIT 10;

-- Section 7: Mission Analytics
-- Query 23 – Mission status
SELECT
    Mission_Status,
    COUNT(*)
FROM missions
GROUP BY Mission_Status;
-- Query 24 – Mission priority
SELECT
    Priority,
    COUNT(*)
FROM missions
GROUP BY Priority;
-- Query 25 – Budget by region
SELECT
    Region,
    ROUND(SUM(Budget_INR),2) AS Budget
FROM missions
GROUP BY Region
ORDER BY Budget DESC;
-- Query 26 – Average mission duration
SELECT
    ROUND(AVG(Duration_Hours),2)
FROM missions;

-- Section 8: Supplier Analytics
-- Query 27 – Top supplier ratings
SELECT
    Supplier_Name,
    Quality_Rating
FROM suppliers
ORDER BY Quality_Rating DESC
LIMIT 10;
-- Query 28 – Largest contracts
SELECT
    Supplier_Name,
    Annual_Contract_Value_INR
FROM suppliers
ORDER BY Annual_Contract_Value_INR DESC
LIMIT 10;
-- Query 29 – Fastest suppliers
SELECT
    Supplier_Name,
    Average_Delivery_Days
FROM suppliers
ORDER BY Average_Delivery_Days
LIMIT 10;

-- Section 9: Multi-table Analysis
-- Query 30 – Equipment with supplier details
SELECT
    e.Equipment_Name,
    e.Category,
    s.Supplier_Name,
    s.City,
    s.Quality_Rating
FROM equipment e
JOIN suppliers s
ON e.Supplier_ID = s.Supplier_ID;
-- Query 31 – Inventory with base names
SELECT
    b.Base_Name,
    i.Inventory_Status,
    i.Quantity,
    i.Available
FROM inventory i
JOIN bases b
ON i.Base_ID = b.Base_ID;
-- Query 32 – Maintenance with equipment names
SELECT
    e.Equipment_Name,
    m.Maintenance_Type,
    m.Maintenance_Cost_INR,
    m.Downtime_Days
FROM maintenance m
JOIN equipment e
ON m.Equipment_ID = e.Equipment_ID;
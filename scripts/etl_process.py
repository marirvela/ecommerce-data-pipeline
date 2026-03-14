import pandas as pd
import sqlite3

print("Starting ETL Process (Extract, Transform, Load)...")

# --- 1. EXTRACT (Extraer datos de múltiples fuentes) ---
print("\nExtracting data from raw sources...")

# Connect to SQLite (E-commerce system)
conn = sqlite3.connect('data/raw/ecommerce.db')
df_customers = pd.read_sql_query("SELECT * FROM customers", conn)
df_sales = pd.read_sql_query("SELECT * FROM sales", conn)
conn.close()

# Read Excel (Marketing manual file)
df_marketing = pd.read_excel('data/raw/marketing_campaigns.xlsx')

print(f"   - Loaded {len(df_customers)} customers.")
print(f"   - Loaded {len(df_sales)} sales.")
print(f"   - Loaded {len(df_marketing)} marketing campaigns.")

# --- 2. TRANSFORM (Limpiar y procesar los datos) ---
print("\nTransforming and cleaning data...")

# Clean Sales: Fill missing payment methods with 'Unknown'
missing_payments = df_sales['payment_method'].isnull().sum()
print(f"   - Found {missing_payments} sales with missing payment methods. Fixing...")
df_sales['payment_method'] = df_sales['payment_method'].fillna('Unknown')

# Clean Marketing: Remove duplicate rows
duplicates = df_marketing.duplicated().sum()
print(f"   - Found {duplicates} duplicate rows in marketing data. Removing...")
df_marketing = df_marketing.drop_duplicates()

# Clean Marketing: Impute missing costs with the median cost
missing_costs = df_marketing['cost'].isnull().sum()
print(f"   - Found {missing_costs} missing costs in marketing data. Imputing with median...")
median_cost = round(df_marketing['cost'].median(), 2)
df_marketing['cost'] = df_marketing['cost'].fillna(median_cost)

# --- 3. LOAD (Cargar los datos limpios para Power BI) ---
print("\nLoading clean data to 'processed' folder...")

# Save as clean CSV files
df_customers.to_csv('data/processed/clean_customers.csv', index=False)
df_sales.to_csv('data/processed/clean_sales.csv', index=False)
df_marketing.to_csv('data/processed/clean_marketing.csv', index=False)

print("\nETL Process completed successfully! Data is ready for Business Intelligence.")
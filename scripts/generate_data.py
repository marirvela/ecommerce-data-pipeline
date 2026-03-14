import sqlite3
import pandas as pd
from faker import Faker
import random

# Initialize Faker to generate realistic data (we keep the Spanish locale for names/cities so it looks like a LatAm E-commerce)
fake = Faker('es_ES')

# Data volume configuration
NUM_CUSTOMERS = 1000
NUM_SALES = 3000

print("Generating database---------")

# 1. Generate Customers Table
customers = []
for i in range(1, NUM_CUSTOMERS + 1):
    customers.append({
        'customer_id': i,
        'name': fake.name(),
        'email': fake.unique.email(),
        'country': fake.country(),
        'registration_date': fake.date_between(start_date='-2y', end_date='today')
    })

df_customers = pd.DataFrame(customers)

# 2. Generate Sales Table
sales = []
payment_methods = ['Credit Card', 'PayPal', 'Bank Transfer', 'Debit Card']

for i in range(1, NUM_SALES + 1):
    sales.append({
        'sale_id': i,
        'customer_id': random.randint(1, NUM_CUSTOMERS), # Relate sale to an existing customer
        'sale_date': fake.date_between(start_date='-1y', end_date='today'),
        'total_amount': round(random.uniform(15.0, 800.0), 2),
        'payment_method': random.choice(payment_methods)
    })

df_sales = pd.DataFrame(sales)

# --- INJECT INTENTIONAL NOISE (For later data cleaning) ---
# We will make some sales have missing payment methods (NULL)
for _ in range(100):
    idx = random.randint(0, NUM_SALES - 1)
    df_sales.at[idx, 'payment_method'] = None

# 3. Save to SQLite (Local Database Engine)
db_path = 'data/raw/ecommerce.db'
conn = sqlite3.connect(db_path)

# Write DataFrames to SQL database
df_customers.to_sql('customers', conn, if_exists='replace', index=False)
df_sales.to_sql('sales', conn, if_exists='replace', index=False)

conn.close()

print(f"Database created with {NUM_CUSTOMERS} customers and {NUM_SALES} sales.")
print(f"File saved at: {db_path}")
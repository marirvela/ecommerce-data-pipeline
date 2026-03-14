import pandas as pd
import random

print("Generating Marketing Excel file...")

# Create mock data for marketing campaigns
platforms = ['Google Ads', 'Meta Ads', 'TikTok Ads', 'LinkedIn Ads']

campaigns = []
for i in range(1, 51): # 50 campaigns
    campaigns.append({
        'campaign_id': f'CMP-{i}',
        'platform': random.choice(platforms),
        'cost': round(random.uniform(500.0, 5000.0), 2),
        'clicks': random.randint(1000, 15000),
        'signups': random.randint(10, 500)
    })

df_marketing = pd.DataFrame(campaigns)

# --- INJECT INTENTIONAL NOISE (For data cleaning) ---
# 1. Add a duplicate row
df_marketing = pd.concat([df_marketing, df_marketing.iloc[[0]]], ignore_index=True)

# 2. Add some missing costs (NULLs)
df_marketing.at[10, 'cost'] = None
df_marketing.at[25, 'cost'] = None

# Save to Excel in the raw data folder
file_path = 'data/raw/marketing_campaigns.xlsx'
df_marketing.to_excel(file_path, index=False, engine='openpyxl')

print(f"Marketing data with intentional noise saved at: {file_path}")
import pandas as pd

# Load the data
df = pd.read_csv('startup.csv')

# Define category based on features
category_columns = ['is_software', 'is_web', 'is_mobile', 'is_enterprise', 'is_advertising', 'is_gamesvideo', 'is_ecommerce', 'is_biotech', 'is_consulting', 'is_othercategory']
def determine_category(row):
    for col in category_columns:
        if row[col] == 1:
            return col[3:]  # Strip 'is_' prefix
    return 'unknown'  # In case no category is 1

df['category'] = df.apply(determine_category, axis=1)

# Select necessary columns and drop rows with missing coordinates
df = df[['name', 'latitude', 'longitude', 'status', 'funding_total_usd', 'category']]
df = df.dropna(subset=['latitude', 'longitude'])

# Save to JSON
df.to_json('data.json', orient='records')

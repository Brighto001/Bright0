# import pandas as pd
# import psycopg2
# import numpy as np
# from datetime import datetime

# # Load the CSV (adjust the file path as needed)
# df = pd.read_csv(r"C:\full\path\to\Rewards.csv")

# # 1. Delete the 'tags' column
# if 'tags' in df.columns:
#     df.drop(columns=['tags'], inplace=True)

# # 2. Fill empty zip at roll no. 438 with 11011
# df.loc[df['roll no.'] == 438, 'zip'] = 11011

# # 3. Truncate zip codes longer than 5 digits
# df['zip'] = df['zip'].astype(str).str[:5]

# # 4. Fill remaining empty zip codes with mean (converted to int)
# df['zip'] = pd.to_numeric(df['zip'], errors='coerce')
# mean_zip = int(df['zip'].mean(skipna=True))
# df['zip'] = df['zip'].fillna(mean_zip).astype(int)

# # 5. Fix capitalization of Winston Salem
# df['city'] = df['city'].replace(to_replace=r'\bwinston salem\b', value='Winston Salem', regex=True)

# # 6. Remove abbreviations in city column (anything in parentheses)
# df['city'] = df['city'].replace(to_replace=r'\(.*?\)', value='', regex=True).str.strip()
# df['city'] = df['city'].replace('', np.nan)

# # 7. Replace state abbreviations with full names (example for a few states)
# state_map = {
#     'NC': 'North Carolina',
#     'CA': 'California',
#     'NY': 'New York',
#     'TX': 'Texas',
#     'FL': 'Florida'
# }
# df['state'] = df['state'].replace(state_map)

# # 8. Replace empty states with alphabetical list of states (cycle through if needed)
# states_filled = df['state'].copy()
# empty_indices = df[df['state'].isna()].index
# unique_states = sorted(df['state'].dropna().unique())
# for i, idx in enumerate(empty_indices):
#     states_filled.at[idx] = unique_states[i % len(unique_states)]
# df['state'] = states_filled

# # 9. Standardize birthday column format (to YYYY-MM-DD)
# df['birth date'] = pd.to_datetime(df['birth date'], errors='coerce').dt.strftime('%Y-%m-%d')

# # 10. Fill empty birth dates with a fixed date
# df['birth date'] = df['birth date'].fillna('2000-01-01')

# # 11. Remove rows where zip code is less than 5 digits
# df['zip'] = df['zip'].astype(str)
# df = df[df['zip'].str.len() == 5]

# # 12. Fill empty city values with "Thomas Ville"
# df['city'] = df['city'].fillna('Thomas Ville')

# # ==========================
# # PUSH TO POSTGRESQL
# # ==========================

# # Connect to your PostgreSQL DB
# conn = psycopg2.connect(
#     host="localhost",
#     database="your_database",
#     user="your_username",
#     password="your_password"
# )
# cursor = conn.cursor()

# # Replace 'your_table' with the actual table name
# # You might want to truncate the table first if reloading
# cursor.execute("TRUNCATE TABLE your_table")

# # Insert data row-by-row
# for _, row in df.iterrows():
#     cursor.execute("""
#         INSERT INTO your_table (roll_no, zip, city, state, birth_date)
#         VALUES (%s, %s, %s, %s, %s)
#     """, (
#         row['roll no.'],
#         row['zip'],
#         row['city'],
#         row['state'],
#         row['birth date']
#     ))

# conn.commit()
# cursor.close()
# conn.close()

# # print("Data cleaning complete and uploaded to database.")

# # import os
# # # print(os.getcwd())  # This will show you the folder your script is running in



# import pandas as pd
# import numpy as np
# from datetime import datetime
# import random

# # Load the data
# df = pd.read_csv(r"c:\Users\User\Desktop\RewardsData.csv")

# # a. Delete the tags column
# df = df.drop('Tags', axis=1)

# # b. Locate the empty cell on row 438, under the zip column and fill it with the number (11011)
# if pd.isna(df.at[437, 'Zip']):  # row 438 is index 437
#     df.at[437, 'Zip'] = '11011'

# # c. In the zip column, truncate the numbers to the first 5 numbers
# df['Zip'] = df['Zip'].astype(str).str[:5]

# # d. In the zip column, populate all the empty cells with the mean value of the zip column
# # First convert to numeric, handling non-numeric values
# df['Zip'] = pd.to_numeric(df['Zip'], errors='coerce')
# # Calculate mean (ignoring NaN values)
# zip_mean = int(df['Zip'].mean())
# # Fill NaN values with mean
# df['Zip'] = df['Zip'].fillna(zip_mean).astype(int)

# # e. In the city column, replace all instances of Winston Salem with the right capitalization
# df['City'] = df['City'].str.replace('Winston Salem', 'Winston-Salem')
# df['City'] = df['City'].str.replace('Winston-salem', 'Winston-Salem')
# df['City'] = df['City'].str.replace('Winston salem', 'Winston-Salem')

# # f. In the city column, remove every abbreviation and leave the cells empty
# # Assuming abbreviations are single letters (like 'G' in row 6)
# df['City'] = df['City'].apply(lambda x: '' if isinstance(x, str) and len(x.strip()) == 1 else x)

# # g. In the state column, replace every abbreviation with the full state names
# state_mapping = {
#     'AL': 'Alabama', 'AK': 'Alaska', 'AZ': 'Arizona', 'AR': 'Arkansas', 
#     'CA': 'California', 'CO': 'Colorado', 'CT': 'Connecticut', 
#     'DE': 'Delaware', 'FL': 'Florida', 'GA': 'Georgia', 'HI': 'Hawaii', 
#     'ID': 'Idaho', 'IL': 'Illinois', 'IN': 'Indiana', 'IA': 'Iowa', 
#     'KS': 'Kansas', 'KY': 'Kentucky', 'LA': 'Louisiana', 'ME': 'Maine', 
#     'MD': 'Maryland', 'MA': 'Massachusetts', 'MI': 'Michigan', 
#     'MN': 'Minnesota', 'MS': 'Mississippi', 'MO': 'Missouri', 
#     'MT': 'Montana', 'NE': 'Nebraska', 'NV': 'Nevada', 'NH': 'New Hampshire', 
#     'NJ': 'New Jersey', 'NM': 'New Mexico', 'NY': 'New York', 
#     'NC': 'North Carolina', 'ND': 'North Dakota', 'OH': 'Ohio', 
#     'OK': 'Oklahoma', 'OR': 'Oregon', 'PA': 'Pennsylvania', 
#     'RI': 'Rhode Island', 'SC': 'South Carolina', 'SD': 'South Dakota', 
#     'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah', 'VT': 'Vermont', 
#     'VA': 'Virginia', 'WA': 'Washington', 'WV': 'West Virginia', 
#     'WI': 'Wisconsin', 'WY': 'Wyoming', 'DC': 'District of Columbia'
# }

# df['State'] = df['State'].replace(state_mapping)

# # h. Under the state column, replace all the empty cells with state names in alphabetical order
# states_ordered = sorted(state_mapping.values())
# empty_state_count = df['State'].isna().sum()
# state_cycle = states_ordered * (empty_state_count // len(states_ordered) + 1)
# df.loc[df['State'].isna(), 'State'] = state_cycle[:empty_state_count]

# # i. Reformat the dates in the birthday column to the proper format
# def reformat_date(date_str):
#     if pd.isna(date_str):
#         return np.nan
#     try:
#         # Try parsing with different formats
#         for fmt in ('%m/%d/%Y', '%m/%d/%y', '%Y-%m-%d', '%d-%m-%Y', '%d/%m/%Y'):
#             try:
#                 dt = datetime.strptime(str(date_str), fmt)
#                 return dt.strftime('%Y-%m-%d')
#             except ValueError:
#                 continue
#         return np.nan
#     except:
#         return np.nan

# df['Birthdate'] = df['Birthdate'].apply(reformat_date)

# # j. Replace all the empty cells in the birthday column with random birth dates
# def random_date(start_year=1950, end_year=2005):
#     year = random.randint(start_year, end_year)
#     month = random.randint(1, 12)
#     day = random.randint(1, 28)  # Simple approach to avoid invalid dates
#     return f"{year}-{month:02d}-{day:02d}"

# df['Birthdate'] = df['Birthdate'].fillna(df['Birthdate'].apply(lambda x: random_date()))

# # k. In the zip column, delete every row with numbers less than 5
# df = df[df['Zip'] >= 5]

# # l. In the city column, populate all the empty cells with Thomasville
# df['City'] = df['City'].fillna('Thomasville')

# # Save the cleaned data
# df.to_csv('Cleaned_RewardsData.csv', index=False)

# print("Data cleaning complete. Saved to Cleaned_RewardsData.csv")

import pandas as pd
import numpy as np
from datetime import datetime
import random

# Load the data
df = pd.read_csv("RewardsData.csv")

# a. Delete the Tags column (case-sensitive)
if 'Tags' in df.columns:
    df.drop('Tags', axis=1, inplace=True)

# b. Fill empty Zip at row 438 (index 437)
if pd.isna(df.at[437, 'Zip']):
    df.at[437, 'Zip'] = '11011'

# c. Truncate Zip codes to first 5 digits
df['Zip'] = df['Zip'].astype(str).str[:5]

# d. Convert Zip to numeric, fill missing with mean
df['Zip'] = pd.to_numeric(df['Zip'], errors='coerce')
zip_mean = int(df['Zip'].mean(skipna=True))
df['Zip'] = df['Zip'].fillna(zip_mean).astype(int)

# e. Capitalize Winston Salem correctly
df['City'] = df['City'].str.replace(r'(?i)winston[\s-]?salem', 'Winston-Salem', regex=True)

# f. Remove abbreviations in City column (single-letter or short codes)
df['City'] = df['City'].apply(lambda x: np.nan if isinstance(x, str) and len(x.strip()) <= 2 else x)

# g. Replace State abbreviations
state_mapping = {
    'NC': 'North Carolina', 'CA': 'California', 'NY': 'New York',
    'TX': 'Texas', 'FL': 'Florida', 'GA': 'Georgia', 'NJ': 'New Jersey',
    # Add more as needed
}
df['State'] = df['State'].replace(state_mapping)

# h. Fill empty States with alphabetical list (cycled)
states_present = sorted(df['State'].dropna().unique())
empty_indices = df[df['State'].isna()].index
for i, idx in enumerate(empty_indices):
    df.at[idx, 'State'] = states_present[i % len(states_present)]

# i. Fix Birthdate format to YYYY-MM-DD
def reformat_date(date_str):
    if pd.isna(date_str):
        return np.nan
    for fmt in ('%m/%d/%Y', '%m/%d/%y', '%Y-%m-%d', '%d-%m-%Y', '%d/%m/%Y'):
        try:
            return datetime.strptime(str(date_str), fmt).strftime('%Y-%m-%d')
        except ValueError:
            continue
    return np.nan

df['Birthdate'] = df['Birthdate'].apply(reformat_date)

# j. Fill missing birthdates with random dates
def random_birthdate():
    year = random.randint(1950, 2005)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return f"{year}-{month:02d}-{day:02d}"

df['Birthdate'] = df['Birthdate'].fillna(random_birthdate)

# k. Remove rows where Zip is less than 5 digits
df = df[df['Zip'].astype(str).str.len() == 5]

# l. Fill empty City values with "Thomasville"
df['City'] = df['City'].fillna('Thomasville')

# Save cleaned file
df.to_csv(r'C:\Users\hp\Desktop\Cleaned_RewardsData.csv', index=False)
print("✅ Data cleaned and saved to Desktop as 'Cleaned_RewardsData.csv'")



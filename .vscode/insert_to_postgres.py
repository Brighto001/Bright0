import psycopg2
import pandas as pd

# Load the cleaned CSV
df = pd.read_csv(r'C:\Users\hp\Desktop\Cleaned_RewardsData.csv')

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="your_database_name",  # replace this
    user="your_username",           # replace this
    password="your_password"        # replace this
)

cur = conn.cursor()

# Create table
cur.execute("""
    CREATE TABLE IF NOT EXISTS rewards (
        roll_no SERIAL PRIMARY KEY,
        City VARCHAR(100),
        State VARCHAR(100),
        Zip INTEGER,
        Birthdate DATE
    );
""")

# Insert data
for _, row in df.iterrows():
    cur.execute("""
        INSERT INTO rewards (City, State, Zip, Birthdate)
        VALUES (%s, %s, %s, %s)
    """, (row['City'], row['State'], row['Zip'], row['Birthdate']))

conn.commit()
cur.close()
conn.close()

print("✅ Data successfully inserted into PostgreSQL.")

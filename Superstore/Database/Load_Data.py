import sqlite3
import pandas as pd

# Load the dataset from CSV
df = pd.read_csv(r"C:\Users\santo\OneDrive - St. Clair College\Desktop\SEM-1\3 WED Intro to Python\Superstore\Database\Superstore.csv")

# Connect to SQLite database (this will create the file if it doesn't exist)
conn = sqlite3.connect('superstore.db')
cursor = conn.cursor()

# Create the table schema
cursor.execute('''
    CREATE TABLE IF NOT EXISTS superstore (
        Ship_Mode TEXT,
        Segment TEXT,
        Country TEXT,
        City TEXT,
        State TEXT,
        Postal_Code INTEGER,
        Region TEXT,
        Category TEXT,
        Sub_Category TEXT,
        Sales REAL,
        Quantity INTEGER,
        Discount REAL,
        Profit REAL
    )
''')

# Insert the data into the table
df.to_sql('superstore', conn, if_exists='replace', index=False)

# Commit and close the connection
conn.commit()
conn.close()

print("Data inserted successfully into the database.")

import sqlite3

# Connect to SQLite database (creates smart.db if it doesn't exist)
conn = sqlite3.connect("smart.db")

# Execute SQL commands from schema.sql
with open("schema.sql", "r") as f:
    conn.executescript(f.read())

print("Database and tables created successfully!")

conn.close()
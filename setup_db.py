import sqlite3

# Create a new SQLite database (if not already created)
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create users table with username and password columns
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL)''')

# Commit changes and close connection
conn.commit()
conn.close()

print("Database and table created successfully!")

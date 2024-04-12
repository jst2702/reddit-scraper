import sqlite3
from reddit_scraper.db.metadata import DB_PATH

# Connect to SQLite database (create if not exists)
conn = sqlite3.connect(DB_PATH)
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS posts
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              title TEXT,
              author TEXT)''')

# Commit changes and close connection
conn.commit()
conn.close()

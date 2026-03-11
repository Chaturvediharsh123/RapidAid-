import sqlite3

# connect to database
conn = sqlite3.connect("complaints.db", check_same_thread=False)
cursor = conn.cursor()

# create complaints table
cursor.execute("""
CREATE TABLE IF NOT EXISTS complaints(
id INTEGER PRIMARY KEY AUTOINCREMENT,
raw_text TEXT,
issue_type TEXT,
location TEXT,
priority TEXT,
department TEXT
)
""")

conn.commit()


def save_complaint(text, issue, location, priority, department):

    cursor.execute(
        """
        INSERT INTO complaints(raw_text,issue_type,location,priority,department)
        VALUES (?,?,?,?,?)
        """,
        (text, issue, location, priority, department)
    )

    conn.commit()


def get_complaints():

    cursor.execute("SELECT * FROM complaints")

    return cursor.fetchall()
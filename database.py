import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER PRIMARY KEY,
    first_name TEXT,
    username TEXT
)
""")

conn.commit()


def add_user(user_id, first_name="", username=""):
    cursor.execute(
        """
        INSERT OR IGNORE INTO users(user_id, first_name, username)
        VALUES(?,?,?)
        """,
        (user_id, first_name, username),
    )
    conn.commit()


def get_all_users():
    cursor.execute("SELECT user_id FROM users")
    return cursor.fetchall()


def total_users():
    cursor.execute("SELECT COUNT(*) FROM users")
    return cursor.fetchone()[0]

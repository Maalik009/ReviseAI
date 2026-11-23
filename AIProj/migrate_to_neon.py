
import json
import os
import sqlite3
from pathlib import Path

import psycopg
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

DATABASE_URL = os.getenv("DATABASE_URL")
SQLITE_FILE = BASE_DIR / "reviseai.db"

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is missing from .env")

if not SQLITE_FILE.exists():
    raise FileNotFoundError("reviseai.db was not found")

# Read the latest data from SQLite
with sqlite3.connect(SQLITE_FILE) as sqlite_conn:
    rows = sqlite_conn.execute(
        "SELECT name, data FROM app_data"
    ).fetchall()

if not rows:
    raise ValueError("No data was found in the SQLite database")

# Copy the data into Neon
with psycopg.connect(DATABASE_URL) as pg_conn:
    with pg_conn.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS app_data (
                name TEXT PRIMARY KEY,
                data TEXT NOT NULL
            )
        """)

        for name, data in rows:
            cursor.execute(
                """
                INSERT INTO app_data (name, data)
                VALUES (%s, %s)
                ON CONFLICT (name) DO NOTHING
                """,
                (name, data)
            )

print("Migration script finished.")
print("Data categories found:", [name for name, data in rows])

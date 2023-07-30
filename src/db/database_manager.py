import os
import sqlite3
from dotenv import load_dotenv
load_dotenv()

from supabase import create_client

# Load the environment variables

# Get the Supabase URL and Key from the environment variables
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
SQLITE_DBNAME = os.getenv("SQLITE_DBNAME")

def supabase_client():
    return create_client(SUPABASE_URL, SUPABASE_KEY)

def sqlite_client():
    return sqlite3.connect(SQLITE_DBNAME)

# class SQLiteManager(DatabaseManager):
#     def __init__(self):
#         self.connection = None
#         self.cursor = None

#     def connect(self):
#         self.connection = sqlite3.connect(SQLITE_DBNAME)
#         self.cursor = self.connection.cursor()
#         return self

#     def execute_query(self, query):
#         self.cursor.execute(query)
#         return self.cursor.fetchall()

#     def close(self):
#         self.connection.close()
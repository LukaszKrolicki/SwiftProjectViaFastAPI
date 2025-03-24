import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
import psycopg2

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://dbuser:dbpass@localhost:5430/swift_db")

engine = create_engine(DATABASE_URL)

Base = declarative_base()

csv_file_path = os.getenv("CSV_FILE_PATH", "./data/swift_codes.csv")
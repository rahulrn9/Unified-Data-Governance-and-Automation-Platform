import pandas as pd
from pandas_profiling import ProfileReport
import sqlalchemy, os

# Configuration
DB_CONN = "postgresql://username:password@your-rds-endpoint:5432/yourdb"
OUTPUT_DIR = "profiles"

if __name__ == "__main__":
    engine = sqlalchemy.create_engine(DB_CONN)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    tables = ["orders", "customers"]  # list your tables
    for tbl in tables:
        df = pd.read_sql(f"SELECT * FROM {tbl} LIMIT 10000", engine)
        profile = ProfileReport(df, minimal=True)
        profile.to_file(f"{OUTPUT_DIR}/{tbl}.html")
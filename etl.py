import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
import pandas as pd
from sqlalchemy.engine import URL

load_dotenv()

pg_uid = os.environ['PGUID']
pg_pwd = os.environ['PGPASS']

driver = "{ODBC Driver 17 for SQL Server}"
server = "localhost"
database = "AdventureWorksDW2019;"

def extract():
    try:
        connection_string = (
            f'DRIVER={driver};'
            f'SERVER={server};'
            f'DATABASE={database};'
            'Trusted_Connection=yes;'
        )
        connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
        src_conn = create_engine(connection_url)
        tbl_name = "DimProduct"
        df = pd.read_sql_query(f'SELECT * FROM {tbl_name}', src_conn)
        print(f"Extracted {len(df)} rows from {tbl_name}")
        return df, tbl_name
    except Exception as e:
        print("Data extract error: " + str(e))
        return None, None

from urllib.parse import quote_plus

def load(df, tbl):
    try:
        pg_uid_enc = quote_plus(pg_uid)
        pg_pwd_enc = quote_plus(pg_pwd)
        engine = create_engine(f'postgresql://{pg_uid_enc}:{pg_pwd_enc}@{server}:5432/AdventureWorks')
        print(f'importing {len(df)} rows into table stg_{tbl}')
        df.to_sql(f'stg_{tbl}', engine, if_exists='replace', index=False)
        print(f"Data imported successfully: {len(df)} rows")
    except Exception as e:
        print("Data load error: " + str(e))
if __name__ == "__main__":
    print("ETL process started")
    df, tbl = extract()
    if df is not None and not df.empty:
        print("Extraction succeeded, starting load...")
        load(df, tbl)
        print("ETL process finished successfully")
    else:
        print("Extraction failed or returned no data. ETL process aborted.")

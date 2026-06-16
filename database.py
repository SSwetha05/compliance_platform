import psycopg2
import pandas as pd
from config import (Db_Host, Db_Name, Db_User, Db_Password, Db_Port)

def get_connection():
    return psycopg2.connect(
        host=Db_Host,
        database=Db_Name,
        user=Db_User,
        password=Db_Password,
        port=Db_Port
    )


def run_query(query, params=None):
    conn = get_connection()

    try:
        return pd.read_sql(query, conn, params=params)
    finally:
        conn.close()

def execute_query(query, params=None):
    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute(query, params)
        conn.commit()
    finally:
        cur.close()
        conn.close()
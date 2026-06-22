import psycopg2
import pandas as pd
from config import (Db_Host, Db_Name, Db_User, Db_Password, Db_Port)

def get_connection():
    return psycopg2.connect(
        host=Db_Host,
        database=Db_Name,
        user=Db_User,
        password=Db_Password,
        port=Db_Port,
        sslmode = 'require'
    )

def run_query(query, params=None):

    conn = get_connection()

    try:
        return pd.read_sql(
            query,
            conn,
            params=params
        )

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

def get_checklist_details(checklist_id):

    query = """
    SELECT *
    FROM checklists
    WHERE checklist_id = %s
    """

    result = run_query(
        query,
        (checklist_id,)
    )

    if result.empty:
        return None

    return result.iloc[0]

def get_previous_version(checklist_id):

    current = get_checklist_details(
        checklist_id
    )

    if current is None:
        return None

    query = """
    SELECT *
    FROM checklists
    WHERE law_id = %s
      AND version < %s
    ORDER BY version DESC
    LIMIT 1
    """

    result = run_query(
        query,
        (
            int(current["law_id"]),
            int(current["version"])
        )
    )

    if result.empty:
        return None

    return result.iloc[0]
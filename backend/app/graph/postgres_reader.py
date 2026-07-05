import psycopg2
import pandas as pd

from config import POSTGRES


def read_table(table):

    conn = psycopg2.connect(

        host=POSTGRES["host"],

        database=POSTGRES["database"],

        user=POSTGRES["user"],

        password=POSTGRES["password"],

        port=POSTGRES["port"]

    )

    query = f"SELECT * FROM {table};"

    df = pd.read_sql(query, conn)

    conn.close()

    return df
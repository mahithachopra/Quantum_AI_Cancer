import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="quantum_cancer",
    user="postgres",
    password="postgres123",
    port=5432
)

conn.autocommit = True

cursor = conn.cursor()
from sqlalchemy import create_engine
import pandas as pd
import pyodbc
import psycopg2
import snowflake.connector
import requests

# 1 - Replicação PostgreSQL -> SQL Server
def replicate_postgres_to_sqlserver():
    postgres_engine = create_engine("postgresql+psycopg2://user:password@host:port/dbname")
    sqlserver_engine = create_engine("mssql+pyodbc://user:password@host/dbname?driver=ODBC+Driver+17+for+SQL+Server")
    
    df = pd.read_sql("SELECT id, name, age FROM source_table", postgres_engine)
    df.to_sql("destination_table", sqlserver_engine, if_exists='replace', index=False)

# 2 - Replicação SQL Server -> CSV
def replicate_sqlserver_to_csv():
    sqlserver_engine = create_engine("mssql+pyodbc://user:password@host/dbname?driver=ODBC+Driver+17+for+SQL+Server")
    df = pd.read_sql("SELECT id, name, age FROM source_table", sqlserver_engine)
    df.to_csv("output.csv", index=False)

# 3 - Replicação Snowflake -> CSV
def replicate_snowflake_to_csv():
    conn = snowflake.connector.connect(
        user='user',
        password='password',
        account='account',
        database='dbname',
        schema='public'
    )
    df = pd.read_sql("SELECT id, name, age FROM source_table", conn)
    df.to_csv("output.csv", index=False)

# 4 - Replicação PostgreSQL -> Snowflake
def replicate_postgres_to_snowflake():
    postgres_engine = create_engine("postgresql+psycopg2://user:password@host:port/dbname")
    conn = snowflake.connector.connect(
        user='user',
        password='password',
        account='account',
        database='dbname',
        schema='public'
    )
    df = pd.read_sql("SELECT id, name, age FROM source_table", postgres_engine)
    for _, row in df.iterrows():
        conn.cursor().execute(
            "INSERT INTO destination_table (id, name, age) VALUES (%s, %s, %s)",
            (row.id, row.name, row.age)
        )
    conn.commit()

# 5 - Conexão a uma API e gravação no SQL Server
def api_to_sqlserver():
    response = requests.get("https://api.exemplo.com/dados")
    data = response.json()
    df = pd.DataFrame(data)
    sqlserver_engine = create_engine("mssql+pyodbc://user:password@host/dbname?driver=ODBC+Driver+17+for+SQL+Server")
    df.to_sql("destination_table", sqlserver_engine, if_exists='replace', index=False)

# 6 - Envio de dados SQL Server -> API
def sqlserver_to_api():
    sqlserver_engine = create_engine("mssql+pyodbc://user:password@host/dbname?driver=ODBC+Driver+17+for+SQL+Server")
    df = pd.read_sql("SELECT id, name, age FROM source_table", sqlserver_engine)
    
    for _, row in df.iterrows():
        requests.post("https://api.exemplo.com/dados", json=row.to_dict())

if __name__ == "__main__":
    replicate_postgres_to_sqlserver()
    replicate_sqlserver_to_csv()
    replicate_snowflake_to_csv()
    replicate_postgres_to_snowflake()
    api_to_sqlserver()
    sqlserver_to_api()
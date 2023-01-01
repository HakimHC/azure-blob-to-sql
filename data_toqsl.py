import pyodbc
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
import azure.storage.blob as azureblob

def create_sql(data, sqlcon):

    connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": sqlcon})

    engine = create_engine(connection_url)
    con = engine.connect()

    df = pd.read_excel(data)

    df.to_sql('OrdersAzure', con, index=False, if_exists='append')
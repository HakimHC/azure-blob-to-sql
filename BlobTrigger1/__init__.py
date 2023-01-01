import logging
import os
import azure.functions as func
import azure.storage.blob as azureblob
from data_toqsl import create_sql
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

def main(myblob: func.InputStream):
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {myblob.name}")

    constr = os.getenv('connstring')

    blob_client = azureblob.BlobClient.from_blob_url(f"https://excelstorage10.blob.core.windows.net/{myblob.name}")

    try:
        downloaded_blob = blob_client.download_blob()

        create_sql(downloaded_blob.content_as_bytes(), sqlcon=constr)
    except Exception as e:
        logging.error(e)

import os 
import datetime
from azure.storage.blob import BlobClient

def upload_file(filename):
    blob = BlobClient.from_connection_string(conn_str=os.environ["STRING"], container_name=os.environ["CONTAINER"], blob_name=os.path.basename(filename))

    with open(f"{filename}", "rb") as data:
        blob.upload_blob(data)


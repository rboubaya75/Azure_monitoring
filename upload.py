import os 
from azure.storage.blob import BlobService
from dotenv import load_dotenv 
load_dotenv()

service = BlobServiceClient(account_url="https://bartrachidtiphn.blob.core.windows.net/", credential=os.environ["KEY"]) #get the adress on json, primary endpoint 

blob = BlobClient.from_connection_string(conn_str= os.environ["KEY"], container_name="excel", blob_name="my_blob")

with open("/Desktop/Simplon/Monitor/Azure_Monitoring/PJ/MainFile-12-Apr-2021.xls", "rb") as data:
    blob.upload_blob(data)

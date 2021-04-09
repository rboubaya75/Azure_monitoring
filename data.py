

import os
import uuid
import sys
from azure.storage.blob import BlockBlobService, PublicAccess

# ---------------------------------------------------------------------------------------------------------
# Method that creates a test file in the 'Sample' folder.
# This sample application creates a test file, uploads the test file to the Blob storage,
# lists the blobs in the container, and downloads the file with a new name.
# ---------------------------------------------------------------------------------------------------------
# Documentation References:
# Associated Article - https://docs.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-python
# What is a Storage Account - http://azure.microsoft.com/en-us/documentation/articles/storage-whatis-account/
# Getting Started with Blobs-https://docs.microsoft.com/en-us/azure/storage/blobs/storage-python-how-to-use-blob-storage
# Blob Service Concepts - http://msdn.microsoft.com/en-us/library/dd179376.aspx
# Blob Service REST API - http://msdn.microsoft.com/en-us/library/dd135733.aspx
# ----------------------------------------------------------------------------------------------------------


def run_sample():
    try:
        # Create the BlockBlobService that is used to call the Blob service for the storage account
        blob_service_client = BlockBlobService(
            account_name='rachid2', account_key='Sq25Lq6lGlJNTNfpj+j5rBPTSgotvDVS7HmjIF72jYcTzsqVfxXU8k9W237ruMAW4ENmnbjxPBrKxRcU4iU3UA==')

        # Create a container called 'quickstartblobs'.
        container_name = 'rachid'
        blob_service_client.create_container(container_name)

        # Set the permission so the blobs are public.
        blob_service_client.set_container_acl(
            container_name, public_access=PublicAccess.Container)

        # Create Sample folder if it not exists, and create a file in folder Sample to test the upload and download.
        local_path = os.path.expanduser("~/Sample")
        if not os.path.exists(local_path):
            os.makedirs(os.path.expanduser("~/Sample"))
        local_file_name = "QuickStart_" + str(uuid.uuid4()) + ".txt"
        full_path_to_file = os.path.join(local_path, local_file_name)

        # Write text to the file.
        file = open(full_path_to_file,  'w')
        file.write("Hello, World!")
        file.close()

        print("Temp file = " + full_path_to_file)
        print("\nUploading to Blob storage as blob" + local_file_name)

        # Upload the created file, use local_file_name for the blob name
        blob_service_client.create_blob_from_path(
            container_name, local_file_name, full_path_to_file)

        # List the blobs in the container
        print("\nList blobs in the container")
        generator = blob_service_client.list_blobs(container_name)
        for blob in generator:
            print("\t Blob name: " + blob.name)

        # Download the blob(s).
        # Add '_DOWNLOADED' as prefix to '.txt' so you can see both files in Documents.
        full_path_to_file2 = os.path.join(local_path, str.replace(
            local_file_name ,'.txt', '_DOWNLOADED.txt'))
        print("\nDownloading blob to " + full_path_to_file2)
        blob_service_client.get_blob_to_path(
            container_name, local_file_name, full_path_to_file2)

        sys.stdout.write("Sample finished running. When you hit <any key>, the sample will be deleted and the sample "
                         "application will exit.")
        sys.stdout.flush()
        input()

        # Clean up resources. This includes the container and the temp files
        blob_service_client.delete_container(container_name)
        os.remove(full_path_to_file)
        os.remove(full_path_to_file2)
    except Exception as e:
        print(e)


# Main method.
if __name__ == '__main__':
    run_sample()

import datetime 
import email 
import imaplib 
import os

from contextlib import suppress
from dotenv import load_dotenv

load_dotenv()

def connection_to_inbox(imap_url):
    email_user = os.environ["EMAIL"]
    email_password = os.environ["MOTDEPASSE"]

    connection = imaplib.IMAP4_SSL(imap_url)
    connection.login(email_user, email_password)

    connection.select("inbox") 
    _ , data = connection.fetch(b'12', '(RFC822)') 

    raw = email.message_from_bytes(data[0][1])
    return raw

def get_attachement(msg, current_date): 
    attachment_folder = os.environ["FOLDER"]   

    for part in msg.walk(): 
        if part.get_content_maintype == 'multipart': 
            continue
        if part.get('Content-Disposition') is None: 
            continue 
        filename = part.get_filename()
        with suppress(FileExistsError):
            os.mkdir(attachment_folder)
        if bool(filename): 
            filePath = os.path.join(attachment_folder, filename)
            with open(filePath, 'wb') as f: 
                f.write(part.get_payload(decode= True))

        old_file = os.path.join(attachment_folder, filename)
        new_file = os.path.join(attachment_folder, f"AZ_Cost_Report_{current_date}.xls")
        os.rename(old_file, new_file)

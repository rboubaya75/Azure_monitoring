#Une fonction qui récupère ma PJ 
#Un Cron qui lance ma fonction PJ automatiquement tt les jours 
#Quatre fichiers: get_email.py, cron.py, main.py, tests.py
#Commment uploader automatiquement ma PJ dans mon Storage ? 

import imaplib #install standard protocol 
import os
import email #use to read, write, send email 
import datetime #voir comment renomme le fichier 
from dotenv import load_dotenv #python3 -m pip install python-dotenv
load_dotenv()

email_user = os.environ["EMAIL"]
email_password = os.environ["MOTDEPASSE"]
imap_url = "imap.gmail.com"
attachment_folder = os.environ["FOLDER"]   #where we are going to store the attachment
Current_Date = datetime.datetime.today().strftime ('%d-%b-%Y')

connection = imaplib.IMAP4_SSL(imap_url)
connection.login(email_user, email_password)
#connection.list() #list of all my email (sent, inbox etc)

connection.select("inbox") #list the email in my inbox
result, data = connection.fetch(b'12', '(RFC822)') #je mets 12, le dernier email que je recois, des pages de 12 
#print(data)
raw = email.message_from_bytes(data[0][1])


################# Fonction optionnelle qui me permet de cherche dans mes mails par envoyeur 
def search(key, value, con): 
    result, data = con.search(None, key, "{}".format(value))
    return data

my_email = search('FROM', 'tiphaine.minguet@gmail.com', connection)


################# Fonction qui me permet de récupérer ma PJ 

def get_attachement(msg): 
    for part in msg.walk(): #walk me permet de parcourir mon message
        if part.get_content_maintype == 'multipart': #vérifie qu'il ya plusieurs partie dans mon email, donc PJ 
            continue
        if part.get('Content-Disposition') is None: 
            continue 
        filename = part.get_filename() #pour avoir le nom du fichier

        #print(type(filename)

        if bool(filename): #if BOOL == False no PJ 
            filePath = os.path.join(attachment_folder, filename)
            with open(filePath, 'wb') as f: #wb for write in bytes, not strings 
                f.write(part.get_payload(decode= True))

        old_file = os.path.join(attachment_folder, filename)
        new_file = os.path.join(attachment_folder, f"MainFile-{Current_Date}.xls")
        os.rename(old_file, new_file)

get_attachement(raw)
#Une fonction qui récupère ma PJ 
#Un Cron qui lance ma fonction PJ automatiquement tt les jours 
#Quatre fichiers: get_email.py, cron.py, main.py, tests.py
#Commment uploader automatiquement ma PJ dans mon Storage ? 

import imaplib #install standard protocol 
import base64 #to uncode ASCII character 
import os
import email #use to read, write, send email 
from dotenv import load_dotenv #python3 -m pip install python-dotenv
load_dotenv()

        
email_user = os.environ["EMAIL"]
email_password = os.environ["MOTDEPASSE"]

#print(email_user)
#print(email_password)

mail = imaplib.IMAP4_SSL(host="imap.gmail.com", port="993")
#print(mail)

mail.login(email_user, email_password)
mail.select('Inbox')  #('OK', [b'12']) j'ai bien 12 mails dans mon Inbox

type, data = mail.search(None, 'ALL') #type: OK, ma requête est bonne, et data me permet d'avoir les id de mes emails 
mail_ids = data[0] #data est une liste avec un 1 élément
id_list = mail_ids.split() #un objet binaire, pas considéré comme str 


for num in data[0].split():
    typ, data = mail.fetch(num, '(RFC822)' )
    raw_email = data[0][1]
# converts byte literal to string removing b''
    raw_email_string = raw_email.decode('utf-8')
    #print(raw_email_string)
    email_message = email.message_from_string(raw_email_string)
    #print(email_message)
# downloading attachments
    for part in email_message.walk():
        # this part comes from the snipped I don't understand yet... 
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue
        fileName = part.get_filename()
        #print(fileName)
        if bool(fileName):
            filePath = os.path.join('/Users/tiphaineminguet/Desktop/Simplon/Monitor/Azure_monitoring/PJ', fileName)
            if not os.path.isfile(filePath) :
                fp = open(filePath, 'wb')
                fp.write(part.get_payload(decode=True))
                fp.close()
            subject = str(email_message).split("Subject: ", 1)[1].split("\nTo:", 1)[0]
            #print('Downloaded "{file}" from email titled "{subject}" with UID {uid}.'.format(file=fileName, subject=subject, uid=latest_email_uid.decode('utf-8')))



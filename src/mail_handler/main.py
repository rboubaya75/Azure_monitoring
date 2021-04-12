import datetime
import os

from dotenv import load_dotenv 

from data_processing import DB, process_raw_data
from get_data_from_email import connection_to_inbox, get_attachement
from upload import upload_file

load_dotenv()

def main(): 
    imap_url = "imap.gmail.com"
    current_date = datetime.datetime.today().strftime ('%d-%b-%Y')
    new_file = os.path.join(os.environ["FOLDER"], f"AZ_Cost_Report_{current_date}.xls")

    raw = connection_to_inbox(imap_url)
    get_attachement(raw, current_date)
    upload_file(new_file)
    services, subs, cost = process_raw_data(new_file)
    with DB() as db:
            db.insert_subscriptions(subs)
            db.insert_services(services)
            db.insert_cost(cost)

if __name__ == "__main__": 
    main()

import pandas as pd
import os
import datetime 
import logging
from dotenv import load_dotenv
import psycopg2
from sqlalchemy import create_engine
import csv
from io import StringIO
from sqlalchemy import create_engine
load_dotenv()

# Load data file in dataframe and format cost values as numbers



attachment_folder = os.environ["FOLDER"]   
Current_Date = datetime.datetime.today().strftime ('%d-%b-%Y')

new_file = os.path.join(attachment_folder, f"data-{Current_Date}.xlsx")



def datafr():
        df=pd.read_excel(new_file )
        df['Cost'] = df['Cost'].apply(lambda x: float(x.replace(',', '.')))

        # Create table Service with ids
        Services=df["ServiceName"].drop_duplicates()
        Services=Services.to_frame()
        Services["id"]=list(range(1, Services.size + 1))
        print(Services)


        # Create table Subscription with ids
        Subscriptions=df["SubscriptionName"].drop_duplicates()
        Subscriptions=Subscriptions.to_frame()
        Subscriptions["id"]=list(range(1, Subscriptions.size + 1))
        print(Subscriptions)

        # Create Cost table
        Cost=df.groupby(['SubscriptionName', 'ServiceName']).sum().round(5).reset_index()
        print(Cost)


        # Replace ServiceName and SubscriptionName with id from Services and Subscriptions tables
        Cost = Cost.replace(Services.set_index('ServiceName')['id'])
        Cost = Cost.replace(Subscriptions.set_index('SubscriptionName')['id'])
        print(Cost.to_string())


        return Subscriptions,Services, Cost

datafr()
"""
def psql_insert_copy(table, conn, keys, data_iter):
    # gets a DBAPI connection that can provide a cursor
    dbapi_conn = conn.connection
    with dbapi_conn.cursor() as cur:
        s_buf = StringIO()
        writer = csv.writer(s_buf)
        writer.writerows(data_iter)
        s_buf.seek(0)

        columns = ', '.join('"{}"'.format(k) for k in keys)
        if table.schema:
            table_name = '{}.{}'.format(table.schema, table.name)
        else:
            table_name = table.name

        sql = 'COPY {} ({}) FROM STDIN WITH CSV'.format(
            table_name, columns)
        cur.copy_expert(sql=sql, file=s_buf)


#driver://username:password@server/database

host=os.environ['PG_HOST']
user=os.environ['PG_USER']
password=os.environ['PG_PASSWORD']
database=os.environ['PG_DATABASE']



engine = create_engine(f'''postgresql+psycopg2://{user}:{password}@{host}/{database}''')

Cost.to_sql('Mycosts', engine, if_exists='replace',index=False, method=psql_insert_copy)

ServiceName.to_sql('Myservices', engine, if_exists='replace',index=False, method=psql_insert_copy)

Subscription.to_sql('Mysubscription', engine, if_exists='replace',index=False, method=psql_insert_copy)

"""
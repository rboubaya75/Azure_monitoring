import datetime
import os
import pandas as pd
import psycopg2
import sys
import time

class DB:
    def __init__(self):
        self._dbcon = None

    def __enter__(self):
        try:
            self._dbcon = psycopg2.connect(
                host=os.environ['POSTGRES_HOST'],
                user=os.environ['POSTGRES_USER'],
                password=os.environ['POSTGRES_PASSWORD'],
                database=os.environ['POSTGRES_DB']
            )
            self._cursor = self._dbcon.cursor()
            return self
        except:
            raise
    
    def __exit__(self, exc_type, exc_val, traceback):
        self._dbcon.close()

    def insert_subscriptions(self, subscriptions):
        subs = tuple(subscriptions['SubscriptionName'].values.tolist())
        try:
            for sub in subs:
                self._cursor.execute("INSERT INTO Subscriptions (Name) VALUES (%s)", [sub])
            self._dbcon.commit()
        except psycopg2.errors.UniqueViolation:
            self._dbcon.rollback()

    def insert_services(self, services):
        ser = tuple(services['ServiceName'].values.tolist())
        try:
            for s in ser:
                self._cursor.execute("INSERT INTO Services (Name) VALUES (%s)", [s])
            self._dbcon.commit()
        except psycopg2.errors.UniqueViolation:
            self._dbcon.rollback()

    def insert_cost(self, cost):
        cst = tuple(cost.values.tolist())
        try:
            for c in cst:
                self._cursor.execute("INSERT INTO Cost (Subid, Serviceid, Cost) VALUES (%s, %s, %s)", c)
            self._dbcon.commit()
        except psycopg2.errors.UniqueViolation:
            self._dbcon.rollback()

def process_raw_data(filename):
    df = pd.read_excel(filename)
    df['Cost'] = df['Cost'].apply(lambda x: float(x.replace(',', '.')))

    services = df["ServiceName"].drop_duplicates()
    services = services.to_frame()
    services["id"] = list(range(1, services.size + 1))

    subscriptions = df["SubscriptionName"].drop_duplicates()
    subscriptions = subscriptions.to_frame()
    subscriptions["id"] = list(range(1, subscriptions.size + 1))

    # AJOUTER COLONNE DATE à la table Cost
    cost = df.groupby(['SubscriptionName', 'ServiceName']).sum().round(5).reset_index()
    cost = cost.replace(services.set_index('ServiceName')['id'])
    cost = cost.replace(subscriptions.set_index('SubscriptionName')['id'])
    date = datetime.datetime.today().strftime ('%d-%m-%Y')
    return services, subscriptions, cost
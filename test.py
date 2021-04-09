import pandas as pd 
import numpy as np

df=pd.read_excel("data.xlsx")


df.info()

print(df["Cost"].unique())


df['Cost'] = df['Cost'].apply(lambda x: float(x.replace(',', '.')))
print(df["Cost"].sum())



SubName=df.groupby(['SubscriptionName']).sum().reset_index()

print(SubName)


#cost by ServiceName
ServiceName=df.loc[:, ["ServiceName","Cost"]].groupby(by=df.ServiceName).agg(sum).reset_index()
print(ServiceName)

ServiceName2=df.groupby(['ServiceName']).sum().reset_index()
print(ServiceName2)


#concat




import pandas as pd 
import numpy as np

df=pd.read_excel("data.xlsx")

print('Le dataframe a la tête suivante :',df.head(5))

df['Cost'] = df['Cost'].apply(lambda x: float(x.replace(',', '.')))
print("la somme totale dépensée par Simplon Co pour les service Cloud Azure est de :", df["Cost"].sum().round(2))



SubName=df.groupby(['SubscriptionName']).sum().round(2).reset_index()

print ("Le cout par entité Simplon: \n", SubName)


#cost by ServiceName
ServiceName=df.loc[:, ["ServiceName","Cost"]].groupby(by=df.ServiceName).agg(sum).reset_index()


ServiceName2=df.groupby(['ServiceName']).sum().round(2).reset_index()


print ("Le cout par entité Service Cloud Azure: \n", ServiceName2)

#concat




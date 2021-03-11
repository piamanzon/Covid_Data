'''
Created on Feb 9, 2021

@author: pia.manzon

'''
import numpy as np
import pandas as pd
import wget
from datetime import date, timedelta, datetime, time
import os
import Database

def Main():
   
    db = Database.Database()
    df = pd.read_csv(os.path.join(r'C:\Users\pia.manzon\Documents',"World.csv"))
    df.Date = pd.to_datetime(df.Date)

    #===========================================================================
    # if(dateYesterday == (startDate + timedelta(1))):
    #     df.insert(2, 'date', dateYesterday)
    #===========================================================================
   # os.remove(os.path.join(r'C:\Users\pia.manzon\Documents',"world_data.csv"))
    
    print(df.info())
   # print(df["date"])
    
  #  df = df[df['continent'].notna()] #Uncomment to not include world and continent data
 
  
#===============================================================================
#     if(dateYesterday == (startDate + timedelta(1)) and (dateYesterday in df.values)):
#         print("one date") 
#         worldData_url ='https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/latest/owid-covid-latest.csv'
#         db.updateDatabase(df)
#     elif(dateYesterday in df.values):
#         print("multiple dates")
#         worldData_url = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv'
# 
#         mask = (df['date'] > startDate) & (df['date'] <= dateYesterday)
#         finalDF = df.loc[mask]
#         db.updateDatabase(finalDF)
#     else:
#         print("No update yet")
#===============================================================================
    df.to_csv("World_Data.csv")
    db.updateDatabase(df)



Main()
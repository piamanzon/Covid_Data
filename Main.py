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
    startDate = db.getLatestDate()
    dateYesterday = date.today() - timedelta(1)
    print(startDate)
    fileName = ""
    columnList = []
    
    #===========================================================================
    # if(dateYesterday == (startDate + timedelta(1))):
    #     worldData_url ='https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/latest/owid-covid-latest.csv'
    #     fileName = "owid-covid-latest.csv"
    #     columnList = ["continent", "location", "total_cases", "new_cases", "total_deaths","total_vaccinations"]
    #     print("hey")
    # else:
    #     worldData_url = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv'
    #     fileName = "owid-covid-data.csv"
    #     columnList = ["continent", "location", "date", "total_cases", "new_cases", "total_deaths","total_vaccinations"]
    #===========================================================================
    
    worldData_url = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv'
    fileName = "owid-covid-data.csv"
    columnList = ["continent", "location", "date", "total_cases", "new_cases", "total_deaths","total_vaccinations"]
                

    wget.download(worldData_url, r'C:\Users\pia.manzon\Documents\temp')
   
    df = pd.read_csv(os.path.join(r'C:\Users\pia.manzon\Documents\temp',fileName), usecols=columnList)
    df.date = pd.to_datetime(df.date)

    #===========================================================================
    # if(dateYesterday == (startDate + timedelta(1))):
    #     df.insert(2, 'date', dateYesterday)
    #===========================================================================
    os.remove(os.path.join(r'C:\Users\pia.manzon\Documents\temp',fileName))
    
    print(df.info())
    print(df["date"])
    
  #  df = df[df['continent'].notna()] #Uncomment to not include world and continent data
    print(df.info())
    print(df.head(10))
    
    df.columns= ["Continent","Country", "Date", "Total_Cases", "New_Cases", "Total_Deaths", "Total_Vaccinations"]
    df=df[["Date", "Continent", "Country", "Total_Cases", "New_Cases", "Total_Deaths", "Total_Vaccinations"]]
    df['Total_Cases'][df['Total_Cases'] < 0] = 0
    df['New_Cases'][df['New_Cases'] < 0] = 0
    df['Total_Deaths'][df['Total_Deaths'] < 0] = 0
    df['Total_Vaccinations'][df['Total_Vaccinations'] < 0] = 0
    print(df.info())
  
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
    myTime = time(0, 0, 0)
    dateYesterday_DT = datetime.combine(dateYesterday, myTime)
    
    if(dateYesterday_DT in df.values):
        print("multiple dates")
        worldData_url = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv'
        startDate_DT = datetime.combine(startDate, myTime)
        print(startDate_DT)
        mask = (df['Date'] > startDate_DT) & (df['Date'] <= dateYesterday_DT)
        df = df.loc[mask]
        print(df.info())
        #df.to_csv("Daily.csv")
        db.updateDatabase(df)
    else:
        print("No update yet")



Main()
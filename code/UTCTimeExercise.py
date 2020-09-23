#!/usr/bin/env python

from calendar import monthrange

def findfirstdatetime(inputdate):
  yearmonthdatetime =inputdate.split('T') 

  try:
    minyear = yearmonthdatetime[0].split('-')[0]
    maxyear=minyear
  except IndexError:
    minyear='0000'
    
  try:
    minmonth = yearmonthdatetime[0].split('-')[1]
    maxmonth=minmonth
  except IndexError:
    minmonth='01'
    maxmonth='12'
  
  try:
    minday = yearmonthdatetime[0].split('-')[2]
    maxday=str(monthrange(int(minyear), int(maxmonth))[1])
  except IndexError:
    minday='01'
    maxday= str(monthrange(int(minyear), int(maxmonth))[1])
  
  try:
    minhour = yearmonthdatetime[1].split(':')[0]
    maxhour='23'
  except IndexError:
    minhour='00'
    maxhour='23'

  try:
    minminn = yearmonthdatetime[1].split(':')[1]
    maxminn='59'
  except IndexError:
    minminn='00'
    maxminn='59'

  try:
    minsec = yearmonthdatetime[1].split(':')[2]
    minsec= minsec.split('.')[0]
    maxsec='59'
  except IndexError:
    minsec='00'
    maxsec='59'
  try:
    minzn = yearmonthdatetime[1].split('.')[1]    
    maxzn='9'*(len(minzn)-1)+'Z'
  except IndexError:
    minzn='000Z'
    minzn='0'*(len(minzn)-1)+'Z'
    maxzn='9'*(len(minzn)-1)+'Z'

  firstdate=minyear+'-'+minmonth+'-'+minday+'T'+minhour+':'+minminn+':'+minsec+'.'+minzn
  maxdate=maxyear+'-'+maxmonth+'-'+maxday+'T'+maxhour+':'+maxminn+':'+maxsec+'.'+maxzn
  try:
    dateutil.parser.parse(firstdate)
    return firstdate,maxdate
  except:
    print("input date is not in correct format")
    return None,None
    
  
  

if __name__ == '__main__':

  import time
  import dateutil.parser

 
  date_string = "2018-01-02T22:08:12.510696"  
  firstdate,maxdate=findfirstdatetime(date_string)
  if firstdate:
    print(f'Date range from : Start Date : {firstdate} ,  End Date : {maxdate} ')

  



 
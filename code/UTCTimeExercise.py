#!/usr/bin/env python

from calendar import monthrange

#function for finding the first and last timestamp
def findfirstdatetime(inputdate):
  yearmonthdatetime =inputdate.split('T') #parsing the input string into data and timestamp section

  try:
    minyear = yearmonthdatetime[0].split('-')[0] # Parsing the year from input and assign min and max value
    maxyear=minyear
  except IndexError:
    minyear='0000'
    
  try:
    minmonth = yearmonthdatetime[0].split('-')[1] # Parsing the Month from input and assign min and max value
    maxmonth=minmonth
  except IndexError:
    minmonth='01'
    maxmonth='12'
  
  try:
    minday = yearmonthdatetime[0].split('-')[2] # Parsing the Day from input and assign min and max value
    maxday=str(monthrange(int(minyear), int(maxmonth))[1])
  except IndexError:
    minday='01'
    maxday= str(monthrange(int(minyear), int(maxmonth))[1])
  
  try:
    minhour = yearmonthdatetime[1].split(':')[0]    # Parsing the hour from input and assign min and max value
    maxhour='23'
  except IndexError:
    minhour='00'
    maxhour='23'

  try:
    minminn = yearmonthdatetime[1].split(':')[1] # Parsing the minutes from input and assign min and max value
    maxminn='59'
  except IndexError:
    minminn='00'
    maxminn='59'

  try:
    minsec = yearmonthdatetime[1].split(':')[2] # Parsing the Second from input and assign min and max value
    minsec= minsec.split('.')[0]
    maxsec='59'
  except IndexError:
    minsec='00'
    maxsec='59'
  try:
    minzn = yearmonthdatetime[1].split('.')[1]  # Parsing the milsec from input and assign min and max value
    maxzn='9'*(len(minzn)-1)+'Z'
  except IndexError:
    minzn='000Z'
    minzn='0'*(len(minzn)-1)+'Z'
    maxzn='9'*(len(minzn)-1)+'Z'

  firstdate=minyear+'-'+minmonth+'-'+minday+'T'+minhour+':'+minminn+':'+minsec+'.'+minzn # forming the complete first date
  maxdate=maxyear+'-'+maxmonth+'-'+maxday+'T'+maxhour+':'+maxminn+':'+maxsec+'.'+maxzn # forming the maxdate
  try:                             # Checking the passed input is in right format
    dateutil.parser.parse(firstdate)
    return firstdate,maxdate
  except:
    print("input date is not in correct format")
    return None,None
    
  
  

if __name__ == '__main__':

  import time
  import dateutil.parser

 
  date_string = "2018-04-01T22:08:12.100Z"  # passing the inputdate  value 
  firstdate,maxdate=findfirstdatetime(date_string)
  if firstdate:
    print(f'Date range from : Start Date : {firstdate} ,  End Date : {maxdate} ')

  



 

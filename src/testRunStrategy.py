#import os
import datetime
import pandas as pd
import service.strategy as s


# get data
data = pd.read_csv('resources/historical_data/AAPL_90_days_ended_on_2019-12-13.csv')
data.rename( columns={'Unnamed: 0':'time'}, inplace=True )

# load data into simple strategy
s = s.simple(data)

startTime = datetime.datetime(2019, 6, 20, 9, 40)
fund = 10000
position = 0


currentTime = startTime
currentPrice = data['average'][data.time == str(currentTime)].tolist()[0]

for i in range(300):
#    print(currentTime, end='\t')
    
    action = s.result(5, currentPrice, currentTime)
#    print(action, end='\t')
    
    if action == 'hold':
        pass
    elif action =='buy':
        if fund > currentPrice:
            fund -= currentPrice
            position += 1
    elif action == 'sell':
        if position > 0:
            fund += currentPrice
            position -+ 1
            
#    print(position)
    
    currentTime += datetime.timedelta(minutes=1)
    currentPrice = data['average'][data.time == str(currentTime)].tolist()[0]
    
print(fund + currentPrice * position)
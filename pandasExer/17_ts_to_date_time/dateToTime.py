#Pandas Time Series Analysis Tutorial: to_datetime
import pandas as pd
dates = ['2017-01-05', 'Jan 5, 2017', '01/05/2017', '2017.01.05', '2017/01/05','20170105']
pd.to_datetime(dates)
'''
DatetimeIndex(['2017-01-05', '2017-01-05', '2017-01-05', '2017-01-05',
               '2017-01-05', '2017-01-05'],
              dtype='datetime64[ns]', freq=None)
'''
dt = ['2017-01-05 2:30:00 PM', 'Jan 5, 2017 14:30:00', '01/05/2016', '2017.01.05', '2017/01/05','20170105']
pd.to_datetime(dt)
'''
DatetimeIndex(['2017-01-05 14:30:00', '2017-01-05 14:30:00',
               '2016-01-05 00:00:00', '2017-01-05 00:00:00',
               '2017-01-05 00:00:00', '2017-01-05 00:00:00'],
              dtype='datetime64[ns]', freq=None
'''
#European style dates with day first
pd.to_datetime('30-12-2016')
#Timestamp('2016-12-30 00:00:00')
pd.to_datetime('5-1-2016', dayfirst=True)
#Timestamp('2016-01-05 00:00:00')
#Custom date time format
pd.to_datetime('2017$01$05', format='%Y$%m$%d')
#Timestamp('2017-01-05 00:00:00')
pd.to_datetime('2017#01#05', format='%Y#%m#%d')
#Timestamp('2017-01-05 00:00:00')
#Handling invalid dates
pd.to_datetime(['2017-01-05', 'Jan 6, 2017', 'abc'], errors='ignore')
#array(['2017-01-05', 'Jan 6, 2017', 'abc'], dtype=object)
pd.to_datetime(['2017-01-05', 'Jan 6, 2017', 'abc'], errors='coerce')
#DatetimeIndex(['2017-01-05', '2017-01-06', 'NaT'], dtype='datetime64[ns]', freq=None)
#Epoch
#Epoch or Unix time means number of seconds that have passed since Jan 1, 1970 00:00:00 UTC time

current_epoch = 1501324478
pd.to_datetime(current_epoch, unit='s')
#Timestamp('2017-07-29 10:34:38')
pd.to_datetime(current_epoch*1000, unit='ms')
#Timestamp('2017-07-29 10:34:38')
t = pd.to_datetime([current_epoch], unit='s')
t
#DatetimeIndex(['2017-07-29 10:34:38'], dtype='datetime64[ns]', freq=None)
t.view('int64')
#array([1501324478000000000], dtype=int64)
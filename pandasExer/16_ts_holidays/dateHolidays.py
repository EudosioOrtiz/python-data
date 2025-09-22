#Pandas Time Series Analysis Tutorial: Handling Holidays
import pandas as pd
df = pd.read_csv("aapl_no_dates.csv")
df.head()
'''
Open	High	Low	Close	Volume
0	144.88	145.30	143.10	143.50	14277848
1	143.69	144.79	142.72	144.09	21569557
2	143.02	143.50	142.41	142.73	24128782
3	142.90	144.75	142.90	144.18	19201712
4	144.11	145.95	143.37	145.06	21090636
'''
rng = pd.date_range(start="7/1/2017", end="7/21/2017", freq='B')
rng
'''
DatetimeIndex(['2017-07-03', '2017-07-04', '2017-07-05', '2017-07-06',
               '2017-07-07', '2017-07-10', '2017-07-11', '2017-07-12',
               '2017-07-13', '2017-07-14', '2017-07-17', '2017-07-18',
               '2017-07-19', '2017-07-20', '2017-07-21'],
              dtype='datetime64[ns]', freq='B')
Using 'B' frequency is not going to help because 4th July was holiday and 'B' is not taking that into account. It only accounts for weekends
'''
#Using CustomBusinessDay to generate US holidays calendar frequency
from pandas.tseries.holiday import USFederalHolidayCalendar
from pandas.tseries.offsets import CustomBusinessDay

us_cal = CustomBusinessDay(calendar=USFederalHolidayCalendar()) # you can customize the businessdays to exclude the holidays

rng = pd.date_range(start="7/1/2017",end="7/23/2017", freq=us_cal)
rng
'''
DatetimeIndex(['2017-07-03', '2017-07-05', '2017-07-06', '2017-07-07',
               '2017-07-10', '2017-07-11', '2017-07-12', '2017-07-13',
               '2017-07-14', '2017-07-17', '2017-07-18', '2017-07-19',
               '2017-07-20', '2017-07-21'],
              dtype='datetime64[ns]', freq='C')
'''
df.set_index(rng,inplace=True)
df.head()
'''
Open	High	Low	Close	Volume
2017-07-03	144.88	145.30	143.10	143.50	14277848
2017-07-05	143.69	144.79	142.72	144.09	21569557
2017-07-06	143.02	143.50	142.41	142.73	24128782
2017-07-07	142.90	144.75	142.90	144.18	19201712
2017-07-10	144.11	145.95	143.37	145.06	21090636
You can define your own calendar using AbstractHolidayCalendar as shown below. USFederalHolidayCalendar is the only calendar available in pandas library and it serves as an example for those who want to write their own custom calendars. Here is the link for USFederalHolidayCalendar implementation https://github.com/pandas-dev/pandas/blob/master/pandas/tseries/holiday.py
'''
#AbstractHolidayCalendar
from pandas.tseries.holiday import AbstractHolidayCalendar, nearest_workday, Holiday
class myCalendar(AbstractHolidayCalendar): # you can create your own holidays to do exceptions on your indexes
    rules = [
        Holiday('My Birth Day', month=4, day=15),#, observance=nearest_workday), #you can use observance to make the exception with others days, in the documentation tell what are those options
    ]
    
my_bday = CustomBusinessDay(calendar=myCalendar())
pd.date_range('4/1/2017','4/30/2017',freq=my_bday)
'''
DatetimeIndex(['2017-04-03', '2017-04-04', '2017-04-05', '2017-04-06',
               '2017-04-07', '2017-04-10', '2017-04-11', '2017-04-12',
               '2017-04-13', '2017-04-14', '2017-04-17', '2017-04-18',
               '2017-04-19', '2017-04-20', '2017-04-21', '2017-04-24',
               '2017-04-25', '2017-04-26', '2017-04-27', '2017-04-28'],
              dtype='datetime64[ns]', freq='C')

CustomBusinessDay
Weekend in egypt is Friday and Saturday. Sunday is just a normal weekday and you can handle this custom week schedule using CystomBysinessDay with weekmask as shown below
'''
egypt_weekdays = "Sun Mon Tue Wed Thu" #you can custome the business days to be contemplated in the dateindex

b = CustomBusinessDay(weekmask=egypt_weekdays)

pd.date_range(start="7/1/2017",periods=20,freq=b)
'''
DatetimeIndex(['2017-07-02', '2017-07-03', '2017-07-04', '2017-07-05',
               '2017-07-06', '2017-07-09', '2017-07-10', '2017-07-11',
               '2017-07-12', '2017-07-13', '2017-07-16', '2017-07-17',
               '2017-07-18', '2017-07-19', '2017-07-20', '2017-07-23',
               '2017-07-24', '2017-07-25', '2017-07-26', '2017-07-27'],
              dtype='datetime64[ns]', freq='C')
You can also add holidays to this custom business day frequency
'''
b = CustomBusinessDay(holidays=['2017-07-04', '2017-07-10'], weekmask=egypt_weekdays) # you can use your customized business days to add the holidays that yo want and make exceptions on your index

pd.date_range(start="7/1/2017",periods=20,freq=b)
'''
DatetimeIndex(['2017-07-02', '2017-07-03', '2017-07-05', '2017-07-06',
               '2017-07-09', '2017-07-11', '2017-07-12', '2017-07-13',
               '2017-07-16', '2017-07-17', '2017-07-18', '2017-07-19',
               '2017-07-20', '2017-07-23', '2017-07-24', '2017-07-25',
               '2017-07-26', '2017-07-27', '2017-07-30', '2017-07-31'],
              dtype='datetime64[ns]', freq='C')
Mathematical operations on date object using custom business day
'''
from datetime import datetime
dt = datetime(2017,7,9)
dt
datetime.datetime(2017, 7, 9, 0, 0)
dt + 1*b
#Timestamp('2017-07-11 00:00:00')
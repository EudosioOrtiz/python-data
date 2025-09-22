#Pandas Time Series Analysis: Period and PeriodIndex
#Yearly Period
import pandas as pd
y = pd.Period('2016')
y
#Period('2016', 'A-DEC')
y.start_time
#Timestamp('2016-01-01 00:00:00')
y.end_time
#Timestamp('2016-12-31 23:59:59.999999999')
y.is_leap_year
True
#Monthly Period
m = pd.Period('2017-12')
m
#Period('2017-12', 'M')
m.start_time
#Timestamp('2017-12-01 00:00:00')
m.end_time
#Timestamp('2017-12-31 23:59:59.999999999')
m+1
#Period('2018-01', 'M')
#Daily Period
d = pd.Period('2016-02-28', freq='D')
d
#Period('2016-02-28', 'D')
d.start_time
#Timestamp('2016-02-28 00:00:00')
d.end_time
#Timestamp('2016-02-28 23:59:59.999999999')
d+1
#Period('2016-02-29', 'D')
#Hourly Period
h = pd.Period('2017-08-15 23:00:00',freq='H')
h
#Period('2017-08-15 23:00', 'H')
h+1
#Period('2017-08-16 00:00', 'H')
#Achieve same results using pandas offsets hour
h+pd.offsets.Hour(1)
#Period('2017-08-16 00:00', 'H')
#Quarterly Period
q1= pd.Period('2017Q1', freq='Q-JAN') # the freq here indicates de termination of the period
q1
#Period('2017Q1', 'Q-JAN')
q1.start_time
#Timestamp('2016-02-01 00:00:00')
q1.end_time
#Timestamp('2016-04-30 23:59:59.999999999')
#Use asfreq to convert period to a different frequency
q1.asfreq('M',how='start')
#Period('2016-02', 'M')
q1.asfreq('M',how='end')
#Period('2016-04', 'M')
#Weekly Period
w = pd.Period('2017-07-05',freq='W')
w
#Period('2017-07-03/2017-07-09', 'W-SUN')
w-1
#Period('2017-06-26/2017-07-02', 'W-SUN')
w2 = pd.Period('2017-08-15',freq='W')
w2
#Period('2017-08-14/2017-08-20', 'W-SUN')
w2-w
#6
#PeriodIndex and period_range
r = pd.period_range('2011', '2017', freq='q')
r
'''
PeriodIndex(['2011Q1', '2011Q2', '2011Q3', '2011Q4', '2012Q1', '2012Q2',
             '2012Q3', '2012Q4', '2013Q1', '2013Q2', '2013Q3', '2013Q4',
             '2014Q1', '2014Q2', '2014Q3', '2014Q4', '2015Q1', '2015Q2',
             '2015Q3', '2015Q4', '2016Q1', '2016Q2', '2016Q3', '2016Q4',
             '2017Q1'],
            dtype='period[Q-DEC]', freq='Q-DEC')
'''
r[0].start_time
#Timestamp('2011-01-01 00:00:00')
r[0].end_time
#Timestamp('2011-03-31 23:59:59.999999999')
#Walmart's fiscal year ends in Jan, below is how you generate walmart's fiscal quarters between 2011 and 2017

r = pd.period_range('2011', '2017', freq='q-jan')
r
'''
PeriodIndex(['2011Q4', '2012Q1', '2012Q2', '2012Q3', '2012Q4', '2013Q1',
             '2013Q2', '2013Q3', '2013Q4', '2014Q1', '2014Q2', '2014Q3',
             '2014Q4', '2015Q1', '2015Q2', '2015Q3', '2015Q4', '2016Q1',
             '2016Q2', '2016Q3', '2016Q4', '2017Q1', '2017Q2', '2017Q3',
             '2017Q4'],
            dtype='period[Q-JAN]', freq='Q-JAN')
'''
r[0].start_time
#Timestamp('2010-11-01 00:00:00')
r[0].end_time
#Timestamp('2011-01-31 23:59:59.999999999')
r = pd.PeriodIndex(start='2016-01', freq='3M', periods=10)
r
'''
PeriodIndex(['2016-01', '2016-04', '2016-07', '2016-10', '2017-01', '2017-04',
             '2017-07', '2017-10', '2018-01', '2018-04'],
            dtype='period[3M]', freq='3M')
'''
import numpy as np
ps = pd.Series(np.random.randn(len(idx)), idx)
ps
'''
2016-01   -0.895267
2016-04    1.343498
2016-07   -0.979625
2016-10   -0.292720
2017-01    0.275139
2017-04    1.200450
2017-07    1.890607
2017-10    0.259646
2018-01   -1.113016
2018-04    1.669858
Freq: 3M, dtype: float64
'''
#Partial Indexing
ps['2016']
'''
2016-01   -0.895267
2016-04    1.343498
2016-07   -0.979625
2016-10   -0.292720
2017-01    0.275139
Freq: 3M, dtype: float64
'''
ps['2016':'2017']
'''
2016-01   -0.895267
2016-04    1.343498
2016-07   -0.979625
2016-10   -0.292720
2017-01    0.275139
2017-04    1.200450
2017-07    1.890607
2017-10    0.259646
Freq: 3M, dtype: float64
'''
#Converting between representations
pst = ps.to_timestamp()
pst
'''
2016-01-01   -0.895267
2016-04-01    1.343498
2016-07-01   -0.979625
2016-10-01   -0.292720
2017-01-01    0.275139
2017-04-01    1.200450
2017-07-01    1.890607
2017-10-01    0.259646
2018-01-01   -1.113016
2018-04-01    1.669858
Freq: QS-OCT, dtype: float64
'''
pst.index
'''
DatetimeIndex(['2016-01-01', '2016-04-01', '2016-07-01', '2016-10-01',
               '2017-01-01', '2017-04-01', '2017-07-01', '2017-10-01',
               '2018-01-01', '2018-04-01'],
              dtype='datetime64[ns]', freq='QS-OCT')
'''
ps = pst.to_period()
ps
'''
2016Q1   -0.895267
2016Q2    1.343498
2016Q3   -0.979625
2016Q4   -0.292720
2017Q1    0.275139
2017Q2    1.200450
2017Q3    1.890607
2017Q4    0.259646
2018Q1   -1.113016
2018Q2    1.669858
Freq: Q-DEC, dtype: float64
'''
ps.index
'''
PeriodIndex(['2016Q1', '2016Q2', '2016Q3', '2016Q4', '2017Q1', '2017Q2',
             '2017Q3', '2017Q4', '2018Q1', '2018Q2'],
            dtype='period[Q-DEC]', freq='Q-DEC')
Processing Wal Mart's Financials
'''
import pandas as pd
df = pd.read_csv("wmt.csv")
df
'''
Line Item	2017Q1	2017Q2	2017Q3	2017Q4	2018Q1
0	Revenue	115904	120854	118179	130936	117542
1	Expenses	86544	89485	87484	97743	87688
2	Profit	29360	31369	30695	33193	29854
'''
df.set_index("Line Item",inplace=True)
df = df.T
df
'''
Line Item	Revenue	Expenses	Profit
2017Q1	115904	86544	29360
2017Q2	120854	89485	31369
2017Q3	118179	87484	30695
2017Q4	130936	97743	33193
2018Q1	117542	87688	29854
'''
df.index = pd.PeriodIndex(df.index, freq="Q-JAN")
df
'''
Line Item	Revenue	Expenses	Profit
2017Q1	115904	86544	29360
2017Q2	120854	89485	31369
2017Q3	118179	87484	30695
2017Q4	130936	97743	33193
2018Q1	117542	87688	29854
'''
df.index
#PeriodIndex(['2017Q1', '2017Q2', '2017Q3', '2017Q4', '2018Q1'], dtype='period[Q-JAN]', freq='Q-JAN')
df.index[0].start_time
#Timestamp('2016-02-01 00:00:00')
#Add start date end date columns to dataframe
df["Start Date"]=df.index.map(lambda x: x.start_time)
df
'''
Line Item	Revenue	Expenses	Profit	Start Date
2017Q1	115904	86544	29360	2016-02-01
2017Q2	120854	89485	31369	2016-05-01
2017Q3	118179	87484	30695	2016-08-01
2017Q4	130936	97743	33193	2016-11-01
2018Q1	117542	87688	29854	2017-02-01
'''
df["End Date"]=df.index.map(lambda x: x.end_time)
df
'''
Line Item	Revenue	Expenses	Profit	Start Date	End Date
2017Q1	115904	86544	29360	2016-02-01	2016-04-30
2017Q2	120854	89485	31369	2016-05-01	2016-07-31
2017Q3	118179	87484	30695	2016-08-01	2016-10-31
2017Q4	130936	97743	33193	2016-11-01	2017-01-31
2018Q1	117542	87688	29854	2017-02-01	2017-04-30
'''
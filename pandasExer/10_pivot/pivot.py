Pivot basics
import pandas as pd
import numpy as np
df = pd.read_csv("weather.csv")
df
'''
date	city	temperature	humidity
0	5/1/2017	new york	65	56
1	5/2/2017	new york	66	58
2	5/3/2017	new york	68	60
3	5/1/2017	mumbai	75	80
4	5/2/2017	mumbai	78	83
5	5/3/2017	mumbai	82	85
6	5/1/2017	beijing	80	26
7	5/2/2017	beijing	77	30
8	5/3/2017	beijing	79	35
'''
df.pivot(index='city',columns='date') # you can use the column that you want to use it as the index and transform your data
#also pivot table is used to summarize and aggregate data inside dataframe
'''
temperature	humidity
date	5/1/2017	5/2/2017	5/3/2017	5/1/2017	5/2/2017	5/3/2017
city						
beijing	80	77	79	26	30	35
mumbai	75	78	82	80	83	85
new york	65	66	68	56	58	60
'''
df.pivot(index='city',columns='date',values="humidity")
'''
date	5/1/2017	5/2/2017	5/3/2017
city			
beijing	26	30	35
mumbai	80	83	85
new york	56	58	60
'''
df.pivot(index='date',columns='city')
'''
temperature	humidity
city	beijing	mumbai	new york	beijing	mumbai	new york
date						
5/1/2017	80	75	65	26	80	56
5/2/2017	77	78	66	30	83	58
5/3/2017	79	82	68	35	85	60
'''
df.pivot(index='humidity',columns='city')
'''
date	temperature
city	beijing	mumbai	new york	beijing	mumbai	new york
humidity						
26	5/1/2017	None	None	80.0	NaN	NaN
30	5/2/2017	None	None	77.0	NaN	NaN
35	5/3/2017	None	None	79.0	NaN	NaN
56	None	None	5/1/2017	NaN	NaN	65.0
58	None	None	5/2/2017	NaN	NaN	66.0
60	None	None	5/3/2017	NaN	NaN	68.0
80	None	5/1/2017	None	NaN	75.0	NaN
83	None	5/2/2017	None	NaN	78.0	NaN
85	None	5/3/2017	None	NaN	82.0	NaN

Pivot Table
'''
df = pd.read_csv("weather2.csv")
df
'''
date	city	temperature	humidity
0	5/1/2017	new york	65	56
1	5/1/2017	new york	61	54
2	5/2/2017	new york	70	60
3	5/2/2017	new york	72	62
4	5/1/2017	mumbai	75	80
5	5/1/2017	mumbai	78	83
6	5/2/2017	mumbai	82	85
7	5/2/2017	mumbai	80	26
'''
df.pivot_table(index="city",columns="date")
'''
humidity	temperature
date	5/1/2017	5/2/2017	5/1/2017	5/2/2017
city				
mumbai	81.5	55.5	76.5	81.0
new york	55.0	61.0	63.0	71.0
Margins
'''
df.pivot_table(index="city",columns="date", margins=True,aggfunc=np.sum) #you can use a function to aggragate important values or results
'''
humidity	temperature
date	5/1/2017	5/2/2017	5/3/2017	All	5/1/2017	5/2/2017	5/3/2017	All
city								
beijing	26.0	30.0	35.0	91.0	80.0	77.0	79.0	236.0
mumbai	80.0	83.0	85.0	248.0	75.0	78.0	82.0	235.0
new york	110.0	122.0	60.0	292.0	126.0	142.0	68.0	336.0
All	216.0	235.0	180.0	631.0	281.0	297.0	229.0	807.0
Grouper
'''
df = pd.read_csv("weather3.csv")
df
'''
date	city	temperature	humidity
0	5/1/2017	new york	65	56
1	5/2/2017	new york	61	54
2	5/3/2017	new york	70	60
3	12/1/2017	new york	30	50
4	12/2/2017	new york	28	52
5	12/3/2017	new york	25	51
'''
df['date'] = pd.to_datetime(df['date'])
df.pivot_table(index=pd.Grouper(freq='M',key='date'),columns='city') # with pd grouper you can make frecuencies using the time in this case is M for month and use the city as the columns, in this case gives you 
# a mean as the values
'''
humidity	temperature
city	new york	new york
date		
2017-05-31	56.666667	65.333333
2017-12-31	51.000000	27.666667
'''
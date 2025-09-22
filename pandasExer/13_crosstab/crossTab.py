#Crosstab Tutorial
import pandas as pd
df = pd.read_excel("survey.xls")
df
'''
Name	Nationality	Sex	Age	Handedness
0	Kathy	USA	Female	23	Right
1	Linda	USA	Female	18	Right
2	Peter	USA	Male	19	Right
3	John	USA	Male	22	Left
4	Fatima	Bangadesh	Female	31	Left
5	Kadir	Bangadesh	Male	25	Left
6	Dhaval	India	Male	35	Left
7	Sudhir	India	Male	31	Left
8	Parvir	India	Male	37	Right
9	Yan	China	Female	52	Right
10	Juan	China	Female	58	Left
11	Liang	China	Male	43	Left
'''
pd.crosstab(df.Nationality,df.Handedness) # croostab allow you to create quick tables with counts of the fileds that you indicate
'''
Handedness	Left	Right
Nationality		
Bangadesh	2	0
China	2	1
India	2	1
USA	1	3
'''
pd.crosstab(df.Sex,df.Handedness)
'''
Handedness	Left	Right
Sex		
Female	2	3
Male	5	2
Margins
'''
pd.crosstab(df.Sex,df.Handedness, margins=True)
'''
Handedness	Left	Right	All
Sex			
Female	2	3	5
Male	5	2	7
All	7	5	12
Multi Index Column and Rows
'''
pd.crosstab(df.Sex, [df.Handedness,df.Nationality], margins=True) #you can use multiples values 
'''
Handedness	Left	Right	All
Nationality	Bangadesh	China	India	USA	China	India	USA	
Sex								
Female	1	1	0	0	1	0	2	5
Male	1	1	2	1	0	1	1	7
All	2	2	2	1	1	1	3	12
'''
pd.crosstab([df.Nationality, df.Sex], [df.Handedness], margins=True) 
'''
Handedness	Left	Right	All
Nationality	Sex			
Bangadesh	Female	1	0	1
Male	1	0	1
China	Female	1	1	2
Male	1	0	1
India	Male	2	1	3
USA	Female	0	2	2
Male	1	1	2
All		7	5	12
Normalize
'''
pd.crosstab(df.Sex, df.Handedness, normalize='index') # also you can normalize the data and give the percentage of every case
'''
Handedness	Left	Right
Sex		
Female	0.400000	0.600000
Male	0.714286	0.285714
'''
##Aggfunc and Values
import numpy as np
pd.crosstab(df.Sex, df.Handedness, values=df.Age, aggfunc=np.average) # you can configure row and columns and aolse indicate the values that you want and that values can handle it with some function
'''
Handedness	Left	Right
Sex		
Female	44.5	31.0
Male	31.2	28.0
'''
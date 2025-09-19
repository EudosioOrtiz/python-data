#Reshape pandas dataframe using melt
import pandas as pd
df = pd.read_csv("weather.csv")
df
'''
day	chicago	chennai	berlin
0	Monday	32	75	41
1	Tuesday	30	77	43
2	Wednesday	28	75	45
3	Thursday	22	82	38
4	Friday	30	83	30
5	Saturday	20	81	45
6	Sunday	25	77	47
'''
melted = pd.melt(df, id_vars=["day"], var_name='city', value_name='temperature')
melted
'''
day	city	temperature
0	Monday	chicago	32
1	Tuesday	chicago	30
2	Wednesday	chicago	28
3	Thursday	chicago	22
4	Friday	chicago	30
5	Saturday	chicago	20
6	Sunday	chicago	25
7	Monday	chennai	75
8	Tuesday	chennai	77
9	Wednesday	chennai	75
10	Thursday	chennai	82
11	Friday	chennai	83
12	Saturday	chennai	81
13	Sunday	chennai	77
14	Monday	berlin	41
15	Tuesday	berlin	43
16	Wednesday	berlin	45
17	Thursday	berlin	38
18	Friday	berlin	30
19	Saturday	berlin	45
20	Sunday	berlin	47
'''
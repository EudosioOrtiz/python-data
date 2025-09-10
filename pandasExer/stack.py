#Reshape dataframe using stack/unstack
import pandas as pd
df = pd.read_excel("stocks.xlsx",header=[0,1])
df
'''
Price	Price to earnings ratio (P/E)
Company	Facebook	Google	Microsoft	Facebook	Google	Microsoft
2017-06-05	155	955	66	37.10	32.0	30.31
2017-06-06	150	987	69	36.98	31.3	30.56
2017-06-07	153	963	62	36.78	31.7	30.46
2017-06-08	155	1000	61	36.11	31.2	30.11
2017-06-09	156	1012	66	37.07	30.0	31.00
'''
df.stack()
'''
Price	Price to earnings ratio (P/E)
Company		
2017-06-05	Facebook	155	37.10
Google	955	32.00
Microsoft	66	30.31
2017-06-06	Facebook	150	36.98
Google	987	31.30
Microsoft	69	30.56
2017-06-07	Facebook	153	36.78
Google	963	31.70
Microsoft	62	30.46
2017-06-08	Facebook	155	36.11
Google	1000	31.20
Microsoft	61	30.11
2017-06-09	Facebook	156	37.07
Google	1012	30.00
Microsoft	66	31.00
'''
df.stack(level=0)
'''
Company	Facebook	Google	Microsoft
2017-06-05	Price	155.00	955.0	66.00
Price to earnings ratio (P/E)	37.10	32.0	30.31
2017-06-06	Price	150.00	987.0	69.00
Price to earnings ratio (P/E)	36.98	31.3	30.56
2017-06-07	Price	153.00	963.0	62.00
Price to earnings ratio (P/E)	36.78	31.7	30.46
2017-06-08	Price	155.00	1000.0	61.00
Price to earnings ratio (P/E)	36.11	31.2	30.11
2017-06-09	Price	156.00	1012.0	66.00
Price to earnings ratio (P/E)	37.07	30.0	31.00
'''
df_stacked=df.stack()
df_stacked
'''
Price	Price to earnings ratio (P/E)
Company		
2017-06-05	Facebook	155	37.10
Google	955	32.00
Microsoft	66	30.31
2017-06-06	Facebook	150	36.98
Google	987	31.30
Microsoft	69	30.56
2017-06-07	Facebook	153	36.78
Google	963	31.70
Microsoft	62	30.46
2017-06-08	Facebook	155	36.11
Google	1000	31.20
Microsoft	61	30.11
2017-06-09	Facebook	156	37.07
Google	1012	30.00
Microsoft	66	31.00
'''
df_stacked.unstack()
'''
Price	Price to earnings ratio (P/E)
Company	Facebook	Google	Microsoft	Facebook	Google	Microsoft
2017-06-05	155	955	66	37.10	32.0	30.31
2017-06-06	150	987	69	36.98	31.3	30.56
2017-06-07	153	963	62	36.78	31.7	30.46
2017-06-08	155	1000	61	36.11	31.2	30.11
2017-06-09	156	1012	66	37.07	30.0	31.00
3 levels of column headers
'''
df2 = pd.read_excel("stocks_3_levels.xlsx",header=[0,1,2])
df2
'''
Price Ratios	Income Statement
Price	Price to earnings ratio (P/E)	Net Sales	Net Profit
Company	Facebook	Google	Microsoft	Facebook	Google	Microsoft	Facebook	Google	Microsoft	Facebook	Google	Microsoft
Q1 2016	155	955	66	37.10	32.0	30.31	2.6	20	18.70	0.80	5.43	4.56
Q2 2016	150	987	69	36.98	31.3	30.56	3.1	22	21.30	0.97	5.89	5.10
Q3 2016	153	963	62	36.78	31.7	30.46	4.3	24	21.45	1.20	6.10	5.43
Q4 2016	155	1000	61	36.11	31.2	30.11	6.7	26	21.88	1.67	6.50	5.89
Q1 2017	156	1012	66	37.07	30.0	31.00	8.1	31	22.34	2.03	6.40	6.09
'''
df2.stack()
'''
Income Statement	Price Ratios
Net Profit	Net Sales	Price	Price to earnings ratio (P/E)
Company				
Q1 2016	Facebook	0.80	2.60	155	37.10
Google	5.43	20.00	955	32.00
Microsoft	4.56	18.70	66	30.31
Q2 2016	Facebook	0.97	3.10	150	36.98
Google	5.89	22.00	987	31.30
Microsoft	5.10	21.30	69	30.56
Q3 2016	Facebook	1.20	4.30	153	36.78
Google	6.10	24.00	963	31.70
Microsoft	5.43	21.45	62	30.46
Q4 2016	Facebook	1.67	6.70	155	36.11
Google	6.50	26.00	1000	31.20
Microsoft	5.89	21.88	61	30.11
Q1 2017	Facebook	2.03	8.10	156	37.07
Google	6.40	31.00	1012	30.00
Microsoft	6.09	22.34	66	31.00
'''
df2.stack(level=0)
'''
Net Profit	Net Sales	Price	Price to earnings ratio (P/E)
Company	Facebook	Google	Microsoft	Facebook	Google	Microsoft	Facebook	Google	Microsoft	Facebook	Google	Microsoft
Q1 2016	Income Statement	0.80	5.43	4.56	2.6	20.0	18.70	NaN	NaN	NaN	NaN	NaN	NaN
Price Ratios	NaN	NaN	NaN	NaN	NaN	NaN	155.0	955.0	66.0	37.10	32.0	30.31
Q2 2016	Income Statement	0.97	5.89	5.10	3.1	22.0	21.30	NaN	NaN	NaN	NaN	NaN	NaN
Price Ratios	NaN	NaN	NaN	NaN	NaN	NaN	150.0	987.0	69.0	36.98	31.3	30.56
Q3 2016	Income Statement	1.20	6.10	5.43	4.3	24.0	21.45	NaN	NaN	NaN	NaN	NaN	NaN
Price Ratios	NaN	NaN	NaN	NaN	NaN	NaN	153.0	963.0	62.0	36.78	31.7	30.46
Q4 2016	Income Statement	1.67	6.50	5.89	6.7	26.0	21.88	NaN	NaN	NaN	NaN	NaN	NaN
Price Ratios	NaN	NaN	NaN	NaN	NaN	NaN	155.0	1000.0	61.0	36.11	31.2	30.11
Q1 2017	Income Statement	2.03	6.40	6.09	8.1	31.0	22.34	NaN	NaN	NaN	NaN	NaN	NaN
Price Ratios	NaN	NaN	NaN	NaN	NaN	NaN	156.0	1012.0	66.0	37.07	30.0	31.00
'''
df2.stack(level=1)
'''
Income Statement	Price Ratios
Company	Facebook	Google	Microsoft	Facebook	Google	Microsoft
Q1 2016	Net Profit	0.80	5.43	4.56	NaN	NaN	NaN
Net Sales	2.60	20.00	18.70	NaN	NaN	NaN
Price	NaN	NaN	NaN	155.00	955.0	66.00
Price to earnings ratio (P/E)	NaN	NaN	NaN	37.10	32.0	30.31
Q2 2016	Net Profit	0.97	5.89	5.10	NaN	NaN	NaN
Net Sales	3.10	22.00	21.30	NaN	NaN	NaN
Price	NaN	NaN	NaN	150.00	987.0	69.00
Price to earnings ratio (P/E)	NaN	NaN	NaN	36.98	31.3	30.56
Q3 2016	Net Profit	1.20	6.10	5.43	NaN	NaN	NaN
Net Sales	4.30	24.00	21.45	NaN	NaN	NaN
Price	NaN	NaN	NaN	153.00	963.0	62.00
Price to earnings ratio (P/E)	NaN	NaN	NaN	36.78	31.7	30.46
Q4 2016	Net Profit	1.67	6.50	5.89	NaN	NaN	NaN
Net Sales	6.70	26.00	21.88	NaN	NaN	NaN
Price	NaN	NaN	NaN	155.00	1000.0	61.00
Price to earnings ratio (P/E)	NaN	NaN	NaN	36.11	31.2	30.11
Q1 2017	Net Profit	2.03	6.40	6.09	NaN	NaN	NaN
Net Sales	8.10	31.00	22.34	NaN	NaN	NaN
Price	NaN	NaN	NaN	156.00	1012.0	66.00
Price to earnings ratio (P/E)	NaN	NaN	NaN	37.07	30.0	31.00
'''
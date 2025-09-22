#Dataframe and mysql database tutorial
import pandas as pd
import sqlalchemy
engine = sqlalchemy.create_engine('mysql+pymysql://root:@localhost:3306/application')
#Format of connection string is:

#mysql+pymysql://username:password@host:port/database_name

#Format of connection string for other databases

#https://pandas.pydata.org/pandas-docs/stable/io.html#engine-connection-examples



#Read entire table in a dataframe using read_sql_table
df = pd.read_sql_table('customers',engine)
df
'''
id	name	phone_number
0	1	Donald	7326784567
1	2	Bill	6573489999
2	3	Modi	4567895646
Read only selected columns
'''
df = pd.read_sql_table('customers', engine, columns=["name"])
df
'''
name
0	Donald
1	Bill
2	Modi
Join two tables and read them in a dataframe using read_sql_query
'''
df = pd.read_sql_query("select id,name from customers",engine)
df
'''
id	name
0	1	Donald
1	2	Bill
2	3	Modi
'''
query = '''
 SELECT customers.name, customers.phone_number, orders.name, orders.amount
 FROM customers INNER JOIN orders
 ON customers.id=orders.customer_id
'''
df = pd.read_sql_query(query,engine)
df
'''
name	phone_number	name	amount
0	Donald	7326784567	Google Pixel	950.0
1	Bill	6573489999	Yoga Mat	20.0
2	Modi	4567895646	Fossil Watch	120.0
read_sql is a wrapper around read_sql_query and read_sql_table
'''
query = '''
 SELECT customers.name, customers.phone_number, orders.name, orders.amount
 FROM customers INNER JOIN orders
 ON customers.id=orders.customer_id
'''
pd.read_sql(query,engine)
'''
name	phone_number	name	amount
0	Bill	6573489999	Yoga Mat	20.0
1	Donald	7326784567	Google Pixel	950.0
2	Modi	4567895646	Fossil Watch	120.0
'''
pd.read_sql("customers",engine)
'''
id	name	phone_number
0	1	Donald	7326784567
1	2	Bill	6573489999
2	3	Modi	4567895646
3	10	rafael nadal	4567895647
4	11	maria sharapova	434534545
5	12	vladimir putin	89345345
6	13	kim un jong	123434456
7	14	jeff bezos	934534543
8	15	rahul gandhi	44324222
Write to mysql database using to_sql
'''
df = pd.read_csv("customers.csv")
df
'''
Customer Name	Customer Phone
0	rafael nadal	4567895647
1	maria sharapova	434534545
2	vladimir putin	89345345
3	kim un jong	123434456
4	jeff bezos	934534543
5	rahul gandhi	44324222
'''
df.rename(columns={
    'Customer Name': 'name',
    'Customer Phone': 'phone_number'
}, inplace=True)
df
'''
name	phone_number
0	rafael nadal	4567895647
1	maria sharapova	434534545
2	vladimir putin	89345345
3	kim un jong	123434456
4	jeff bezos	934534543
5	rahul gandhi	44324222
'''
df.to_sql(
    name='customers', # database table name
    con=engine,
    if_exists='append',
    index=False
)
#to_sql has different parameters such as chunksize which allows to write data in chunks. This is useful when size of dataframe is huge
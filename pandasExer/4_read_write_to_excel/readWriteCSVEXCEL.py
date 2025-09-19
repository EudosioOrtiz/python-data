import pandas as pd

df = pd.read_csv("stock_data.csv")
df

df = pd.read_csv("stock_data.csv", skiprows=1)
df

df = pd.read_csv("stock_data.csv", header=1) # skiprows and header are kind of same
df

df = pd.read_csv("stock_data.csv", header=None, names = ["ticker","eps","revenue","people"])
df

df = pd.read_csv("stock_data.csv",  nrows=2)
df

df = pd.read_csv("stock_data.csv", na_values=["n.a.", "not available"])
df

df = pd.read_csv("stock_data.csv",  na_values={
        'eps': ['not available'],
        'revenue': [-1],
        'people': ['not available','n.a.']
    })
df

#Write to CSV
df.to_csv("new.csv", index=False)
df.columns

df.to_csv("new.csv",header=False)
df.to_csv("new.csv", columns=["tickers","price"], index=False)
#Read Excel
df = pd.read_excel("stock_data.xlsx","Sheet1")
df

def convert_people_cell(cell):
    if cell=="n.a.":
        return 'Sam Walton'
    return cell

def convert_price_cell(cell):
    if cell=="n.a.":
        return 50
    return cell
    
df = pd.read_excel("stock_data.xlsx","Sheet1", converters= {
        'people': convert_people_cell,
        'price': convert_price_cell
    })
df

#Write to Excel
df.to_excel("new.xlsx", sheet_name="stocks", index=False, startrow=2, startcol=1)
#Write two dataframes to two separate sheets in excel

df_stocks = pd.DataFrame({
    'tickers': ['GOOGL', 'WMT', 'MSFT'],
    'price': [845, 65, 64 ],
    'pe': [30.37, 14.26, 30.97],
    'eps': [27.82, 4.61, 2.12]
})

df_weather =  pd.DataFrame({
    'day': ['1/1/2017','1/2/2017','1/3/2017'],
    'temperature': [32,35,28],
    'event': ['Rain', 'Sunny', 'Snow']
})
with pd.ExcelWriter('stocks_weather.xlsx') as writer:
    df_stocks.to_excel(writer, sheet_name="stocks")
    df_weather.to_excel(writer, sheet_name="weather")
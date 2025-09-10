import pandas as pd
#Using csv
df = pd.read_csv('./pandasExer/weather_data.csv')
#print(df)
#Using excel
df2 = pd.read_excel('./pandasExer/weather_data.xlsx','Sheet1')
#print(df2)

#Using dictionary

def data():
    weather_data = {
        'day': ['1/1/2017','1/2/2017','1/3/2017'],
        'temperature': [32,35,28],
        'windspeed': [6,7,2],
        'event': ['Rain', 'Sunny', 'Snow']
    }
    return weather_data

weather_data = {
    'day': ['1/1/2017','1/2/2017','1/3/2017'],
    'temperature': [32,35,28],
    'windspeed': [6,7,2],
    'event': ['Rain', 'Sunny', 'Snow']
}
df3 = pd.DataFrame(weather_data)
#print(df3)

#Using tuples list
weather_data = [
    ('1/1/2017',32,6,'Rain'),
    ('1/2/2017',35,7,'Sunny'),
    ('1/3/2017',28,2,'Snow')
]
df = pd.DataFrame(data=weather_data, columns=['day','temperature','windspeed','event'])
#print(df)

#Using list of dictionaries
weather_data = [
    {'day': '1/1/2017', 'temperature': 32, 'windspeed': 6, 'event': 'Rain'},
    {'day': '1/2/2017', 'temperature': 35, 'windspeed': 7, 'event': 'Sunny'},
    {'day': '1/3/2017', 'temperature': 28, 'windspeed': 2, 'event': 'Snow'},
    
]
df = pd.DataFrame(data=weather_data, columns=['day','temperature','windspeed','event'])
#print(df)
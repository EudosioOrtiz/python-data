import pandas as pd

india_weather = pd.DataFrame({
    "city": ["mumbai","delhi","banglore"],
    "temperature": [32,45,30],
    "humidity": [80, 60, 78]
})
india_weather

us_weather = pd.DataFrame({
    "city": ["new york","chicago","orlando"],
    "temperature": [21,14,35],
    "humidity": [68, 65, 75]
})
us_weather

df = pd.concat([india_weather, us_weather])
df
df = pd.concat([india_weather, us_weather], ignore_index=True)
df

df = pd.concat([india_weather, us_weather], keys=["india", "us"])
df

df.loc["us"]

df.loc["india"]

temperature_df = pd.DataFrame({
    "city": ["mumbai","delhi","banglore"],
    "temperature": [32,45,30],
}, index=[0,1,2])
temperature_df

windspeed_df = pd.DataFrame({
    "city": ["delhi","mumbai"],
    "windspeed": [7,12],
}, index=[1,0])
windspeed_df

df = pd.concat([temperature_df,windspeed_df],axis=1)
df

s = pd.Series(["Humid","Dry","Rain"], name="event")
s

df = pd.concat([temperature_df,s],axis=1)
df


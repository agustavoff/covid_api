import requests
import json
import pandas as pd
import os
import matplotlib.pyplot as plt

# Basic configs
endpoint = 'https://api.covid19api.com/country'
country = 'brazil'
start_dt = '2020-03-01'
end_dt = '2020-04-01'


# Compose URL
url = f'{endpoint}/country/{country}?from={start_dt}&to={end_dt}'
# TODO: show other ways to create the same kind of string (format, '+', ...)


# Get data from Covid19 API
# TODO: execute in postman
response = requests.get(url)
resp_dict = response.json()  # Transform to a Dictionary data type
df = pd.DataFrame(resp_dict)

# TODO: Show dataframe...
# Select only the confirmed cases


# Calculate moving average
df['MA_14'] = df.rolling(window=14).mean()


# chart
plt.plot(df['Cases'], label='Cases')
plt.plot(df['MA_14'], label='MA 14 days')
plt.legend(loc='best')
plt.title('Covid-19\nCases and Moving Average (14 days)')
plt.show()
# TODO: improve this


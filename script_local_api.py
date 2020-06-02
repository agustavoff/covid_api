import requests
import pandas as pd

# API https://covid19api.com/
# https://documenter.getpostman.com/view/10808728/SzS8rjbc?version=latest
#
# GET response looks like:
#     {'Countries': [{'Country': 'Afghanistan',
#                     'CountryCode': 'AF',
#                     'Date': '2020-05-31T22:36:36Z',
#                     'NewConfirmed': 866,
#                     'NewDeaths': 3,
#                     'NewRecovered': 44,
#                     'Slug': 'afghanistan',
#                     'TotalConfirmed': 14525,
#                     'TotalDeaths': 249,
#                     'TotalRecovered': 1303},
#                    {'Country': 'Albania',
#                     'CountryCode': 'AL',
#                     'Date': '2020-05-31T22:36:36Z',
#                     'NewConfirmed': 23,
#                     'NewDeaths': 0,
#                     'NewRecovered': 6,
#                     'Slug': 'albania',
#                     'TotalConfirmed': 1122,
#                     'TotalDeaths': 33,
#                     'TotalRecovered': 857},
#                 ...
#     'Date': '2020-05-31T22:36:36Z',
#      'Global': {'NewConfirmed': 135514,
#                 'NewDeaths': 4355,
#                 'NewRecovered': 71158,
#                 'TotalConfirmed': 6149975,
#                 'TotalDeaths': 376268,
#                 'TotalRecovered': 2564042}}


# Get data from Covid19 API 
url = 'https://api.covid19api.com/summary'
response = requests.get(url)
resp_dict = response.json()     # Transform to a Dictionary data type
countries = resp_dict.get('Countries')  # Select just the "Countries" set of data

# Load data to Pandas
df = pd.DataFrame(countries)

# Select the "Country" and "Total" columns
df = df[['Country', 'TotalConfirmed', 'TotalDeaths', 'TotalRecovered']]

# Save data on the blob storage
df.to_csv('local.csv', index=False)     # Inittially save la local file
# TODO: save on blob


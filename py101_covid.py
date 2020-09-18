import requests
import json
import pandas as pd
import os
import matplotlib.pyplot as plt

# Get data from Covid19 API
url = 'https://api.covid19api.com/summary'

response = requests.get(url)
# TODO: SHOW THE PROPERTIES OF THE RESPONSE...
# TODO: EXPLAIN BRIEFLY THE HTTP STATUS

resp_dict = response.json()  # Transform to a Dictionary data type
# TODO: SHOW HOW IT LOOKS LIKE...

countries = resp_dict.get('Countries')  # Select just the "Countries" set of data

# Load data to Pandas
df = pd.DataFrame(countries)

# TODO: PRINT DATAFRAME
#   DTYPES
#   HEAD / TAIL
#   STATS PER COLUMNS

# Select the "Country" and "Total" columns
df = df[['Country', 'TotalConfirmed', 'TotalDeaths', 'TotalRecovered']]

# TODO: CREATE A CHART COMPARING ALL COUNTRIES... TO MANY COUNTRIES! LETS CLEAN IT A LITTLE BIT..


# TODO: SELECT COUNTRIES WHERE THE COMPANY HAS SITES
# DUMB WAY: ITERATE OVER ALL ROWS (FOR) AND SELECT THE DESIRED COUNTRY USING IF
# PANDAS WAY:  df[(df['Country'] == 'Brazil') & (df['think_something'] > 9999)]
# PANDAS - query:  df.query("Country = 'Brazil'...)


# TODO: CREATE A CHART COMPARING ALL COUNTRIES WHERE EXXON HAS SITES


# Save data
df.to_csv('local.csv', index=False)

# TODO: save in parquet, avro, excel...


# TODO: AND NOW.... DRILLDOWN TO AN SPECIFIC COUNTRY!
# GO TO NEXT PYTHON FILE...

## import dependencies
import tensorflow as tf 
import numpy as np
import pandas as pd
from datetime import datetime
## Loading the data as a pandas dataframe 
data = pd.read_csv("sunspots.csv", index_col=0) 
## show first dew rows of the dataset
data.head()

## import dependencies
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

## You can generate a Token from the "Tokens Tab" in the UI
token = "MoGhN6nViwhYfaoCU1ZSZJUvVNVPc6go0I3eS0BbJp43FAo81YoCpJTcyCLKHfqk_eZ-xwNIjXdYkPBAuZKT8g=="
org = "main"
bucket = "sunspot"
url = "http://localhost:8086"



# convert Date column to datetime 
data['Date'] = pd.to_datetime(data['Date'])

## create date as index
data.set_index(data['Date'], drop = True, inplace = True)
data.drop('Date', axis = 1, inplace = True)
data.head()

with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(data)




"""
Ingest DataFrame
"""
print()
print("=== Ingesting DataFrame via batching API ===")
print()
startTime = datetime.now()

with InfluxDBClient(url=url, token=token, org=org) as client:

        """
        Use batching API
        """
        with client.write_api() as write_api:
            write_api.write(bucket=bucket, record=data,
                            data_frame_tag_columns=['sunspot'],
                            data_frame_measurement_name="sunspot")
            print()
            print("Wait to finishing ingesting DataFrame...")
            print()

            print()
            print(f'Import finished in: {datetime.now() - startTime}')
            print()




## query data
#query_api = client.query_api()
#tables = query_api.query('from(bucket:"my-bucket") |> range(start: -275y)')
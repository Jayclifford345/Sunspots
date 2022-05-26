
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import pandas as pd

## You can generate a Token from the "Tokens Tab" in the UI
token = "MoGhN6nViwhYfaoCU1ZSZJUvVNVPc6go0I3eS0BbJp43FAo81YoCpJTcyCLKHfqk_eZ-xwNIjXdYkPBAuZKT8g=="
org = "main"
bucket = "sunspot"
url = "http://localhost:8086"

with InfluxDBClient(url=url, token=token, org=org) as client:
## query data
    query_api = client.query_api()
    tables = query_api.query_data_frame('from(bucket:"sunspot") |> range(start: -275y)')
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
        print(tables)
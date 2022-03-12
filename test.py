import pandas as pd
from av_api import AV_API
from db_connector import DB_connector

api = AV_API('TIME_SERIES_Daily','AMC','Full', 'Daily')
db = DB_connector()

datasql = db.select_table('stock_ticker')

print(datasql)

df1 = pd.read_csv('./stock_ticker_csvs/nasdaq_screener_1647107939010.csv')
print(df1)


data = api.call_api()

df = pd.DataFrame(data)
df_t = df.T
print(df_t)
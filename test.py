import pandas as pd
from AV_API import AV_API

api = AV_API('TIME_SERIES_Daily','AMC','Full', 'Daily')


data = api.call_api()

df = pd.DataFrame(data)
df_t = df.T
print(df_t)
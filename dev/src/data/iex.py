import pandas_datareader.data as web

import datetime

start = datetime.datetime(2018, 1, 1)

end = datetime.datetime(2019, 1, 1)

f = web.DataReader('MSFT', 'iex', start, end)

print(f.loc['2018-01-17']['open'])
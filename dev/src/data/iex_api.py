import pandas_datareader.data as web
import database as db

import datetime

start = datetime.datetime(2018, 1, 1)

end = datetime.datetime(2019, 1, 1)

f = web.DataReader('MSFT', 'iex', start, end)

close  = f.to_dict()["close"]

db.Database.initialize()

db.Database.insert('close', {"tid": 0, "ticker": 'MSFT', "data": close, "_id":0} )



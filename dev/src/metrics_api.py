"""
access layer to all the computed metrics that can feed to web mobile etc
"""
import src.data.storage.database as db

def getVolatility(tid):
    db.Database.initialize()
    data = db.Database.find_one("volatility",{"tid":tid})["data"]["2019-01-30"]
    return data

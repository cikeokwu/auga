"""
Data Access object designed to provide an interface for metrics to acess certain data and allow use to abstact away our
database and

"""
import dev.src.data.storage.database as db

db.Database.initialize()

def getData(collection, tid):
    return db.Database.find_one(collection,{"tid":tid})

def getClosePriceData(tid):
    return list(db.Database.find_one("close",{"tid":tid})['data'].values())


def saveMetric(collection,data):
    db.Database.insert(collection,data)

"""
Data Access object designed to provide an interface for metrics to acess certain data and allow use to abstact away our
database and

"""
import database as db

def getData(collection, ticker):
    db.find_one(collection,{tic})
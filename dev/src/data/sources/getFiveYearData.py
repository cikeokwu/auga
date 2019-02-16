import pandas as pd
import pandas_datareader.data as web
import pandas_datareader
import datetime
import numpy as np
from iexfinance import get_available_symbols, Stock
import iexfinance

DF =get_available_symbols()

stocko = pd.DataFrame(DF)
stockSymbols = stocko['symbol'].unique()
totalTickers = len(stockSymbols)


def get5yHistorical(stockSymbols, totalTickers):
    bigDF = Stock(stockSymbols[0],output_format="pandas").get_chart(range='5y').transpose()
    bigDF['ticker']=stockSymbols[0]
    bigDF.index= [bigDF['ticker'],bigDF.index]
    for i in range(1,totalTickers):
        try:
            print(" iteration:",i," ","ticker: ",stockSymbols[i], 'percentage:',i/totalTickers*100,end='\r')
            trial=pd.DataFrame(Stock(stockSymbols[i],output_format="pandas").get_chart(range='5y').transpose())
            trial['ticker']=stockSymbols[i]
            trial.index= [trial['ticker'],trial.index]
            bigDF = bigDF.append(trial)
        except KeyError:
            print('this key had an error:', stockSymbols[i], 'at position:',i)
            pass
        
    return bigDF

result=get5yHistorical(stockSymbols,totalTickers)	

result.to_csv('resulting5YearData.csv',index=[result.index])


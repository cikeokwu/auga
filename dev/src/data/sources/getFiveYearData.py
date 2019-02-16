import pandas as pd
import pandas_datareader.data as web
import pandas_datareader
import datetime
from iexfinance import get_available_symbols, Stock
import iexfinance

DF =get_available_symbols()

stocko = pd.DataFrame(DF)
stockSymbols = stocko['symbol'].unique()
totalTickers = len(stockSymbols)


def get5yHistorical(stockSymbols, totalTickers):
   	bigDF = Stock(stockSymbols[0],output_format="pandas").get_chart(range='5y')
    bigDF['ticker']=stockSymbols[0]
    for i in range(1,totalTickers):
        try:
            print(" iteration:",i," ","ticker: ",stockSymbols[i], 'percentage:',i/totalTickers*100,end='\r')
            trial=pd.DataFrame(Stock(stockSymbols[i],output_format="pandas").get_chart(range='5y'))
            trial['ticker']=stockSymbols[i]
            bigDF = bigDF.append(trial)
        except KeyError:
            print('\n this key had an error:', stockSymbols[i], 'at position:',i)
            pass
        
    return bigDF
result = get5yHistorical(stockSymbols,totalTickers)
result = result.dropna()
result.to_csv('iexRaw.csv')


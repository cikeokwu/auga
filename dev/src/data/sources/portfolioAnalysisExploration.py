
##Generates pandas dataframe of investment club's holdings

#below are the tickers I ran in the meeting.
#alibabe, bb&t, delta, ELT managers trust, fidelity,homedepot, JPMorgan and chase
# microsoft, morgan stanley, united health group, vanguard intermediate term, vanguard scalar index falits.
import pandas as pd

def generatePortfolioDF(portfolioStockTickers):
	totalDF = pd.read_csv('iexRaw.csv')

	portfolioDF = totalDF[totalDF['ticker']==portfolioStockTickers[0]]

	for ticker in portfolioStockTickers:
		df = totalDF[totalDF['ticker']==ticker]
		portfolioDF = portfolioDF.append(df)

	return portfolioDF
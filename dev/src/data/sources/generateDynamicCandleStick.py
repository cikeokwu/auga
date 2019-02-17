import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from bokeh.plotting import figure, show, output_file



#returns html code for a dynamic candlestick, to integrate with flask.
#takes in user necessary form. 

def generateCandleStick(userticker):
	fullStockDF = pd.read_csv('iexRaw.csv')
	try:
		chosenStock = fullStockDF[fullStockDF['ticker']==userticker]
		chosenStock['date']=pd.to_datetime(chosenStock['date'],infer_datetime_format=True)

		#get increasing and decreasing series of booleans 
		inc = chosenStock.close > chosenStock.open
		dec = chosenStock.open > chosenStock.close
		w = 12*60*60*1000 # half day in ms
		#get ticles
		title = chosenStock['ticker'].iloc[0] + ' Chart'
		TOOLS = "pan,wheel_zoom,box_zoom,reset,save"
		
		#figure addtions!
		p = figure(x_axis_type="datetime", tools=TOOLS, plot_width=1000, title = title)
		p.xaxis.major_label_orientation = 3.14/4
		p.grid.grid_line_alpha=0.3
		p.segment(chosenStock['date'], chosenStock['high'],chosenStock['date'], chosenStock['low'], color="black")
		p.vbar(chosenStock.date[inc], w, chosenStock.open[inc], chosenStock.close[inc], fill_color="#D5E1DD", line_color="black")
		p.vbar(chosenStock.date[dec], w, chosenStock.open[dec], chosenStock.close[dec], fill_color="#F2583E", line_color="black")
		
		#output_file("AUGA-"+userticker+".html", title=("auga"+userticker))

		#show(p)
		return p

	except NameError:
		print("Your ticker isnt found. Choose another")
		return
	
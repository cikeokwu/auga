from flask import Flask, render_template,redirect, url_for, request
import pandas as pd
from bokeh.resources import INLINE
from bokeh.embed import components
from bokeh.util.string import encode_utf8
from src.data.sources.generateDynamicCandleStick import generateCandleStick


app = Flask(__name__)

#Im making this an absolute path, replace with dynamic path, its a hackathon
datapath = "~/Desktop/projects/python/auga/dev/src/data/sources/"
# Create the main plot

mymorals= 'SPY' #global variables are great when you have 56 mins left

# Index page
@app.route('/')
def index():
	# Determine the selected feature
	if request.method == 'POST':
		mymorals= request.form
		return redirect(url_for('plot'))

	# Create the plot
	
	return render_template("index.html")

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')

@app.route('/plot/',methods=['POST','GET'])
def plot():
	currentTickerName = None
	if request.method == 'POST':
		currentTickerName= request.form['ticker']
	 
	if currentTickerName == None:
		currentTickerName = "SPY"
	print("\n current ticker is: ", currentTickerName)
	plot = generateCandleStick(currentTickerName,datapath)
	
	# Embed plot into HTML via Flask Render
	script, div = components(plot)
	js_resources = INLINE.render_js()
	css_resources = INLINE.render_css()	
	html = render_template(
	'plot.html',
	plot_script=script,
	plot_div=div,
	js_resources=js_resources,
	css_resources=css_resources,
	)

	return encode_utf8(html)
# With debug=True, Flask server will auto-reload 
# when there are code changes
if __name__ == '__main__':
	app.run(port=5000, debug=True)


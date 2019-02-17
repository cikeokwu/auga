from flask import Flask, render_template, request
import pandas as pd
from bokeh.resources import INLINE
from bokeh.embed import components
from bokeh.util.string import encode_utf8
from src.data.sources.generateDynamicCandleStick import generateCandleStick


app = Flask(__name__)

#Im making this an absolute path, replace with dynamic path, its a hackathon
datapath = "~/Desktop/projects/python/auga/dev/src/data/sources/"
# Create the main plot


# Index page
@app.route('/')
def index():
	# Determine the selected feature
	
	# Create the plot
	
	return render_template("index.html")


@app.route('/plot')
def plot():
	currentTickerName = request.args.get("feature_name")
	if currentTickerName == None:
		currentTickerName = "SPY"

	plot = generateCandleStick(currentTickerName,datapath)
	js_resources = INLINE.render_js()
	css_resources = INLINE.render_css()	
	# Embed plot into HTML via Flask Render
	script, div = components(plot)

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


# auga

# Tool to help organize stock market data for data analysis
## Data provided for free by IEX. View IEX’s Terms of Use.” You can find the terms here: https://iextrading.com/api-terms/


## Getting set up
1. Clone this repository. Ex:
''' bash
git clone ssh@github.com:ChristianIkeokwu/auga
'''

2. Set up a virtual python environment using the command:
''' bash
python3 -m venv auga/
'''

3. cd into that directory, then enter the virtual environment you created:
''' bash
cd auga/
source bin/activate

4. Install all the required python modules:
''' bash
pip3 install -r ./dev/requirements.txt
'''

5. Then, simply call the startup script:
'''bash
./start
'''


## Dependencies:
0. Python3
1. Scipy Package
2. Python-Flask
3. MongoDB
4. pymongo
5. pandasdatareader
6. iexfinance (pip install iexfinance)
7. Bokeh
8. jupyter notebooks

## Features:
embedded stock chart in Flask App
five year stock data generator (run in auga/dev/src/data/source/generatefiveyeardata.py)


## Resources
1. implement many charts for comaprison-- the python code is here: https://bokeh.pydata.org/en/latest/docs/gallery/stocks.html
2. Flask tutorial by sentdex

## Todo List
1. fix navigation
2. make portfolio page, where you can input x tickers and have the output as a chart.
3. Make Stock ticker dashboard


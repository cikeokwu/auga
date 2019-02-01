from flask import Flask
from flask import Blueprint,url_for,render_template
from src.metrics_api import getVolatility


app = Flask(__name__)


@app.route('/')
@app.route("/index")
def getVol():
    info = {"volatility": getVolatility(0)}
    return render_template("index.html",tid=0,info=info)


if __name__ == '__main__':
    app.run(debug=True)

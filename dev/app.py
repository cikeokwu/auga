from flask import Flask, render_template, redirect, flash
from flask import Blueprint,url_for,render_template
from src.metrics_api import getVolatility
from config import Config
from flask_bootstrap import Bootstrap
# Things needed to be imported for forms:
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
Bootstrap(app) # allow bootstrap extension
app.config.from_object(Config)

class MyForm(FlaskForm):
    ticker = StringField('ticker', validators=[DataRequired()])
    date = DateField('date', format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField('Go')

@app.route('/')
@app.route("/index", methods=['GET', 'POST'])
def submit():
    form = MyForm()
    if form.validate_on_submit():
        return redirect('/result')
    return render_template('index.html', form=form)

@app.route("/result")
def result():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)

from flask import render_template
from app import app

@app.route('/')
def index():
    '''
    Function that returns the index page & its data
    '''
    message = "Welcome to NewsHighlight"
    return render_template('index.html', messages = message)

@app.route('/news_source/<int:news_id>')
def news_source(news_id):
    '''
    News source page function that will return news sources plus data
    '''
    return render_template('news_source.html',id = news_id)

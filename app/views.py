from flask import render_template
from app import app
from .request import get_news_source

@app.route('/')
def index():
    '''
    Function that returns the index page & its data
    '''
    # Fetch Technology 
    technology_news = get_news_source('technology')

    # Fetch General
    general_news = get_news_source('general')

    #Fetch Sports
    sports_news = get_news_source('sports')

    #Fetch Business
    business_news = get_news_source('business')

    #Fetch Entertainment
    entertainment_news = get_news_source('entertainment')

    #Fetch Health
    health_news = get_news_source('health')

    #Title
    title = 'Get breaking news headlines'

    return render_template('index.html', title = title, tech = technology_news, general = general_news, sports = sports_news, business = business_news, entertainment = entertainment_news, health = health_news)

@app.route('/news_source/<int:news_id>')
def news_source(news_id):
    '''
    News source page function that will return news sources plus data
    '''
    return render_template('news_source.html',id = news_id)

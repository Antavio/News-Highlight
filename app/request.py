from app import app
import urllib.request,json
from .models import news_sources

News_sources= news_sources.News_sources

#Get API Key
api_key = app.config['NEWS_API_KEY']

#Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]

def get_news_source(category):
    '''
    A Function that gets json response to our url request
    '''
    get_news_source_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_source_url) as url:
        get_news_source_data = url.read()
        get_news_source_response = json.loads(get_news_source_data)

        news_sources_results = None

        if get_news_source_response['sources']:
            news_sources_list = get_news_source_response['sources']
            news_sources_results = process_sources(news_sources_list)

    return news_sources_results

def process_sources(news_list):
    '''
    A function that will process news_list & transform them into a list of objects
    params:
        movie_list: A list of dictionaries that contain news details
    returns:
        news_results: A list of new objects
    '''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')

        news_objects = News_sources(id,name,description,url)
        news_results.append(news_objects)

    return news_results

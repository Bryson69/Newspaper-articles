import urllib.request
import json
from .models import Sources, Articles
from datetime import datetime

# Getting api key
api_key = None

# Getting the articlces url
articles_url = None


# Getting the news base url
base_url = None



def configure_request(app):
    global api_key, base_url, articles_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_SOURCES_BASE_URL']
    articles_url = app.config['ARTICLES_BASE_URL']



def process_articles(articles_list):
    articles_object = []
    for article_item in articles_list:
        id = article_item.get('id')
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        image = article_item.get('urlToImage')
        date = article_item.get('publishedAt')

        if image:
            articles_result = Articles(
                id, author, title, description, url, image, date)
            articles_object.append(articles_result)

    return articles_object



def get_articles(id):
    '''
    Function that processes the articles and returns a list of articles objects
    '''
    get_articles_url = articles_url.format(id, api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        articles_results = json.loads(url.read())

        articles_object = None
        if articles_results['articles']:
            articles_object = process_articles(articles_results['articles'])

    return articles_object

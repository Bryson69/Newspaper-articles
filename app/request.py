from app import app
import urllib.request,json
from .models import article

Article = article.Article

#Getting api key
api_key = app.config['ARTICLE_API_KEY']
#GETTING MOVIE BASE URL
base_url = app.config['ARTICLE_BASE_URL']

def get_articles(category):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        article_results = None

        if get_articles_response['articles']:
            article_results_list = get_articles_response['articles']
            article_results = process_results(article_results_list)

    return article_results

def process_results(article_list):
    '''
    Function that processes the article result and transform them to a list of object

    Args:
        article_list: A lst of dictionaries that contain article details

    Returns:
        article_results:A list of article objects
    '''

    article_results = []
    for article_item in article_list:
        id = article_item.get('id')
        name = article_item.get('name')
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        content = article_item.get('content')

        article_object = Article(id,name,author,title,description,content)
        article_results.append(article_object)

    return article_results

def get_article(id):
    
    get_articles_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_article_details_url) as url:
       article_details_data = url.read()
       article_details_response = json.loads(article_details_data)

        article_results = None
        if article_details_response:
            id = article_details_response.get('id')
            name = article_details_response.get('name')
            author = article_details_response.get('author')
            title = article_details_response.get('title')
            description = article_details_response.get('description')
            content = article_details_response.get('content')

            article_object = Article(id,name,author,title,description,content)



    return article_object


            
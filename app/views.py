from flask import render_template
from app import app
from .request import get_articles


# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    scoop_article = get_articles('scoop')
    politics_article = get_articles('politics')
    title = 'The best article page'
    return render_template('index.html', title = title)



    
# @app.route('/article/<int:article_id>')
# def article(article_id):
#     '''
#     Views article page that returns the atricle and its data
#     '''

#     return render_template('article.html', id = article_id)

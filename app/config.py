class Config:
    '''
    General configuration parent class
    '''

    # ARTICLE_BASE_URL ='https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
   	# ARTICLE_BASE_URL = 'https://newsapi.org/v2/everything?language=en&sources={}&apiKey={}'
    ARTICLE_BASE_URL = 'https://newsapi.org/v2/everything?q={}&apiKey={}'
    ARTICLE_API_KEY = '95b3000b62764125a9981921ca505d4a'



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
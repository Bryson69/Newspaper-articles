import unittest
from models import article

Article = article.Article

class ArticleTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''

        self.new.article = Article('The articleis the best','My homie')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_artcle ,Article))



if __name__ == '__main__':
    unittest.main()
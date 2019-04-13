import unittest
from models import news_sources

News_sources= news_sources.News_sources

class NewsTest(unittest.TestCase):
    '''
    Test classs to test News_sources class
    '''
    def setUp(self):
        '''
        Runs before every Test
        '''
        self.new_source = News_sources ('bbc-sport','BBC Sport','The home of BBC Sport online',"http://www.bbc.co.uk/sport")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,News_sources))

if __name__ == '__main__':
    unittest.main()
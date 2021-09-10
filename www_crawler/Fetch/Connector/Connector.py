from urllib.request import Request, urlopen
# from Fetch.SingletonInstane import SingletonInstane

'''
Connector 클래스

하위 클래스
NaverConnector, GoogleConnector, Connect_agent
'''

class Connector(object):

    def __init__(self, word):
        '''
        :param word: 검색 단어
        '''
        self.word = word

    def search_engine(self, url):
        '''
        :param url:  url 링크
        :return: url_link
        '''

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
        re = Request(url + self.word, headers=headers)
        source_code_from_URL = urlopen(re)

        return source_code_from_URL

    def url_opener(self, url):

        try:
            result = urlopen(url)
        except:
            result = False

        return result







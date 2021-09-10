from Fetch.Connector.Connector import Connector
from Fetch.Connector.NaverConnector import NaverConnector
from Fetch.Connector.GoogleConnector import GoogleConnector
from urllib.parse import quote

class Connector_agent(Connector):

    def __init__(self, word):
        '''
        생성자, Naver, Google Connector를 실행 시키며, 검색할 단어인 Word를 전달한다.
        :param word: [Type = String] 검색할 단어 '문장도 가능'
        '''
        word = quote(word)
        super().__init__(word)
        print('-' * 50)
        print('[System] Connector agent on')
        print('-' * 50)
        self.naver_page_cnt, self.google_page_cnt = (1, 1)
        self.nc = NaverConnector(word)
        self.gc = GoogleConnector(word)

    def search_getter(self):
        '''
        검색 결과 URL을 모아서 가져다 준다.
        :return: [Type = Dictionary | key : [Type = String] , Value : [Type = 'http.client.HTTPResponse']]
        '''
        url_dic = {}

        print('-' * 50)
        print('[Message]Connector agent : 링크 연결 기능 동작')
        print('-' * 50)

        url_dic[self.nc.engine_name] = self.nc.naver_get_real_url()

        print('-' * 50)
        print('[Message]Connector agent : 네이버 Response HTTP 객체 획득')
        print('Naver : ', self.nc.url)
        print('-' * 50)

        url_dic[self.gc.engine_name] = self.gc.google_get_real_url()

        print('-' * 50)
        print('[Message]Connector agent : 구글 Response HTTP 객체 획득')
        print('Google : ', self.gc.url)
        print('-' * 50)

        return url_dic

    def num_link_checker(self, page_links):
        '''

        :param page_links:
        :return:
        '''

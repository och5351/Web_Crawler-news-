from Fetch.Collector.Collector_agent import Collector_agent
from Fetch.Connector.Connector_agent import Connector_agent
from Util.Util_agent import Util_agent
import os

if __name__ == '__main__':

    word = '쿠버네티스'
    conn_agent = Connector_agent(word)
    coll_agent = Collector_agent()
    util_agent = Util_agent()

    # Naver, Google 검색 엔진 검색
    first_real_url = conn_agent.search_getter()

    # html 획득
    htmls = coll_agent.page_get_html(urls=first_real_url)

    # Naver, Google url 획득(페이지 넘기기 기능 추가 해야 함)
    search_urls = coll_agent.get_url(htmls)

    # 획득한 url 접속 후 html scrap & save(Parsing 과정 생략)
    for key in search_urls.keys():
        for url in search_urls[key]:
            soup = conn_agent.url_opener(url)
            html_data = coll_agent.get_html(soup)
            print(os.listdir())
            os.mkdir('Naver_html')
            #util_agent.save_html(html_data, '1', os.listdir())
            break
    #


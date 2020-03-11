# -*- coding: utf-8 -*-
from CrawlingCategory.crawlingUtil import CrawUtil

class naverLifeCultureCrawling:

    crawlingUtil = CrawUtil()

    def __init__(self, today, rootPath):

        path = rootPath + '/LifeCulture'
        URL = 'https://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day&sectionId=103&date=' + today
        links = self.crawlingUtil.get_link(URL)
        fileNum = self.crawlingUtil.isInDirectory(path)
        p = 0
        for count in range(len(links)):
            result_text = self.crawlingUtil.get_text('https://news.naver.com/'+ links[count])
            if result_text == '':
                p += 1
            else:
                OUTPUT_FILE_NAME = 'LifeCulture/LifeCulture%05d.txt' % (count + fileNum - p)
                print(OUTPUT_FILE_NAME)
                open_output_file = open(OUTPUT_FILE_NAME, 'w', -1, "utf-8")
                open_output_file.write(result_text)
                open_output_file.close()
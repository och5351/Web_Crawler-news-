# -*- coding: utf-8 -*-
from datetime import datetime
from CrawlingCategory.naverFinanceCr import naverFinanceCrawling
from CrawlingCategory.naverScienceCr import naverScienceCrawling
from CrawlingCategory.naverSocialCr import naverSocialCrawling
from CrawlingCategory.naverPoliticsCr import naverPoliticsCrawling
from CrawlingCategory.naverWorldCr import naverWorldCrawling
from CrawlingCategory.naverLifeCultureCr import naverLifeCultureCrawling
import schedule
import time


def job_day():
    for i in range(29):
        tempStr = __file__
        today = '202002' + '%02d' %(i+1) # str(datetime.today().year) + "%02d" % datetime.today().month + "%02d" % datetime.today().day
        rootPath = tempStr[:-16]

        naverFinanceCrawling(today, rootPath)
        naverScienceCrawling(today, rootPath)
        naverSocialCrawling(today, rootPath)
        naverPoliticsCrawling(today, rootPath)
        naverWorldCrawling(today, rootPath)
        naverLifeCultureCrawling(today, rootPath)
        print('\n')
        print("="*120)
        print('\n\t' + str(today) + ' 크롤링 완료')
        print('\n')
        print("=" * 120)


if __name__ == '__main__':
    job_day()
    #schedule.every().days.at("11:55").do(job_day)
    #while True:
        #schedule.run_pending()
        #time.sleep(1)

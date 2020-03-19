# -*- coding: utf-8 -*-
from datetime import datetime

from CrawlingCategory.GameCategory import GameCategory

import time


def job_day():
    for i in range(1):
        tempStr = __file__
        today = str(datetime.today().year) + "%02d" % datetime.today().month + "%02d" % datetime.today().day
        rootPath = tempStr[:-16] # 현재 프로그램 경로

        GameCategory(count=135, rootPath=rootPath)

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

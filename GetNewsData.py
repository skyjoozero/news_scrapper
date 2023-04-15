import pprint

import requests
import json
import re
import os.path
from collections import OrderedDict
from time import sleep
from bs4 import BeautifulSoup as bs
from NewsDataToFile import NewsDataToFile

class GetNewsData():

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Whale/3.19.166.16 Safari/537.36'
    }

    def _getSoup(self, urlString):
        mainPage = requests.get(urlString, headers=self.headers)
        return bs(mainPage.content, "html.parser")

    def _getNewsTitlesAndUrlHTMLArray(self, newses):
        for news in newses:
            tempSoup = bs(str(news), "html.parser")
            if tempSoup.getText() == '' or tempSoup.find('img'):
                newses.remove(news)
        # newses = [str(news).strip('\n\t') for news in newses]
        return newses

    def _findTitleUrl(self, data):
        returnData = []
        for tag in data:
            tempSoup = bs(str(tag), 'html.parser')
            returnData.append([tempSoup.getText(), tempSoup.find('a')['href']])
        return returnData

    def _getNewsWriter(self, contents):
        arr = []

        for el in contents.find_all('span', 'writing'):
            arr.append(el.get_text().strip())
        print(arr)
        print(len(arr))
        return arr

    def changeNewsNum(self, jsonString, addedNum = False):
        '''
        :param jsonString: dict
        :return: dict
        '''
        jsonData = jsonString
        newsNumber = jsonData['newsCount']
        articles = jsonData['articles']

        for i in range(newsNumber):
            print(i)
            articles[i - newsNumber] = articles[i + 1]
        for i in range(-(newsNumber), 0, 1):
            print(i)
            articles[abs(i)] = articles[i]
            articles.pop(i)

        return jsonData

    def getNewsJsonData(self, date):
        '''
        :param date: 'YYYYMMDD'형식 문자영
        :return: json object
        '''

        returnData = {"date": date,
                      "newsCount": 0,
                      "articles": {}}
        page = 1
        mainUrl = 'https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid2=258&sid1=101&date=' + str(date) + '&page='

        while True:
            soup = self._getSoup(mainUrl + str(page))
            print(mainUrl + str(page))
            pprint.pprint(soup.select_one('div.paging'))
            pageNum = soup.select_one('div.paging').find('strong').getText()

            if str(page) != pageNum:
                break
            else:
                print('page: ' + pageNum)

                newses = soup.select_one('div.newsflash_body').find_all('a')
                data = self._getNewsTitlesAndUrlHTMLArray(newses)
                newsData = self._findTitleUrl(data)

                contents = soup.select_one('div.list_body')
                writer = self._getNewsWriter(contents)
                if len(newsData) == len(writer):
                    for i in range(len(newsData)):
                        returnData["newsCount"] += 1
                        returnData["articles"][returnData["newsCount"]] = {"title": re.sub('\s+', ' ', newsData[i][0]),
                                                                           "url": re.sub('\s+', ' ', newsData[i][1]),
                                                                           "writer": writer[i]}
                else:
                    pass  # todo: 오류 발생 시 디코나 다른 연락처로 연락 갈 수 있도록 기능 추가

                page = page + 1
                sleep(0.1)

        if os.path.isfile('/news_json_file/' + date + '.txt'):
            beforeData = json.loads(NewsDataToFile.readFile(date))
            beforeCount = int(beforeData['newsCount'])
            returnData = self.changeNewsNum(returnData, addedNum= True)
            for i in range(returnData['newsCount']):
                beforeData["articles"][beforeCount + i + 1] = returnData['articles'][i + 1]
            beforeData['newsCount'] = beforeCount + returnData['newsCount']
            return json.dumps(self.changeNewsNum(beforeData), ensure_ascii=False, indent='\t')

        else:
            return json.dumps(self.changeNewsNum(returnData), ensure_ascii=False, indent='\t')

        #todo: 파일 존재 시 기존 파일에 이어서 저장하는 기능 -> 체크하기
import requests
import json
import re
from collections import OrderedDict
import pprint
from time import sleep
from bs4 import BeautifulSoup as bs

date = '20230414'


mainUrl = 'https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid2=258&sid1=101&date=' + date + '&page='
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Whale/3.19.166.16 Safari/537.36'
}

def getSoup(urlString):
    mainPage = requests.get(urlString, headers=headers)
    return bs(mainPage.content, "html.parser")

def getNewsTitlesAndUrlHTMLArray(newses):
    for news in newses:
        tempSoup = bs(str(news), "html.parser")
        if tempSoup.getText() == '' or tempSoup.find('img'):
            newses.remove(news)
    # newses = [str(news).strip('\n\t') for news in newses]
    return newses

def findTitleUrl(data):
    returnData = []
    for tag in data:
        tempSoup = bs(str(tag), 'html.parser')
        returnData.append([tempSoup.getText(), tempSoup.find('a')['href']])
    return returnData

def getNewsWriter(contents):
    arr = []

    for el in contents.find_all('span', 'writing'):
        arr.append(el.get_text().strip())
    print(arr)
    print(len(arr))
    return arr

def returnJsonData():
    page = 1
    returnData = {'date': date,
                  'newsCount': 0,
                  'articles': {}}
    while True:
        soup = getSoup(mainUrl + str(page))
        pageNum = soup.select_one('div.paging').find('strong').getText()

        if str(page) != pageNum:
            break
        else:
            print('page: ' + pageNum)

            newses = soup.select_one('div.newsflash_body').find_all('a')
            data = getNewsTitlesAndUrlHTMLArray(newses)
            newsData = findTitleUrl(data)

            contents = soup.select_one('div.list_body')
            writer = getNewsWriter(contents)
            # print('aasd', data[0])

            if len(newsData) == len(writer):
                for i in range(len(newsData)):
                    returnData['newsCount'] += 1
                    returnData['articles'][returnData['newsCount']] = {'title': re.sub('\s+',' ',newsData[i][0]),
                                                                       'url': re.sub('\s+',' ',newsData[i][1]),
                                                                       'writer': writer[i]}
            else:
                pass  # todo: 오류 발생 시 디코나 다른 연락처로 연락 갈 수 있도록 기능 추가

            page = page + 1
            sleep(0.1)

    return json.dumps(returnData, ensure_ascii=False, indent='\t')

if __name__ == '__main__':
    print(returnJsonData())

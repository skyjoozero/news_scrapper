import requests
import json
from collections import OrderedDict
import pprint
from time import sleep
from bs4 import BeautifulSoup as bs

date = '20230412'


mainUrl = 'https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid2=258&sid1=101&date=' + date + '&page='
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Whale/3.19.166.16 Safari/537.36'
}

def getSoup(urlString):
    mainPage = requests.get(urlString, headers=headers)
    return bs(mainPage.content, "html.parser")

def getNewsTitles(contents):
    arr = []

    for el in contents.find_all('a'):
        arr.append(el.get_text().strip())
    arr = [x for x in arr if (x != '' and x != '동영상기사')]

    return arr
def getNewsUrls(contents):
    arr = []

    for el in contents.find_all('a'):
        arr.append(el['href'])
    arr = list(dict.fromkeys(arr))

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
            page = page + 1
            sleep(0.1)

        contents = soup.select_one('div.list_body')
        titles = getNewsTitles(contents)
        urls = getNewsUrls(contents)
        if (len(titles) == len(urls)):
            for i in range(len(titles)):
                returnData['newsCount'] += 1
                returnData['articles'][returnData['newsCount']] = {'title': titles[i],
                                          'url': urls[i]}
        else:
            pass #todo: 오류 발생 시 디코나 다른 연락처로 연락 갈 수 있도록 기능 추가

    return json.dumps(returnData, ensure_ascii=False, indent='\t')

if __name__ == '__main__':
    print(returnJsonData())

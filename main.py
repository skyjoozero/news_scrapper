import requests
import json
from collections import OrderedDict
import pprint
from time import sleep
from bs4 import BeautifulSoup as bs

date = '20230414'
page = 1

main_url = 'https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid2=258&sid1=101&date=' + date +'&page='
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Whale/3.19.166.16 Safari/537.36'
}

# contents = soup.select_one('td.content').find_all('a')
# page_num = soup.select_one('div.paging').find('strong').getText()

def get_soup(url_string):
    main_page = requests.get(url_string, headers=headers)
    return bs(main_page.content, "html.parser")

def getNewsTitles(contents):
    arr = []

    for el in contents.find_all('a'):
        arr.append(el.get_text().strip())

    return arr
def getNewsUrls(contents):
    arr = []

    for content in contents:
        tempSoup = bs(str(content), "html.parser")
        arr.append(tempSoup.find('a')['href'])

    return arr

if __name__ == '__main__':

    while True:
        soup = get_soup(main_url + str(page))
        page_num = soup.select_one('div.paging').find('strong').getText()

        contents = soup.select_one('div.list_body')
        titles = getNewsTitles(contents)

        contents = soup.find_all('dt', 'photo')
        urls = getNewsUrls(contents)

        if str(page) != page_num:
            break
        else:
            print(page)
            page = page + 1
            sleep(0.1)
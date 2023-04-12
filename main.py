import requests
import pprint
from time import sleep
from bs4 import BeautifulSoup as bs

date = '20230412'
page = 1

main_url = 'https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid2=258&sid1=101&date=' + date +'&page='
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Whale/3.19.166.16 Safari/537.36'
}

# contents = soup.select_one('td.content').find_all('a')
# page_num = soup.select_one('div.paging').find('strong').getText()

while True:
    url = main_url + str(page)

    main_page = requests.get(url, headers=headers)
    soup = bs(main_page.content, "html.parser")

    # contents = soup.select_one('td.content').find_all('a')
    page_num = soup.select_one('div.paging').find('strong').getText()

    if str(page) != page_num:
        break
    else:
        print(page)
        page = page + 1
        sleep(0.1)

# pprint.pprint(page_num)
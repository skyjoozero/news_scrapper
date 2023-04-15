from GetNewsData import *
from NewsDataToFile import NewsDataToFile

if __name__ == '__main__':
    date = '20230416'
    scrapper = GetNewsData()
    NewsDataToFile.writeFile(date, scrapper.getNewsJsonData(date))
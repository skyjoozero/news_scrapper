from GetNewsData import *
from NewsDataToFile import *

if __name__ == '__main__':
    date = '20230412'
    scrapper = GetNewsData()
    NewsDataToFile.NewsDataFile.writeFile(date, scrapper.getNewsJsonData(date))
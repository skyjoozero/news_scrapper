from GetNewsData import *
from NewsDataToFile import NewsDataToFile
from CheckDate import CheckDate
from datetime import datetime, timedelta

def findNewsDuringDate(startYear, startMonth, startDay, lastYear, lastMonth, lastDay):
    '''

    :param startYear: string
    :param startMonth: string
    :param startDay: string
    :param lastYear: string
    :param lastMonth: string
    :param lastDay: string
    :return: None

    '''


    while True:
        scrapper = GetNewsData()
        startDate = datetime(startYear, startMonth, startDay, 0, 0, 0)
        lastDate = datetime(lastYear, lastMonth, lastDay + 1, 0, 0, 0)
        if((lastDate - startDate).days >= 1):
            print((lastDate - startDate).days, '--------------------------------------------------------------------------------------------------')
            if CheckDate.checkDateValid(startYear, startMonth, startDay):
                date = str(startYear).zfill(4) + str(startMonth).zfill(2) + str(startDay).zfill(2)
                NewsDataToFile.writeFile(date, scrapper.getNewsJsonData(date))
            else:
                if startDay > 31:
                    startDay = 0
                    startMonth += 1
                if startMonth > 12:
                    startMonth = 1
                    startDay = 0
        else:
            break
        startDay += 1
        del scrapper


if __name__ == '__main__':
    date = '20230416'
    findNewsDuringDate(2023, 4, 14, 2023, 4, 16)
    # scrapper = GetNewsData()
    # NewsDataToFile.writeFile(date, scrapper.getNewsJsonData(date))
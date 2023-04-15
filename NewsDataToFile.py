import json
import pprint

class NewsDataToFile():
    # def __init__(self, date):
    #     self.date = date

    @staticmethod
    def readFile(date):
        with open('news_json_file/' + date + '.txt', "r", encoding= 'utf-8') as fileData:
            return fileData.read()

    @staticmethod
    def writeFile(date, data):
        with open('news_json_file/' + date + '.txt', "w", encoding= 'utf-8') as fileData:
            pprint.pprint(data)
            fileData.write(data)
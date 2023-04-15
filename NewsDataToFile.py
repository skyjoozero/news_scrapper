import json
import pprint

class NewsDataFile():
    # def __init__(self, date):
    #     self.date = date

    def readFile(self):
        pass

    @staticmethod
    def writeFile(date, data):
        with open('news_json_file/' + date + '.txt', "w", encoding= 'utf-8') as fileData:
            pprint.pprint(data)
            fileData.write(data)
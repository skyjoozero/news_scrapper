import time
import copy
from MyUtil.FileIo import FileIo
from Tockenization.FindTocken import FindTocken
import json

class MakeTockenFile():
    fileIo = FileIo()
    tockenFinder = FindTocken()
    temp = []
    titles = []

    def makeFile(self, date):
        tockenJsonData = json.loads(self.tockenFinder.getDate(date))
        tockenJson = tockenJsonData['words'].keys()
        newsesJsonData = json.loads(self.fileIo.readFile(date))
        newsesJson = newsesJsonData['articles']
        for word in tockenJson:
            tempInt = 1
            for i in range(int(newsesJsonData['newsCount'])):
                if word in newsesJson[str(i + 1)]['title']:
                    tockenJsonData['words'][word]['articles'][str(tempInt)] = newsesJson[str(i + 1)]
                    tockenJsonData['words'][word]['wordCount'] = tempInt
                    tempInt += 1
                    # tockenJsonData['words'][word]['articles'].append(newsesJson[str(i + 1)])

        self.fileIo.writeInfoFile(date, json.dumps(tockenJsonData, ensure_ascii=False, indent='\t'))
        # for keys in tockenJson:
        #     print(keys)

        # for i in range(int(jsonData['newsCount'])):
        #     jsonData['articles'][str(i + 1)]['title']
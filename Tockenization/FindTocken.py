from konlpy.tag import Okt
from konlpy.tag import Kkma
from konlpy.tag import Komoran
from MyUtil.FileIo import FileIo
import json
import itertools

okt = Okt()
kkma = Kkma()
komoran = Komoran()

class FindTocken():

    fileIo = FileIo()

    def setDate(self, date):
        '''
        :param date: date string "YYYYMMDD"
        :return:
        '''
        data = self.fileIo.readFile(date)
        jsonData = json.loads(data)
        temp = []
        wordsCount = {}
        for i in range(int(jsonData['newsCount'])):
            temp.append(list(okt.nouns(jsonData['articles'][str(i + 1)]['title'])))

        temp = sum(temp, [])
        #todo

        for i in range(len(temp)):
            if temp[i] in wordsCount:
                wordsCount[temp[i]] += 1
            else:
                wordsCount[temp[i]] = 1

        print(wordsCount)
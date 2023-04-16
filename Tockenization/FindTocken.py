from konlpy.tag import Okt
from MyUtil.FileIo import FileIo
import json

class FindTocken():

    fileIo = FileIo()
    okt = Okt()

    def getDate(self, date):
        '''
        :param date: date string "YYYYMMDD"
        :return: json obj tocken info
        '''
        data = self.fileIo.readFile(date)
        jsonData = json.loads(data)
        temp = []
        wordsCount = {'mostCounted': 0,
                      'words': {}}
        for i in range(int(jsonData['newsCount'])):
            temp.append(list(self.okt.nouns(jsonData['articles'][str(i + 1)]['title'])))

        temp = sum(temp, [])
        #todo

        for i in range(len(temp)):
            if temp[i] in wordsCount['words']:
                wordsCount['words'][temp[i]]['wordCount'] += 1
                if wordsCount['words'][temp[i]]['wordCount'] > wordsCount['mostCounted']:
                    wordsCount['mostCounted'] = wordsCount['words'][temp[i]]['wordCount']
            else:
                wordsCount['words'][temp[i]] = {'wordCount': 1,
                                                'articles': {}}

        return json.dumps(wordsCount, ensure_ascii=False, indent='\t')
import sys

class FileIo():
    def __init__(self):

        if sys.platform.startswith('win'):
             self.news_path = 'news_json_flie/'
             self.tocken_path = 'tocken_json_file/'
        else:
            self.news_path = '/home/ubuntu/news_scrapper/news_json_file'
            self.tocken_path = '/home/ubuntu/news_scrapper/tocken_json_file'

    def readFile(self, date):
        '''
        :param date: date string "YYYYMMDD"
        :return: json formatted string
        '''
        with open(self.news_path + str(date) + '.txt', "r", encoding= 'utf-8') as fileData:
            return fileData.read()

    def readInfoFile(self, date):
        '''
        :param date: date string "YYYYMMDD"
        :return: json formatted string
        '''
        with open(self.tocken_path + date + '_tocken.txt', "r", encoding='utf-8') as fileData:
            return fileData.read()

    def writeFile(self, date, data):
        '''
        :param date: date string "YYYYMMDD"
        :param data: json formatted string
        :return: None
        '''
        with open(self.news_path + date + '.txt', "w", encoding= 'utf-8') as fileData:
            fileData.write(data)

    def writeInfoFile(self, date, data):
        '''
        :param date: date string "YYYYMMDD"
        :param data: json formatted string
        :return: None
        '''
        with open(self.tocken_path + date + '_tocken.txt', "w", encoding='utf-8') as fileData:
            fileData.write(data)

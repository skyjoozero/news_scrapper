class FileIo():
    # def __init__(self, date):
    #     self.date = date

    @staticmethod
    def readFile(date):
        '''
        :param date: date string "YYYYMMDD"
        :return: json formatted string
        '''
        with open('news_json_file/' + date + '.txt', "r", encoding= 'utf-8') as fileData:
            return fileData.read()

    @staticmethod
    def writeFile(date, data):
        '''
        :param date: date string "YYYYMMDD"
        :param data: json formatted string
        :return: None
        '''
        with open('news_json_file/' + date + '.txt', "w", encoding= 'utf-8') as fileData:
            fileData.write(data)
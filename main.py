from NewsClasses.GetNewsData import *
from Tockenization.FindTocken import FindTocken

if __name__ == '__main__':
    date = '20230416'
    finder = FindTocken()
    finder.setDate(date)
    # scrapper = GetNewsData()
    # scrapper.findNewsDuringDate(2023, 4, 16, 2023, 4, 16)
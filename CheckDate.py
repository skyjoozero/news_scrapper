import datetime

class CheckDate():

    @staticmethod
    def checkDateValid(year, month, day):
        try:
            data = datetime.datetime(int(year), int(month), int(day))
            return True
        except ValueError:
            return False
import asyncio

from NewsClasses.GetNewsData import *
from MyUtil.FileIo import FileIo
from Tockenization.MakeTockenFile import MakeTockenFile
from TelegramBot.TelegramSender import TelegramSender

if __name__ == '__main__':
    chatBot = TelegramSender()
    newsGetter = GetNewsData()
    fileReader = FileIo()
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    try:
        date = datetime.now()
        year = date.strftime('%Y')
        month = date.strftime('%m')
        day = date.strftime('%d')
        print(year, month, day)

        newsData = newsGetter.findNewsDuringDate(int(year), int(month), int(day), int(year), int(month), int(day))

        finder = MakeTockenFile()
        finder.makeFile(year + month + day)

        chatBot = TelegramSender()

        jsonData = json.loads(fileReader.readInfoFile(year + month + day))
        mostCount = int(jsonData['mostCounted'])

        sendCount = 0
        for key in jsonData['words'].keys():
            # print(key)
            if jsonData['words'][key]['wordCount'] == mostCount:
                for i in range(mostCount):
                    asyncio.run(chatBot.main(key + '' + json.dumps(jsonData['words'][key]['articles'], ensure_ascii=False, indent='\t')))
                    sendCount += 1
                if sendCount >= 5:
                    break

            mostCount -= 1




            # asyncio.run(chatBot.main())

    except BaseException as e:
        print(e)
        asyncio.run(chatBot.main(str(e)))
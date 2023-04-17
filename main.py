import asyncio
import sys
from NewsClasses.GetNewsData import *
from MyUtil.FileIo import FileIo
from Tockenization.MakeTockenFile import MakeTockenFile
from TelegramBot.TelegramSender import TelegramSender

if __name__ == '__main__':
    chatBot = TelegramSender()
    newsGetter = GetNewsData()
    fileReader = FileIo()
    py_ver = int(f"{sys.version_info.major}{sys.version_info.minor}")
    if py_ver > 37 and sys.platform.startswith('win'):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

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
    print(jsonData['mostCounted'])
    mostCount = jsonData['mostCounted']


    sendCount = 0
    while True:
        for key in jsonData['words'].keys():
            print(key)
            if jsonData['words'][key]['wordCount'] == mostCount:
                print(jsonData['words'][key]['wordCount'], mostCount)
                msg = key + '(' + str(mostCount) + ')'  + json.dumps(jsonData['words'][key]['articles'], ensure_ascii=False, indent='\t')
                # print(msg)
                msgs = [msg[i:i + 4096] for i in range(0, len(msg), 4096)]
                for text in msgs:
                    try:
                        asyncio.run(chatBot.main(text))
                    except BaseException as e:
                        print(e)
                        asyncio.run(chatBot.main(str(e)))
                    sleep(1)
                sendCount += 1
        mostCount -= 1

        if sendCount >= 5:
            break

        #asyncio.run(chatBot.main())



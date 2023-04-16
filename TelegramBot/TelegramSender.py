import json

import telegram

class TelegramSender():

    token = "6111176148:AAEz0Kj_7JzMyFhRREthyq_g4gElNZvKqMI"  # token 번호 - telegram 채팅창당 1개
    bot = telegram.Bot(token)

    async def main(self, string):
        await self.bot.sendMessage(chat_id=1615871192, text=string)  # chat id - telegram 계정당 1개


import discord

class MyDiscordBot(discord.Client):
    async def on_ready(self):
        print(f'logged on {self.user}')
        
    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

if __name__ == '__main__':
    client = MyDiscordBot()
    client.run('MTEwMTM3NzAzNDgyNDk3NDQwOA.G_Dkg0.daSP7vhj7oy_GfUB540MkRIKnji6fD2y5evUuM')
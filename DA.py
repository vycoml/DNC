import discord
import os

client = discord.Client()

@client.event
async def on_ready():
 print('start')


@client.event
async def on_message(message):
    if message.content.startswith('!도움말'):
        if message.content.startswith('!도움말'):
            embed = discord.Embed(title="DN봇 도움말",
                                  description="!답변채택 <유저> : <유저>의 내공을 올립니다.\n!내공확인 <유저> : 유저>의 내공을 확인합니다.\n!내공순위 : 서버의 내공 순위를 확인합니다.\n!명령어추가 : DN봇의 명령어를 추가합니다.\n!명령어삭제 : DN봇의 명령어를 삭제합니다.\n!명령어추가횟수 <유저> : DN봇의 명령어를 추가한 횟수를 확인합니다.\n!명령어추가순위 : DN봇의 명령어를 추가한 횟수를 확인합니다.",
                                  color=0x72ab49)

            embed.set_footer(text="만든이 : 기화#9547")

            await message.channel.send(embed=embed)

        
        
access_token
client.run('NTg0NTg4NTI2NzY3NTcwOTY0.XPistQ.G63T4rJgsA0zi1pbxLzhUe2n9i4')

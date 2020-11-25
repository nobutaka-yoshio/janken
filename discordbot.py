# インストールした discord.py を読み込む
import discord
import random
import asyncio

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'Nzc5OTg5ODE2ODUwMjUxNzk3.X7okHw.OrX96-McjoMWFobX7sZrzK93s2U'
arr = ['ぐー:punch:', 'ちょき:v:', 'ぱー:hand_splayed:']
# 接続に必要なオブジェクトを生成
client = discord.Client()


# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return

    if message.content == 'じゃんけん':
        await message.channel.send(message.author.mention+" は「"+random.choice(arr)+"」を出しました。")


# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
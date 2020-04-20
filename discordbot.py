from discord.ext import commands
import discord
import os
import sympy

TOKEN = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()

# インストールした discord.py を読み込む
import discord

# 起動時に動作する処理
@client.event
async def on_ready():
  channel = client.get_channel(const.channel_id['bot_control'])
  # 起動したらターミナルにログイン通知が表示される
  print('投稿削除サーバー')
  await channel.send('投稿削除サーバー起動')
  return

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
  if message.name == "bot_control":
    if message.content == "delete":
      if message.author.bot:
        return
      if message.channel.name == 'bot_control':
        return
      if message.channel.name == '一般':
        return
      if message.channel.name == 'ルール':
        return
      if message.channel.name == '対戦a実況':
        return
      if message.channel.name == '対戦b実況':
        return
      await message.channel.purge()
      print('投稿削除しました。')

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)

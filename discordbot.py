from discord.ext import commands
import discord
import os

TOKEN = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()

@client.event
async def on_ready():
  channel = client.get_channel(701731353783304225)
  await channel.send('投稿削除サーバー起動')
  return

@client.event
async def on_message(message):
  channel = client.get_channel(701731353783304225)
  if message.content = "delete":
    await channel.send("削除を開始します")
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
    await channel.send("完了しました")
    return

client.run(TOKEN)

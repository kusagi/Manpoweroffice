import discord
from discord.ext import commands
import os

app = commands.Bot(command_prefix='+')

@app.event
async def on_ready():
    print(app.user.name, 'has cnnected to Discord!')
    await app.change_presence(status=discord.Status.online, activity=None)
    print("ready")

@app.command()
async def 신고(ctx, *, text):
    await ctx.channel.purge(limit=1)
    await app.get_channel(813741144093360158).send(f'신고자:{ctx.author.mention}/신고내용:{text}')


access_token = os.environ['BOT_TOKEN']
app.run(access_token)

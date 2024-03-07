import discord
from discord.ext import commands
import get_model

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def image(ctx):
    err = ''
    img_form = ['png','jpg','jpeg']
    if ctx.message.attachments != []:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            format = file_name.split('.')[1]
            if format not in img_form:
                await ctx.send('Что то пошло не так...')
                return
            await attachment.save(file_name)
            await ctx.send('Вы сохранили файл')
            err = get_model.classife_image(file_name)
            if err == '':
                await ctx.send('')
            else:
                await ctx.send(err)
bot.run('YOUR TOKEN')

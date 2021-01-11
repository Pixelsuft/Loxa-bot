#Pixelsuft Loxa Bot
print('Starting Loxa Bot...')

#imports
from os import environ as env
from os import name as os_type
from os import system as cmd_run
from os import listdir as scan_dir
from colorama import init as colorama_init
from colorama import Back, Fore, Style
from ctypes import windll as windows_dll
from random import randint as random
from discord.ext import commands
from discord.utils import get
from discord import Status as discord_status
from discord import Game as discord_game
from discord import File as discord_file
from discord import Embed as discord_embed
from discord import channel as discord_channel
from subprocess import check_output as cmd_run_with_log
from io import BytesIO
from PIL import Image as pillow_image
from PIL import ImageFilter as pillow_filter
from requests import get as request_get


#set up
windows_dll.kernel32.SetConsoleTitleW("Loxa Bot") #Console title
back_no_fore=False #log, Error, Warning colors to back or fore?
prefix='!!'
error_text='ашипка404'
author_mention='<@!451310273438023681>'
bot_mention='<@!775611736703238144>'
user_images={}
ctrl_c_is_exit=True
game_status='Loxa Bot | '+str(prefix)+'help'
if os_type=='nt': #Only if os is windows
    cmd_run('color 0a') #Change color to matrix XD
colorama_init(autoreset=True)


#log, Error, Warning
def log(string_to_log):
    if back_no_fore==False:
        print(Fore.WHITE + "[Log]" + Style.RESET_ALL + ": " + str(string_to_log) + ";")
    else:
        print(Back.WHITE + Fore.BLACK + "[Log]" + Style.RESET_ALL + ": " + str(string_to_log) + ";")
def error(string_to_error):
    if back_no_fore==False:
        print(Fore.RED + "[Error]" + Style.RESET_ALL + ": " + str(string_to_error) + ";")
    else:
        print(Back.RED + Fore.BLACK + "[Error]" + Style.RESET_ALL + ": " + str(string_to_error) + ";")
def warn(string_to_warn):
    if back_no_fore==False:
        print(Fore.YELLOW + "[Warning]" + Style.RESET_ALL + ": " + str(string_to_warn) + ";")
    else:
        print(Back.YELLOW + Fore.BLACK + "[Warning]" + Style.RESET_ALL + ": " + str(string_to_warn) + ";")

#get token from environ
discord_bot_token=''
try:
    discord_bot_token=env['__DISCORD_BOT_TOKEN']
except KeyError:
    error('__DISCORD_BOT_TOKEN')


#main code starts
client = commands.Bot(command_prefix = prefix)
client.remove_command('help')


@client.event
async def on_ready():
    log("Pixelsuft Loxa Bot (Public) Started!")
    await client.change_presence( status = discord_status.online, activity = discord_game(game_status) )


@client.event
async def on_message(message):
    if not message.author.mention==bot_mention:
        ctx = await client.get_context(message)

        await client.process_commands(message)


@client.command(pass_context=True)
async def run_cmd(ctx, *, command_to_run):
    if ctx.message.author.mention==author_mention:
        result=''
        try:
            result=cmd_run(command_to_run)
        except:
            result=error_text
        await ctx.send(result)


@client.command(pass_context=True)
async def log_cmd(ctx, encode, *, command_to_run):
    if ctx.message.author.mention==author_mention:
        result=''
        try:
            result=cmd_run_with_log(command_to_run, shell=True, encoding=encode)
        except:
            result=error_text
        await ctx.send(result)


@client.command(pass_content=True)
async def imaginer(ctx,*,args_str):
    args=args_str.split(' ')
    await ctx.send('PixelSuft imaginer v1.0')
    if args[0]=='open':
        if not ctx.message.attachments:
            await ctx.send(error_text+': Не прикреплён файл!')
        else:
            response = request_get(ctx.message.attachments[0].url)
            user_images[str(ctx.message.author.id)] = pillow_image.open(BytesIO(response.content))
            await ctx.send('Файл открыт!')
    elif args[0]=='open_url':
        response = request_get(args[1])
        user_images[str(ctx.message.author.id)] = pillow_image.open(BytesIO(response.content))
    elif args[0]=='rotate':
        try:
            user_images[str(ctx.message.author.id)] = user_images[str(ctx.message.author.id)].rotate(int(args[1]))
        except:
            await ctx.send(error_tex)
    elif args[0]=='crop':
        try:
            user_images[str(ctx.message.author.id)] = user_images[str(ctx.message.author.id)].crop((int(args[1]),int(args[2]),int(args[3]),int(args[4])))
        except:
            await ctx.send(error_text)
    elif args[0]=='filter':
        try:
            user_images[str(ctx.message.author.id)] = user_images[str(ctx.message.author.id)].filter(eval('pillow_filter.'+str(args[1])))
        except:
            await ctx.send(error_text)
    elif args[0]=='convert':
        try:
            user_images[str(ctx.message.author.id)] = user_images[str(ctx.message.author.id)].convert(str(args[1]))
        except:
            await ctx.send(error_text)
    elif args[0]=='resize':
        try:
            user_images[str(ctx.message.author.id)] = user_images[str(ctx.message.author.id)].resize((int(args[1]), int(args[2])), pillow_image.ANTIALIAS)
        except:
            await ctx.send(error_text)
    elif args[0]=='size':
        try:
            img_width,img_height=user_images[str(ctx.message.author.id)].size
            await ctx.send('Ширина: '+str(img_width)+'\nВысота: '+str(img_height))
        except:
            await ctx.send(error_text)
    elif args[0]=='random':
        scanned=scan_dir('random_img')
        randomed='random_img\\'+scanned[random(0,len(scanned)-1)]
    elif args[0]=='show':
        with BytesIO() as output:
            try:
                user_images[str(ctx.message.author.id)].save(output, format=args[1].upper())
                output.seek(0)
                contents = output.getvalue()
                await ctx.message.channel.send(file=discord_file(fp=output, filename='zalupa.'+args[1]))
            except:
                await ctx.send(error_text+': Ошибка')
    elif args[0]=='help':
        try:
            if args[1]=='crop':
                await ctx.send(prefix+'imaginer crop X1 Y1 X2 Y2')
            elif args[1]=='rotate':
                await ctx.send(prefix+'imaginer rotate ГРАДУС')
            elif args[1]=='filter':
                await ctx.send(prefix+'''imaginer filter ФИЛЬТР
                Фильтры:
                BLUR BoxBlur BuiltinFilter CONTOUR Color3DLUT DETAIL EDGE_ENHANCE EDGE_ENHANCE_MORE EMBOSS FIND_EDGES Filter GaussianBlur Kernel MaxFilter MedianFilter MinFilter ModeFilter MultibandFilter RankFilter SHARPEN SMOOTH SMOOTH_MORE UnsharpMask
                ''')
            elif args[1]=='resize':
                await ctx.send(prefix+'imaginer resize ШИРИНА ВЫСОТА')
            elif args[1]=='show':
                await ctx.send(prefix+'imaginer show ФОРМАТ')
            elif args[1]=='convert':
                await ctx.send(prefix+'''imaginer convert РЕЖИМ
                Режимы:
                1 (1-bit pixels, black and white, stored with one pixel per byte)
                L (8-bit pixels, black and white)
                P (8-bit pixels, mapped to any other mode using a color palette)
                RGB (3x8-bit pixels, true color)
                RGBA (4x8-bit pixels, true color with transparency mask)
                CMYK (4x8-bit pixels, color separation)
                YCbCr (3x8-bit pixels, color video format)
                LAB (3x8-bit pixels, the L*a*b color space)
                HSV (3x8-bit pixels, Hue, Saturation, Value color space)
                I (32-bit signed integer pixels)
                F (32-bit floating point pixels)
                ''')
        except:
            emb = discord_embed(title = 'Помощь по Imaginer ('+str(prefix)+'imaginer КОМАНДА)',color = 0x00ff00)
            emb.add_field(name='help', value = "Открытие этой подсказки")
            emb.add_field(name='open', value = "Открыть изображение")
            emb.add_field(name='open_url', value = "Открыть изображение по url")
            emb.add_field(name='show', value = "Показать изображение")
            emb.add_field(name='crop', value = "Обрезать изображение")
            emb.add_field(name='rotate', value = "Повернуть изображение")
            emb.add_field(name='filter', value = "Наложить фильтр на изображение")
            emb.add_field(name='size', value = "Показать размер изображения")
            emb.add_field(name='resize', value = "Изменить размер изображения")
            emb.add_field(name='convert', value = "Конвертировать изображение")
            await ctx.send( embed = emb )



if __name__=='__main__':
    while True: #For Ctrl+C
        try:
            log('Loading Main Loop...')
            client.run(discord_bot_token)
            break #This is not Ctrl+C, break while
        except KeyboardInterrupt: #Ctrl+C now restart app
            print('\nKeyBoard Interrupt')
            if ctrl_c_is_exit==True:
                break

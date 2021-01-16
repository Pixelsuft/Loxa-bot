#Pixelsuft Loxa Bot
print('Starting Loxa Bot...')

#imports
from os import environ as env
from os import name as os_type
from os import system as cmd_run
from os import listdir as scan_dir
from colorama import init as colorama_init
from colorama import Back, Fore, Style
from random import randint as random
from random import choice as random_choice
from discord.ext import commands
from discord.utils import get
from discord import Status as discord_status
from discord import Game as discord_game
from discord import File as discord_file
from discord import Embed as discord_embed
from discord import channel as discord_channel
from discord import Color as discord_color
from subprocess import check_output as cmd_run_with_log
from io import BytesIO
from PIL import Image as pillow_image
from PIL import ImageFilter as pillow_filter
from requests import get as request_get
from asyncio import sleep as async_time_sleep
from time import monotonic as time_monotonic


#set up
back_no_fore=False #log, Error, Warning colors to back or fore?
prefix='!!'
error_text='ашипка404'
author_mention='<@!451310273438023681>'
bot_mention='<@!775611736703238144>'
user_images={}
troll_delete=False
enable_rainbow=True
loha_chat=['lox', 'loxa', 'лох', 'лоха', 'лохабот', 'боталох', 'loxabot', 'loxa_bot', 'loxa-bot', 'лох!', 'лоха!']
ctrl_c_is_exit=True
game_status='Loxa Bot | '+str(prefix)+'help'
if os_type=='nt': #Only if os is windows
    from ctypes import windll as windows_dll
    windows_dll.kernel32.SetConsoleTitleW("Loxa Bot") #Console title
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


colours_rainbow = [0x00ff00,discord_color.dark_orange(),discord_color.orange(),discord_color.dark_gold(),discord_color.gold(),discord_color.dark_magenta(),discord_color.magenta(),discord_color.red(),discord_color.dark_red(),discord_color.blue(),discord_color.dark_blue(),discord_color.teal(),discord_color.dark_teal(),discord_color.green(),discord_color.dark_green(),discord_color.purple(),discord_color.dark_purple()]
serverid_rainbow = 753488286978277389
rainbowrolename = "Наркоман"
rainbow_delay=5


async def rainbowrole(role):
    for role in client.get_guild(serverid_rainbow).roles:
        if str(role) == str(rainbowrolename):
            log("Detected role")
            while not client.is_closed():
                try:
                    await role.edit(color=random_choice(colours_rainbow))
                except Exception:
                    pass
                await async_time_sleep(rainbow_delay)
    try:
        await client.get_guild(serverid_rainbow).create_role(reason="Created rainbow role", name=rainbowrolename)
        await async_time_sleep(2)
        client.loop.create_task(rainbowrole(rainbowrolename))
    except Exception as e:
        error(e)
        pass
        await async_time_sleep(10)
        client.loop.create_task(rainbowrole(rainbowrolename))


@client.event
async def on_ready():
    log("Pixelsuft Loxa Bot (Public) Started!")
    if enable_rainbow==True:
        client.loop.create_task(rainbowrole(rainbowrolename))
    log(client.user.name)
    log(client.user.id)
    await client.change_presence(status = discord_status.online, activity = discord_game(game_status))


@client.event
async def on_message(message):
    if not message.author.mention==bot_mention:
        if troll_delete==True:
            if not message.author.mention==author_mention:
                await message.delete()
        else:
            ctx = await client.get_context(message)
            split_cmd=message.content.lower().replace('!','').replace('?','').replace(',','').split(' ')
            if split_cmd[0].lower() in loha_chat:
                if len(split_cmd)<=1:
                    await ctx.send('Привет, '+message.author.mention+', я Лоха Бот!')
                else:
                    entered=False
                    hello_words=['привет', 'хай', 'хеллоу', 'прив', 'здрасьте', 'дарова', 'даров', 'драсьте']
                    for i in split_cmd:
                        if entered==True:
                            break
                        else:
                            if i in hello_words:
                                entered=True
                                await ctx.send('Привет тебе, '+message.author.mention+'!')
        await client.process_commands(message)


@client.command(pass_context=True) # Only for creator
async def run_cmd(ctx, *, command_to_run):
    if ctx.message.author.mention==author_mention:
        result=''
        try:
            result=cmd_run(command_to_run)
        except:
            result=error_text
        await ctx.send(result)
    else:
        await ctx.send('А хер тебе с маслом!')


@client.command(pass_context=True) # Only for creator
async def log_cmd(ctx, encode, *, command_to_run):
    if ctx.message.author.mention==author_mention:
        result=''
        try:
            result=cmd_run_with_log(command_to_run, shell=True, encoding=encode)
        except:
            result=error_text
        await ctx.send(result)
    else:
        await ctx.send('А хер тебе с маслом!')


@client.command(pass_context=True)
async def string(ctx, *, args_str):
    cmd=args_str.split(' ')
    if cmd[0]=='old_rsplit':
        full=''
        for i in range(len(cmd)):
            if not i==0:
                if not full=='':
                    full+=' '
                full+=cmd[i]
        for i in full:
            await ctx.send(i)
    elif cmd[0]=='rsplit':
        full=''
        fuller=''
        for i in range(len(cmd)):
            if not i==0:
                if not full=='':
                    full+=' '
                full+=cmd[i]
        for i in full:
            if not fuller=='':
                fuller+='\n'
            fuller+=i
        await ctx.send(fuller)
    elif cmd[0]=='old_split':
        full=''
        for i in range(len(cmd)):
            if not i==0 and not i==1:
                if not full=='':
                    full+=' '
                full+=cmd[i]
        for i in full.split(cmd[1]):
            await ctx.send(i)
    elif cmd[0]=='split':
        full=''
        fuller=''
        for i in range(len(cmd)):
            if not i==0 and not i==1:
                if not full=='':
                    full+=' '
                full+=cmd[i]
        for i in full.split(cmd[1]):
            if not fuller=='':
                fuller+='\n'
            fuller+=i
        await ctx.send(fuller)
    elif cmd[0]=='reverse':
        full=''
        for i in range(len(cmd)):
            if not i==0:
                if not full=='':
                    full+=' '
                full+=cmd[i]
        await ctx.send(full[::-1])
    elif cmd[0]=='random_choice_space':
        full=''
        for i in range(len(cmd)):
            if not i==0:
                if not full=='':
                    full+=' '
                full+=cmd[i]
        await ctx.send(str(random_choice(full.split(' '))))
    elif cmd[0]=='random_choice':
        full=''
        for i in range(len(cmd)):
            if not i==0:
                if not full=='':
                    full+=' '
                full+=cmd[i]
        await ctx.send(str(random_choice(full)))



@client.command(pass_context=True) # Only for creator
async def troll_delete(ctx):
    if ctx.message.author.mention==author_mention:
        global troll_delete
        if troll_delete==True:
            troll_delete=False
        else:
            troll_delete=True
    else:
        await ctx.send('А хер тебе с маслом!')


@client.command(pass_context=True) # Only for creator
async def set_status(ctx, status_type, *, game_status):
    if ctx.message.author.mention==author_mention:
        game_status=game_status
        new_status=discord_status.online
        if status_type=='dnd':
            new_status=discord_status.dnd
        elif status_type=='do_not_disturb':
            new_status=discord_status.do_not_disturb
        elif status_type=='idle':
            new_status=discord_status.idle
        elif status_type=='invisible':
            new_status=discord_status.invisible
        elif status_type=='offline':
            new_status=discord_status.offline
        elif status_type=='try_value':
            new_status=discord_status.try_value
        await client.change_presence(status = new_status, activity = discord_game(game_status))
    else:
        await ctx.send('А хер тебе с маслом!')


@client.command(pass_context=True)
async def ping(ctx):
    before = time_monotonic()
    message = await ctx.send("Понг блять!")
    ping = (time_monotonic() - before) * 1000
    await message.edit(content=f"Понг блять!\nПинг размером с {int(ping)}ms")


@client.command(pass_content=True)
async def imaginer(ctx,*,args_str):
    args=args_str.split(' ')
    await ctx.send('PixelSuft imaginer v1.0')
    if len(args)>1:
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
                emb = discord_embed(title = 'Помощь по Imaginer ('+str(prefix)+'imaginer КОМАНДА)',color = random_choice(colours_rainbow))
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
                await ctx.send(embed = emb)
    else:
        await ctx.send(ctx.message.author.mention+', для большей информации наберите '+str(prefix)+'imaginer help.')


if __name__=='__main__':
    while True: #For Ctrl+C
        try:
            log('Loading Main Loop...')
            client.run(discord_bot_token)
            break #This is not Ctrl+C, break while
        except KeyboardInterrupt: #Ctrl+C now restart app
            print('\n')
            if ctrl_c_is_exit==True:
                break  #Ctrl+C now close app

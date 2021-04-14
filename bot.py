import asyncio
import os
import discord
import random
from discord.utils import get
from discord.ext.commands import Bot, has_permissions


client = discord.Client()
intents = discord.Intents.default()
intents.members = True

#Bot token
TOKEN = 'ODMwNzg3Mzc3MzA3MTg5MjQ5.YHLxCg.JPbKkF2XWuBBcdr3EXI-g7hP3hk'
ping_bot = Bot(intents = intents, command_prefix= ".")


#bots designated channel for outputs
channel_name = "bot-output"


@ping_bot.command()
async def pozdrav_sa(ctx):
    await ctx.send("Hello! CYKA NUGGETS BLYAT @everyone IM ALIVE YA YEET")

@ping_bot.command()
async def dement(ctx):
    emoji_id = 806566749696426005
    await ctx.send(5*("<:shank:" + str(emoji_id) +"> "))
    await ctx.send("ČO SI TO DOVOLUJEŠ???")

#type a message into bots output channel, deletes authors msg request from chat afterwards
@ping_bot.command()
async def msg(ctx, *args):
    if (len(args) > 0):
        channel = discord.utils.get(ping_bot.guilds[0].text_channels, name=channel_name)
        await channel.send(' '.join([word for word in args]))
        await ctx.message.delete()

@ping_bot.command()
async def sad(ctx):
    role_id = 778638221982302229
    await ctx.send(5*("<:heartcat:" + str(806863011604201525) + "> "))

@ping_bot.command()
async def csko(ctx):
    role_id = 778638221982302229
    await ctx.send("<@&" + str(role_id) + "> jako som bot sice ale dal by som csko :)))")


#ID of the role who has the permission to use the command
perm_role_name = "KOKOT"
#Name of the channel where the bot will post the message
channel_name = "bot-output"
#ID of the role who you will be pinging
ping_role_id = 776551285209956393
@ping_bot.command()
async def ping_user(ctx, user: discord.Member, *args):
    #Channel where the bot will send the ping message
    channel = discord.utils.get(ping_bot.guilds[0].text_channels, name = channel_name)
    # channel = discord.client.get_channel(int(channel_id))
    member = ping_bot.get_user(user.id)

    #Check if user is admin or has the role for making a ping
    if (discord.utils.get(user.roles, name = perm_role_name) is not None or
    user.permissions_in(ctx.message.channel).manage_channels):
        if (len(args) > 0):
            txt = member.mention + " " + " ".join([word for word in args])
            await channel.send(txt)
        else:
            await ctx.send(ctx.message.author.mention + " please add a message you would like me to post.")
    else:
        text = "Sorry {}, you do not have the required permissions to do that!".format(ctx.message.author.mention)
        await ctx.send(text)

# drag_id = 581516615863238691
# trab_id = 309772903040155658
# @ping_bot.command()
# async def bet(ctx):
#     channel = discord.utils.get(ping_bot.guilds[0].text_channels, name = "commandy")

drag_id = 581516615863238691
@ping_bot.command()
async def spam_drag(ctx, num):
    channel = discord.utils.get(ping_bot.guilds[0].text_channels, name=channel_name)
    txt = "<@" + str(drag_id) + "> no čo, kedy ideme all in felak? Cítim v kostiach takú fajnovú zelenú ..."
    if (num.isdigit()):
        for x in range(int(num)): await channel.send(txt)

@ping_bot.command()
async def dm(ctx, name, *args):
    mem = find_mem(ctx, name)

    if (mem != None):
        member = ping_bot.get_user(mem.id)
        await member.send(' '.join([word for word in args]))
        try:
            await ctx.message.delete()
        except:
            pass
    else:
        await ctx.send("User not found! Please enter a valid name.")

#Direct Message a user several times
@ping_bot.command()
async def dmn(ctx, name, *args):
    mem = find_mem(ctx, name)

    if (mem != None):
        member = ping_bot.get_user(mem.id)
        if (len(args) == 0):
            await ctx.send(ctx.message.author + " please enter an amount and a message you want me to spam the user!")
        elif(args[0].isdigit()):
            if (len(args) > 1):
                for x in range(int(args[0])): await member.send(' '.join([word for word in args[1:]]))
            else: await ctx.send("{} please enter a message!".format(ctx.message.author.mention))
        else: await ctx.send("{} please enter an amount of messages you want me to spam!".format(ctx.message.author.mention))
        try:
            await ctx.message.delete()
        except:
            pass
    else:
        await ctx.send("User not found! Please enter a valid name.")

#Send "Ya like Jazz" gif
@ping_bot.command()
async def jazz(ctx):
    trish_id = 756031708473720864
    cwd = os.getcwd() + '\\pics\\jazz.gif'
    with open(cwd, 'rb') as file: pic = discord.File(file)
    await ctx.send("<@" + str(trish_id) + "> Ya like jaaaazzzz? :3")
    await ctx.send(file = pic)

#Send random cat girl picture
@ping_bot.command()
async def mnau(ctx):
    loc_path = '\\pics\\anime\\'
    cwd = os.getcwd() + loc_path
    pictures = [filenames for filenames in os.walk(cwd)][0][2]
    pic_path = cwd + str(random.choice(pictures))
    with open(pic_path, 'rb') as file:
        pic = discord.File(file)
    await ctx.send(file=pic)

#Send random cat girl picture into DMs
@ping_bot.command()
async def mnaudm(ctx, name):
    mem = find_mem(ctx, name)

    if (mem != None):
        member = ping_bot.get_user(mem.id)
        loc_path = '\\pics\\anime\\'
        cwd = os.getcwd() + loc_path
        pictures = [filenames for filenames in os.walk(cwd)][0][2]
        pic_path = cwd + str(random.choice(pictures))
        with open(pic_path, 'rb') as file:
            pic = discord.File(file)

        await member.send("Aha čo ti tvoj tajný ctiteľ {} chce poslať UwU :3".format(ctx.message.author.mention))
        await member.send(file=pic)
        try:
            await ctx.message.delete()
        except:
            pass
    else: await ctx.send("User not found! Please enter a valid name.")


@ping_bot.command()
@has_permissions(kick_members = True)
async def rape(ctx, *channel):
    chnl = find_vc(ctx, ' '.join([w for w in channel]))
    vc = get(ping_bot.voice_clients, guild = ctx.guild)
    if (vc and vc.is_connected()):
        await vc.move_to(chnl)
    else:
        vc = await chnl.connect()

    server = ctx.message.guild.voice_client

    cwd = os.getcwd() + "\\mp3\\earrape.mp3"
    voice_client: discord.VoiceClient = discord.utils.get(ping_bot.voice_clients, guild=ctx.guild)
    audio_source = discord.FFmpegPCMAudio(source = cwd)
    voice_client.play(audio_source, after=None)

    while voice_client.is_playing():
        await asyncio.sleep(1)
    await server.disconnect()

@ping_bot.command()
async def pitr(ctx, *channel):
    role = discord.utils.get(ctx.guild.roles, name="Matfyz")
    if (role not in ctx.message.author.roles):
        await ctx.send("Sorry {}, you do not have the permission to do that!".format(ctx.message.author.mention))
        return
    chnl = find_vc(ctx, ' '.join([w for w in channel]))
    vc = get(ping_bot.voice_clients, guild = ctx.guild)
    if (vc and vc.is_connected()):
        await vc.move_to(chnl)
    else:
        vc = await chnl.connect()

    server = ctx.message.guild.voice_client

    cwd = os.getcwd() + "\\mp3\\petrik\\"
    files = [filenames for filenames in os.walk(cwd)][0][2]
    audio = cwd + str(random.choice(files))

    voice_client: discord.VoiceClient = discord.utils.get(ping_bot.voice_clients, guild=ctx.guild)
    audio_source = discord.FFmpegPCMAudio(source = audio)
    voice_client.play(audio_source, after=None)

    while voice_client.is_playing():
        await asyncio.sleep(1)
    await server.disconnect()

#Return instance of Voice Channel with a given name
def find_vc(ctx, name):
    for vc in list(ctx.guild.voice_channels):
        if (name.lower() in vc.name.lower()): return vc
    return None

#Return user instance with a given name
def find_mem(ctx, name):
    for user in list(ctx.guild.members):
        if (name.lower() in user.name.lower()): return user
    return None



@ping_user.error
async def ping_error(ctx, error):
    if isinstance(error, discord.ext.commands.MissingPermissions):
        text = "Sorry {}, you do not have the required permissions to do that!".format(ctx.message.author.mention)
        await ctx.send(text)
    else:
        await ctx.send(error)

@rape.error
async def rape_error(ctx, error):
    if isinstance(error, discord.ext.commands.MissingPermissions):
        await ctx.send("Sorry {}, you do not have the permission to do that!".format(ctx.message.author.mention))
    else: ctx.send(error)


ping_bot.run(TOKEN)


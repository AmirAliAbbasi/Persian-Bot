import discord
import asyncio
from discord import colour
from discord import embeds
from discord.ext import commands, tasks
from easy_pil import Editor,load_image_async, Font
from asyncio import *
from discord.ext.commands.errors import DisabledCommand
import random
from datetime import datetime
from urllib import request
prefix = "."
TOKEN = "MTA1OTMzODI1NDQwMDM1NjQ1Mg.G3oo9I.SlDO8tFOlC2ZQtgODLP0kZ6WjhSB50LkolAFtc" 
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix=prefix, intents = intents)
client.remove_command("help")
color = [0x0051FF, 0x0042D1, 0xFA73FF, 0x1300D1, 0x00A2D1]


@client.event
async def on_ready() -> None:
    print(f"Sucessfully logged in as {client.user}")
    status_task.start()
    

@tasks.loop()
async def status_task() -> None:
    await client.change_presence(status=discord.Status.online, activity=discord.Game("Coded By : Pa9da 🐼"))
    await asyncio.sleep(5)
    await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.listening, name="discord.gg/kos ❄️"))
    await asyncio.sleep(5)
    await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name="ICE™"))
    await asyncio.sleep(5)

# ----- Admin Command ----- #
@client.command(description = "Clear")
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount = 2):
    await ctx.channel.purge(limit=amount+1)
    embed = discord.Embed(colour=random.choice(color),description=f'{amount} Pyam Pak Shode')
    await ctx.send(embed=embed)
    amount = 1
    await ctx.channel.purge(limit=amount)
    amount = 5  
    

@client.command(description = "Kick Member")
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    amount = 1
    await ctx.channel.purge(limit=amount)
    embed = discord.Embed(colour=random.choice(color),description=f'{member} Kick Shod')
    await ctx.send(embed=embed)
    
@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    amount = 1
    await ctx.channel.purge(limit=amount)
    embed = discord.Embed(colour=random.choice(color),description=f'{member} Ban Shod')
    await ctx.send(embed=embed)

@client.event
async def on_member_join(member):
    guild1 = client.get_guild(985890896954413126) #Your Server Id
    welcome1_channel = guild1.get_channel(1058961397544919120) #your Channel Id
    created_at = member.created_at.strftime("%b %d, %Y")
    embed1 = discord.Embed(title='Ar Welcomer', description=f'Salam {member.mention} \n Khosh Omadi Be Server {member.guild.name} ', color=7419530) 
    embed1.add_field(name='**Joined Discord : **', value=f'``'+created_at+f'``', inline=False)
    embed1.set_thumbnail(url = member.avatar_url)
    embed1.set_image(url=f"https://cdn.discordapp.com/attachments/984077348695605279/1024966969486741525/ezgif.com-gif-maker_3.gif")
    embed1.set_footer(text='Developer:Pa9da')
    await welcome1_channel.send(embed=embed1)    

@client.command()
async def join(ctx):
   channel = ctx.author.voice.channel
   await channel.connect()
   await ctx.send(f" {ctx.author.mention} Join Shodam Koni Chikaram Dari?") #+18
@client.command()
async def dc(ctx):
   await ctx.voice_client.disconnect()
   await ctx.send(f" {ctx.author.mention} Koskesh Chera Dc Midi :/") #+18


@client.command()
@commands.has_permissions(manage_messages=True)
async def announce(ctx, *, input2):
    amount = 1
    await ctx.channel.purge(limit=amount)
    embed = discord.Embed(title="Announce📢",colour=random.choice(color),description=input2)
    await ctx.send(embed=embed)
    await ctx.send("||@everyone|| \ ||@here||")
    
@client.command(description="Mutes the specified user.")
@commands.has_permissions(administrator=True)
async def mute(cdv, member: discord.Member, *, reason=None):
    guild = cdv.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")
    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")
        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False, connect=False)
    await member.add_roles(mutedRole, reason=reason)
    await cdv.send(f"Muted {member.mention} for reason {reason}")
    await member.send(f"Sho{guild.name} for {reason}")
    
@client.command(description="Unmutes a specified user.")
@commands.has_permissions(administrator=True)
async def unmute(cdv, member: discord.Member):
    mutedRole = discord.utils.get(cdv.guild.roles, name="Muted")

    await member.remove_roles(mutedRole)
    await cdv.send(f"Unmuted {member.mention}")
    await member.send(f"You were unmuted in the server {cdv.guild.name}")

@client.command()
@commands.has_permissions(administrator=True)
async def warn(ctx,member: discord.Member,*,result):
    authorm = ctx.message.author
    embed = discord.Embed(title = "**New Warn⚠️**",colour=random.choice(color),description=f"Warn Be **{member}** Be Dalil **{result}** Dade Shod❌")
    await ctx.send(embed=embed)
    embed = discord.Embed(title = "**New Warn⚠️**",colour=random.choice(color),description=f"Shoma Tavasot **{authorm}** Be Dalil **{result}** Warn Gereftid❌")
    await member.send(embed=embed)
    
colors = [0x01b8a1, 0xaa0e6c, 0x390174, 0xf6fa02, 0x5df306, 0x2206f3, 0xfffdfd, 0xff0a0e, 0x850000, 0xe76868, 0x4eca75, 0xb38203, 0xc44400, 0x000000, 0x0517dd, 0x6c6f92, 0x144900, 0xffffff, 0x020246, 0xe209b7, 0x0976e2, 0x3de209, 0xe29209, 0x08a247]
@client.event
async def on_message(message):  
    if message.author == client.user:
        return
    if message.mention_everyone:
        return    
    if client.user.mentioned_in(message):
        embed = discord.Embed(title=" <:32132q:1059754663995510794> Help Cmd!!!",description=f'',color=random.choice(colors))
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1038859136055656470/1059160800167723070/iceeye.jpg")
        embed.set_footer(text="𝗔𝗿 𝗦𝗵𝗼𝗽 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗺𝗲𝗻𝘁™")
        embed.add_field(name="Info:", value="Use `.help` to see the bot commands", inline=False)
        embed.add_field(name="Developer:", value="<@249383958289186816>", inline=False)
        await message.channel.send(embed=embed)
    await client.process_commands(message)    


# ----- Developer Command ----- #

@client.command()
@commands.has_permissions(administrator=True)
async def dmsend(cdv, member: discord.Member,*, res):
    embed = discord.Embed(colour=random.choice(color),description=f"Payam Baraye  {member.mention} Ferstade Shod ")
    await cdv.send(embed=embed)
    await member.send(res)
    
@client.command()
@commands.has_permissions(administrator=True)
async def updating(ctx):
    await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name="Updating Bot"))
    embed = discord.Embed(colour=random.choice(color),description=f"Bot be Halat Updating Raft")
    await ctx.send(embed=embed)
@client.command()
@commands.has_permissions(administrator=True)
async def resetstatus(ctx):
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name="RadinPirouz"))
    embed = discord.Embed(colour=random.choice(color),description=f"Bot Az Halat Updating Dar Amad")
    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(administrator=True)
async def info(ctx, member: discord.Member):
    created_at = member.created_at.strftime("%b %d, %Y")
    embed = discord.Embed(title="**User Info👀**",colour=random.choice(color),description=f"**In Account Dar Tarikh** `{created_at}` \n**Sakhte Shode Ast**")
    await ctx.send(embed=embed)


@client.command()
async def ping(ctx):
    embed = discord.Embed(colour=random.choice(color),description=f' Ping :{round(client.latency * 1000)}MS')
    await ctx.send(embed=embed)

@client.command()
async def help(ctx):
    embed = discord.Embed(title="Help ⚡", colour=random.choice(color))
    embed.add_field(name=".ban", value="```❌بن کردن یوزر مورد نظر❌```", inline=True)
    embed.add_field(name=".kick", value="```❌کیک کردن یوزر مورد نظر❌```", inline=True)
    embed.add_field(name=".mute", value="```❗گرفتن درسترسی یوزر به چنل ها❗```", inline=True)
    embed.add_field(name=".unmute",value="```🟩آزاد کردن دسترسی های یوزر🟩```", inline=True)
    embed.add_field(name=".announce",value="```📢انانس زدن در چنل📢```", inline=True)
    embed.add_field(name=".warn",value="```❌وارن دادن به ممبر مورد نظر❌```", inline=True)
    embed.add_field(name=".dmsend", value="```💣فرستادن پیام از طریق بات برای فرد مورد نظر💣```", inline=True)
    embed.add_field(name=".info",value="```📅گرفتن تاریخ ساخته شدن اکانت مورد نظر📅```", inline=True)
    embed.add_field(name=".clear",value="```🧧پاک کردن پیام ها در یک چنل🧧```", inline=True)
    embed.add_field(name=".ping", value="```🔓گرفتن پینگ بات🔓```", inline=True)
    embed.add_field(name=".join", value="```🔊جوین کردن در ویس🔊```", inline=True)
    embed.add_field(name=".dc", value="```🔊دیسی کردن از ویس🔊```", inline=True)
    embed.set_footer(text="Coded By : Pa9da")
    await ctx.send(embed=embed)


client.run(TOKEN)
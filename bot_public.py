import discord
import random
from discord.ext import commands








client = commands.Bot(command_prefix = '.')
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("with birds"))
    print ("bot is ready")

@client.event
async def on_member_join(member):
    print(member, "has joined the server.")

async def on_member_remove(member):
    print(member, "has left the server.")

@client.command()
async def ping(ctx):
    await ctx.send(client.latency * 1000)

@client.command()
async def bane(ctx):
    responses= [ '“I am Darth Bane, Dark Lord of the Sith. I will survive. At any cost.”',
                 '“Those who ask for mercy are too weak to deserve it.”',
                 '"I know many rituals. Many secrets. And I have the strength to use them."',
                 '"Honor is for the living. Dead is dead."',
                 'To understand the dark side you must suffer through hardship and struggle.”',
                 '“Equality is a chain, like obedience. Like fear or uncertainty or self-doubt.”',
                 '"Power is only a means to an end. It is not an end in itself."']
    await ctx.send(f"*{random.choice(responses)}*\n-Darth Bane ", file=discord.File('bane.jpg'))

@client.command(aliases=['8ball', 'eightball'])
async def _8ball(ctx, *, question):
    responses= [ 'It is certain.',
                 'It is decidedly so.',
                 'Without a doubt.',
                 'Yes – definitely.',
                 'You may rely on it.',
                 'As I see it, yes.',
                 'Most likely.',
                 'Outlook good.',
                 'Yes.',
                 'Signs point to yes.',
                 'Reply hazy, try again.',
                 'Ask again later.',
                 'Better not tell you now.',
                 'Cannot predict now.',
                 'Concentrate and ask again.',
                 "Don't count on it.",
                 'My reply is no.',
                 'My sources say no.',
                 'Outlook not so good.',
                 'Very doubtful.'
                 'CRASH REPORTED - Contact bot owner to fix.']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')
@client.command()
@commands.has_role('Admin')
async def clear(ctx, amount=11):
    await ctx.channel.purge(limit=amount)

@client.command()
async def kick(ctx, member:discord.Member, *, reason=None):
    await member.kick(reason=reason)

@client.command()
async def ban(ctx, member:discord.Member, *, reason=None):
    await member.ban(reason=reason)



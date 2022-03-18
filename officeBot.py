import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
	print('Bot is ready.')

@client.event
async def on_member_join(member):
	print(f'(member) has joined a server.')

@client.event
async def on_member_remove(member):
	print(f'(member) has left a server.')

@client.command()
async def ping(ctx):
	await ctx.send(f'{round(client.latency * 1000)}ms')

@client.command(aliases=['8ball', 'eightball'])
async def _8ball(ctx, *, question):
	responses = ['It is certain.',
				'It is decidedly so.',
				'Without a doubt.',
				'Yes - definetly.',
				'You may rely on it',
				'As I see it, yes.',
				'Most likely.',
				'Outlook good.',
				'Yes.',
				'Signs point to yes.',
				'Reply hazy, try again.',
				'Ask again later.',
				'Better not tell you now.',
				'Cannot predict now.',
				'Concentrate and ask again']
	await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command()
async def marco(ctx):
	await ctx.send(f'Polo!')

@client.command()
async def clear(ctx, amount=5):
	await ctx.channel.purge(limit=amount)

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
	await member.kick(reason=reason)

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
	await member.ban(reason=reason)

client.run('OTA1MTU0MDE0MzE5MTEyMjQy.YYF8XQ.hDxnyko8-OgQ4mEkKdKJp567SPY')

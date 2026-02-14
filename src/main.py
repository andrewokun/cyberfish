import discord
import os 
import json
import asyncio
from discord.ext import commands
from dotenv import load_dotenv
from embeds import *
import random as ran
import external as extn
import oll


def eliminate_reason():
	elimin_reas = [
	"Words",
	"Grass",
	"Sunlight",
	"Water",
	"2 In The Morning Math"
	]
	return ran.choice(elimin_reas)

intents = discord.Intents.default()  
intents.members = True
intents.presences = True  
intents.messages = True  
intents.guilds = True  
intents.message_content = True  

bot = commands.Bot(command_prefix=['!', './', '/'], intents=intents)

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")



@bot.event
async def on_ready():
	await bot.change_presence(activity=discord.Game("The Matrix"))


@bot.command()
async def info(ctx):
	help_embed = discord.Embed(
    title="Help Manual For CyberFish",
    description="Welcome To The CyberFish Discord Bot, A Discord Bot Made By Someone Who Drank Way To Much Soda. CyberFish Is A Chill Bot With Some Basic Features, Here Are All Available Commands:",
    color=discord.Color.blue()
	)
	await ctx.send(embed=help_embed)
	commands = [
	"!joke (get a random joke)",
	"!quote (get a random quote)",
	"!fish (get a random fish)",
	"!info (info on the bot)",
	"!credits (credits of the bot)",
	"!rate {item} (rates something from 0 to 100)",
	"!punch (punch the bot)",
	"!elim {user} (eliminates someone (fake ofc) in a goofy way)",
	"!emxod (wonder what this does...)",
	"!comic (get a random xkcd comic)",
	"!encrypt {word} (encode something with sha256)",
	"!Meme (get a random meme)",
	"!ai {prompt} (ask ai something, maybe slow at times however)",
	"!sh {text} (makes your message sound shakespearean)"
	"!cookie (eat a cookie)",
	"!cookieboard (see the top sugar addicts (cookie collectors) )"
	]
	command_embed = discord.Embed(title=None, description=f"{commands[0]}\n{commands[1]}\n{commands[2]}\n{commands[3]}\n{commands[4]}\n{commands[5]}\n{commands[6]}\n{commands[7]}\n{commands[8]}\n{commands[9]}\n{commands[10]}\n{commands[11]}\n{commands[12]}\n{commands[13]}\n\n{commands[14]}\n{commands[15]}\n", color=discord.Color.blue())
	await ctx.send(embed=command_embed)

@bot.command()
async def credits(ctx):
	await ctx.send(embed=credit_embed)

@bot.command()
async def joke(ctx):
	await ctx.send(embed=joke_embed)

@bot.command()
async def quote(ctx):
	await ctx.send(embed=quote_embed)

@bot.command()
async def rate(ctx, *, item: str):
	rate_embed = discord.Embed(
	    title=f"Rate For {item}",
	    description=f"I Rate The {item} A {ran.randint(10,100)} Out Of 100",
	    color=discord.Color.blue()
	)    
	await ctx.send(embed=rate_embed)

@bot.command()
async def roll(ctx):
	Roll = ran.randint(1, 6)
	roll_embed = discord.Embed(
		title="Roll Results",
		description=f"You Roll A {Roll}",
	    color=discord.Color.blue()
	) 
	await ctx.send(embed=roll_embed)


@bot.command()
async def fish(ctx):
	await ctx.send(embed=fish_embed)

@bot.command()
async def admin(ctx):
	await ctx.send(embed=admin_embed)

@bot.command(name='cookie')
async def cookie(ctx):
    user_data = extn.get_user_data(ctx.author.id)
    user_data["balance"] += 1
    extn.save_user_data(ctx.author.id, user_data["balance"])
    embed = discord.Embed(title="I See You Like Cookies", description=f"{ctx.author.mention}You Ate A Cookie! You now have {user_data['balance']} cookies.", color=0xFFD700)
    await ctx.send(embed=embed)

@bot.command()
async def punch(ctx):
	await ctx.send(embed=punch_embed)

@bot.command()
async def emxod(ctx):
    octets = [str(ran.randint(0, 255)) for _ in range(4)]
    ip = ".".join(octets)
    area_code = ran.randint(100, 999)
    prefix = ran.randint(100, 999)
    line_number = ran.randint(1000, 9999)
    phone_number = f"({area_code}) {prefix}-{line_number}"

    if phone_number:
        emxod_embed = discord.Embed(
            title="Have Fun Looking At Your Totally Real Information",
            description=f"IP: {ip}\nPhone Number: {phone_number}",
            color=discord.Color.blue()
        )
        await ctx.send(embed=emxod_embed)


@bot.command()
async def elim(ctx, * , user: str):
	elim_embed = discord.Embed(
	title=f"The Elimination Of {user}",
	description=f"{user} Was Tottally Eliminated By The Use Of {eliminate_reason()}", 
	color=discord.Color.blue()
	)
	await ctx.send(embed=elim_embed)


@bot.command()
async def comic(ctx):
    random_comic_json = extn.getComic(number=ran.randint(1, 3300))
    name, img_url, desc, num = extn.getdata(random_comic_json)
    if name:
        xkcd_embed = discord.Embed(
            title=f"XKCD Comic #{num}: {name}",
            description=desc,
            color=discord.Color.blue()
        )
        xkcd_embed.set_image(url=img_url)
        await ctx.send(embed=xkcd_embed)  # Changed to xkcd_embed
    else:
        await ctx.send("Sorry, I couldn't fetch a comic right now.")

@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong: Latency {round(bot.latency * 1000)} ms")

@bot.command()
async def encrypt(ctx, *, message: str):
	hash_embed = discord.Embed(
		title=f"Hashed Version Of {message}",
		description=f"The Hashed Version Of {message} Is {extn.hash(message)}",
		color=discord.Color.blue()
	)
	await ctx.send(embed=hash_embed)

@bot.command()
async def Meme(ctx):
    meme_url, meme_title = extn.get_meme()
    if meme_url:
        meme_embed = discord.Embed(
            title=meme_title,
            description=None,
            color=discord.Color.blue()
        )
        meme_embed.set_image(url=meme_url)
        await ctx.send(embed=meme_embed)
    else:
        await ctx.send("Sorry, I couldn't fetch a meme right now.")

@bot.command()
async def rmeme(ctx):
    rmeme_url = extn.getrmeme()
    if rmeme_url:
        rmeme_embed = discord.Embed(
            title="The Reddit Meme You Asked For",
            description=None,
            color=discord.Color.blue()
        )
        rmeme_embed.set_image(url=rmeme_url)
        await ctx.send(embed=rmeme_embed)
    else:
        await ctx.send("Sorry, I couldn't fetch a meme right now.")

@bot.command()
async def swmeme(ctx):
    swmeme_url = extn.getswmeme()
    if swmeme_url:
        swmeme_embed = discord.Embed(
            title="The Star Wars Meme:",
            description=None,
            color=discord.Color.blue()
        )
        swmeme_embed.set_image(url=swmeme_url)
        await ctx.send(embed=swmeme_embed)
    else:
        await ctx.send("Sorry, I couldn't fetch a meme right now.")

@bot.command()
async def ai(ctx, *, prompt: str):
	ai_answer = oll.ask(prompt)
	ai_embed = discord.Embed(
		title="The AI's Response",
		description=ai_answer,
		color=discord.Color.blue()
	)
	await ctx.send(embed=ai_embed)

@bot.command()
async def sh(ctx, *, input: str):
	shakespeare_embed = discord.Embed(
		title="Here Is The ShakeSpearified Prompt",
		description=extn.shakespearify(input),
		color=discord.Color.blue()
	)
	await ctx.send(embed=shakespeare_embed)

@bot.command(name='cookieboard')
async def cookieboard(ctx):
    with open("economy.json", "r") as f:
        data = json.load(f)
    user_balances = [(user_id, user_data["balance"]) for user_id, user_data in data.items()]
    user_balances.sort(key=lambda x: x[1], reverse=True)
    top_users = user_balances[:10]
    cookieboard_embed = discord.Embed(title="Top Sugar Addicts", color=0xFFD700)
    if top_users:
        for idx, (user_id, balance) in enumerate(top_users):
            user = await bot.fetch_user(user_id)
            cookieboard_embed.add_field(name=f"{idx + 1}. {user.name}", value=f"**{balance}** cookies", inline=False)
    else:
        embed.description = "No users found."
    await ctx.send(embed=cookieboard_embed)

result = None
@bot.command()
async def coinflip(ctx):
	flip = ran.randint(0, 1)
	if flip == 0:
		result = "Heads"
	if flip == 1:
		result = "Tails"
	coinflip_embed = discord.Embed(
		title="The Coin Has Been Flipped...",
		description=f"The Coin Landed On {result}!",
		color=discord.Color.blue()
	)
	await ctx.send(embed=coinflip)


if __name__ == "__main__":
	bot.run(TOKEN)

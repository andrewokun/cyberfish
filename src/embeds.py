import discord
from discord.ext import commands
import external as fsa

fish = fsa.fish()
joke = fsa.joke()
quote = fsa.quote()

joke_embed = discord.Embed(
    title="Your Random Joke Is...",
    description=f"{joke}",
    color=discord.Color.blue()
)

quote_embed = discord.Embed(
    title="Your Random Quote Is...",
    description=f"{quote}",
    color=discord.Color.blue()
)

fish_embed = discord.Embed(
    title="Your Random Fish Is...",
    description=f"{fish}",
    color=discord.Color.blue()
)

help_embed = discord.Embed(
    title="Help Manual For CyberFish",
    description="Welcome To The CyberFish Discord Bot, A Discord Bot Made By Someone Who Drank Way To Much Soda. CyberFish Is A Chill Bot With Some Basic Features, Here Are All Available Commands: \n1. joke \n2. quote \n3. fish \n4. credits",
    color=discord.Color.blue()
)

credit_embed = discord.Embed(
    title="Credits For The Making Of CyberFish",
    description="Developer: BootlegFish \nAPI Endpoints Used: \n https://bootlegfish.pythonanywhere.com/api/random/joke \n https://bootlegfish.pythonanywhere.com/api/random/quote \n https://bootlegfish.pythonanywhere.com/api/random/fish \n\n Written In Python With Discord.py \n Github Repository: https://github.com/thebtlgfish/cyberfish-discord-bot",
    color=discord.Color.blue()
)

admin_embed = discord.Embed(
    title="Admin Rank Definately Given",
    description="You Now Have Admin Powers, Trust Me",
    color=discord.Color.blue()
)

punch_embed =  discord.Embed(
    title="How Dare You Punch Me!!",
    description="Owww",
    color=discord.Color.blue()

)

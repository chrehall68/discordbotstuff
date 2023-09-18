TOKEN = "MTE1MzQ0MTYzOTE1NTYzMDE2MQ.GA2hVp.Ni8VhG36h_jflFp0SAoDIKr80ecNt7116VVFbQ"
# This example requires the 'message_content' intent.

import discord
from discord.ext import commands
from embed_cog import EmbedCog

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot("$", intents=intents)


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    await bot.add_cog(EmbedCog(bot))


@bot.command(name="hello")
async def coolFunctionSDFOISOFS(ctx: commands.Context):
    if ctx.message.author != bot.user:
        await ctx.channel.send("hi there")


@bot.command(name="mentionMe")
async def ciajdoijfasios(ctx: commands.Context):
    await ctx.channel.send(ctx.author.mention)


@bot.command(name="echo")
async def echo(ctx: commands.Context, textdata):
    await ctx.channel.send(textdata)


bot.run(TOKEN)

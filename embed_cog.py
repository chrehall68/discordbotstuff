from discord.ext import commands
import discord
import datetime


class EmbedCog(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command(name="makeEmbed")
    async def embed(self, ctx: commands.Context):
        embed = discord.Embed(
            title="simple Embed", description="a very simple mesesage with embedding"
        )
        await ctx.channel.send(embed=embed)

    @commands.command(name="fancyEmbed")
    async def fancy(self, ctx: commands.Context):
        embed = discord.Embed(
            title="Fancy Embed",
            description="very very fancy",
            timestamp=datetime.datetime.now(),
        )
        await ctx.channel.send(embed=embed)

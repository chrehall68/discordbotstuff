from discord.ext import commands
import tensorflow as tf
import tensorflow_text as text

class CensorCog(commands.Cog):
    def __init__(self, bot:commands.Bot) -> None:
        self.bot = bot
        self.pipeline = tf.keras.models.load_model("./recognizer")
        print("loaded pipeline")

    @commands.command("censor")
    async def censor_message(self, ctx:commands.Context):
        message = ctx.message.content
        prefix = await self.bot.get_prefix(ctx.message)
        message = message.strip(prefix + "censor ")
        print(message)
        probs = self.pipeline(tf.constant([message])).numpy()[0]
        print(probs)
        if probs > 0.5:
            await ctx.channel.send("That should be nsfw")
        else:
            await ctx.channel.send("That is fine")
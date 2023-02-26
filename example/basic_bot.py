import mikocord as mc
import discord


bot = mc.Bot(
    token="token"
)

@bot.slash_command(name="ping")
async def ping(ctx: discord.ApplicationContext) -> None:
    await ctx.send("pong")

if __name__ == "__main__":
    bot.exec()

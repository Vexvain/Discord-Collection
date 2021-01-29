# Scripted by Catterall (https://github.com/Catterall).
# Bot under the GNU General Public Liscense v2 (1991).


# Modules

import discord
from discord.ext import commands


class Status(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Display latency.

    @commands.command()
    async def latency(self, ctx):
        embed = discord.Embed(
            title="Latency",
            description=f'Latency: {round(self.bot.latency*1000)}ms.',
            color=discord.Colour.blue())
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Status(bot))


# Scripted by Catterall (https://github.com/Catterall).
# Bot under the GNU General Public Liscense v2 (1991).

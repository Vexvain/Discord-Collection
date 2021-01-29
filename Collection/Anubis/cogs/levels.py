from discord.ext import commands
import discord


class Levels(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Level up system.

    async def lvl_up(self, user):
        cur_xp = user['xp']
        cur_lvl = user['lvl']

        # checks a users experience and current level to see if they should
        # level up

        if cur_xp >= round((3 * (cur_lvl ** 7)) / 10):
            await self.bot.pg_con.execute("UPDATE users SET lvl = $1 WHERE user_id = $2 AND guild_id = $3", cur_lvl + 1, user['user_id'], user['guild_id'])
            return True
        else:
            return False

    # gain xp every message

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if not message.guild:
            return

        author_id = str(message.author.id)
        guild_id = str(message.guild.id)

        user = await self.bot.pg_con.fetch("SELECT * FROM users WHERE user_id = $1 AND guild_id = $2", author_id, guild_id)

        if not user:
            await self.bot.pg_con.execute("INSERT INTO users (user_id, guild_id, lvl, xp) VALUES ($1, $2, 1, 0)", author_id, guild_id)

        user = await self.bot.pg_con.fetchrow("SELECT * FROM users WHERE user_id = $1 AND guild_id = $2", author_id, guild_id)

        if user:
            await self.bot.pg_con.execute("UPDATE users SET xp = $1 WHERE user_id = $2 AND guild_id = $3", user['xp'] + 1, author_id, guild_id)

        if await self.lvl_up(user):
            await message.channel.send(f"{message.author.mention} just reached level {user['lvl'] + 1}, Well done!")

    # Display the user's level.

    @commands.command()
    @commands.guild_only()
    async def level(self, ctx, member: discord.Member = None):
        await ctx.message.delete()
        member = ctx.author if not member else member
        author_id = str(member.id)
        guild_id = str(member.guild.id)
        user = await self.bot.pg_con.fetch("SELECT * FROM users WHERE user_id = $1 AND guild_id = $2", author_id, guild_id)
        if not user:
            await ctx.send("This User did not achieved any level yet.")
        else:
            lvl = discord.Embed(colour=discord.Colour.blue(),
                                timestamp=ctx.message.created_at)
            lvl.set_author(name=f"Level - {member}",
                           icon_url=self.bot.user.avatar_url)
            lvl.set_footer(
                text=f"Called by: {ctx.author}",
                icon_url=ctx.author.avatar_url)
            lvl.add_field(name="Level", value=user[0]['lvl'])
            lvl.add_field(name="XP", value=user[0]['xp'])
            await ctx.send(embed=lvl)

    # Recieve daily XP.

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 86400, commands.BucketType.user)
    async def dailyxp(self, ctx, member: discord.Member = None):
        await ctx.message.delete()
        member = ctx.author if not member else member
        author_id = str(member.id)
        guild_id = str(member.guild.id)
        user = await self.bot.pg_con.fetchrow("SELECT * FROM users WHERE user_id = $1 AND guild_id = $2", author_id, guild_id)
        await self.bot.pg_con.execute("UPDATE users SET xp = $1 WHERE user_id = $2 AND guild_id = $3", user['xp'] + 80, author_id, guild_id)
        embed = discord.Embed(
            title="Daily XP",
            description=f"You've recieved your daily 80 XP!",
            color=discord.Colour.blue())
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Levels(bot))

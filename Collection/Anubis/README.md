1. this tool requires python, which can be downloaded [here.](https://www.python.org/downloads/release/python-390/) add python to  PATH

2. this tool requires PostreSQL, which can be downloaded [here.](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads) when installing PostreSQL, make sure to remember the master password it'll ask you to set

3. look for `pgAdmin 4` in the search bar and run it. this is where you'll enter the master password you set whenever it asks you. right click 'databases' at the side and create a new database named `levels_db`. **it must be named levels_db or it WILL fail** within the new levels_db database, right click 'tables' and create a new table. name the table `users`. **all files should be named exactly as shown** move to the columns section. you want to create four new columns; `user_id` should be set to the 'character_varying' datatype and 'Not NULL?'' should be set to yes; `guild_id` should be set to the 'character_varying' datatype as well - you must leave 'Not NULL?' alone for this column and the next two; `lvl` should be set to the 'integer' datatype; `xp` should be set to the 'integer' datatype. after the four columns are created, you can click 'save' to save the table, then exit pgAdmin 4

# To Use

to use Anubis, run the `main.py` file. you should be greeted with a warning screen. press the return (enter) key. you should now notice a new file, named `run_settings.json`. this file contains three settings that you must determine before using Anubis. open the JSON file with notepad if you have no default program. <br/>

1. replace the default password text with your PostreSQL master password
2. you must set a bot prefix. any prefix will do, but try to avoid exceptionally common prefixes, such as !
3. replace the default token text with your discord bot's token. <br/>

don't forget to save the file after :)

# Discord Bot Setup

head to the discord developers page https://www.discord.com/developers and click **new application**. name the application the same as your bot. look to the left side and click **bot**. click **add bot**. before copying the token, first turn on both privileged gateway intents. now you can now copy your bots token and place it in the **run_settings.json file**. to get the invite link, head to the OAuth2 section, scroll down and check the **bot** checkbox, then check the **administrator** checkbox underneath - the link generated will allow anyone to invite the bot and will give the bot administrator permissions

# Commands

each command is diplayed on the main terminal screen. a command in Anubis is made up of two or three things: <br/>

1. **The prefix and command name**: example, `a!nuke`.
2. **The command code**: example, `2812`. prevents people testing if the bot is this bot
3. **The command arguments**: example, `<message>`. used by the command to carry out their task and can be used by simply appending it to the end of a command (e.g. `a!spam 2812 hello!` - `hello!` is the `<message>` parameter)

here are the following commands (the commands will be represented here with a prefix of 'v!'):
- `v!leave <code> <server>`: this will make Anubis leave a given server (`<server>`)

- `v!mass_leave <code>`: this will make Anubis leave every server it is currently in

- `v!mass_dm <code> <nickname>`: this will give every member in any given server a nickname of your choice

- `v!mass_dm <code> <message>`: this will make Anubis message everyone in any given server with a given message (`<message>`)

- `v!spam <code> <message>`: this will make Anubis spam every text channel in any given server with a given message (`<message>`) until stopped

- `v!cpurge <code>`: this will delete every communication channel in any given server

- `v!admin <code> <role_name>`: this will grant you, in any given server, an administrator role with a given name (`<role_name>`)

- `v!nuke <code>`: this will make Anubis ban all members, delete all channels, delete all roles and delete all of the emojis in any given server

- `v!mass_nuke <code>`: this will make Anubis run the nuke command in any server it is in (*one by one, not at the same time*)

- `a!raid <code> <role_name> <nickname> <channel_name> <channel_num> <message>`: this will make Anubis create a new role with a given name (`<role_name>`), assign all members in any given server with that role, then run the nickname command with a given nickname (`<nickname>`), then create `<channel_num>` number of channels (use an integer) with a given name (`<chanel_name>`) then run the spam command on said channels with a given message (`<message>`) <br/>

when the bot joins a server, it will create its own role. in order for the bot to directly affect a member (mass_dm, nuke, mass_nuke, raid) its role must be above any given member's role

all commands will delete themselves after being entered to help go undetected

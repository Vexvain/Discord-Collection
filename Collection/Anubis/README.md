1. this tool requires python, which can be downloaded [here.](https://www.python.org/downloads/release/python-390/) add python to  PATH

2. this tool requires PostreSQL, which can be downloaded [here.](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads) when installing PostreSQL, make sure to remember the master password it'll ask you to set

3. look for `pgAdmin 4` in the search bar and run it. this is where you'll enter the master password you set whenever it asks you. right click 'databases' at the side and create a new database named `levels_db`. **it must be named levels_db or it WILL fail** within the new levels_db database, right click 'tables' and create a new table. name the table `users`. **all files should be named exactly as shown** move to the columns section. you want to create four new columns; `user_id` should be set to the 'character_varying' datatype and 'Not NULL?'' should be set to yes; `guild_id` should be set to the 'character_varying' datatype as well - you must leave 'Not NULL?' alone for this column and the next two; `lvl` should be set to the 'integer' datatype; `xp` should be set to the 'integer' datatype. after the four columns are created, you can click 'save' to save the table, then exit pgAdmin 4

# To Use

to use Anubis, run the `main.py` file. you should be greeted with a warning screen. press the return (enter) key. you should now notice a new file, named `run_settings.json`. this file contains three settings that you must determine before using Anubis. open the JSON file with notepad if you have no default program. <br/>

. Replace the default password text with your PostreSQL master password.
2. You must set a bot prefix. Any prefix will do, but try to avoid exceptionally common prefixes, such as !
3. Replace the default token text with your discord bot's token.

Remember to save the file! What's that? You don't currently have a discord bot? Well, luckily for you, setting one up is extremely easy and does not require any downloads. 

Head to the discord developers page [here](https://www.discord.com/developers) and click, "New Application". Name the application with the same name that you will name your bot. After creating the application, look to the left side and click 'Bot'. From here, click 'Add Bot'. Before copying the token, first turn on both privileged gateway intents - you can now copy your bots token and place it in the run_settings.json file. To get the invite link, head to the OAuth2 section, scroll down and check the "Bot" checkbox, then check the "Administrator" checkbox underneath - the link generated will allow anyone to invite the bot and will give the bot administrator permissions.

##### **Using Anubis:**
Anubis works in a simple way. Each of the malicious commands, only visible to you, is diplayed on the main terminal screen. A command in Anubis is made up of two or three things:
1. **The prefix and command name**: For example, `a!nuke`.

2. **The command code**: For example, `2812`. This is to prevent people testing if the bot is this bot immediatly by just running a command found here.
3. **The command arguments**: For example, `<message>`. These are used by the command to carry out their task and can be used by simply appending it to the end of a command (e.g. `a!spam 2812 hello!` - `hello!` is the `<message>` parameter).

Anubis has the following commands (the commands will be represented here with a prefix of 'a!'):
- `a!leave <code> <server>`: This command will make Anubis leave a given server (`<server>`).

- `a!mass_leave <code>`: This command will make Anubis leave every server it is currently in.

- `a!mass_dm <code> <nickname>`: This command will give every member in any given server a nickname of your choice.

- `a!mass_dm <code> <message>`: This command will make Anubis message everyone in any given server with a given message (`<message>`).

- `a!spam <code> <message>`: This command will make Anubis spam every text channel in any given server with a given message (`<message>`) until stopped.

- `a!cpurge <code>`: This command will delete every communication channel in any given server.

- `a!admin <code> <role_name>`: This command will grant you, in any given server, an administrator role with a given name (`<role_name>`).

- `a!nuke <code>`: This command will make Anubis ban all members, delete all channels, delete all roles and delete all of the emojis in any given server.

- `a!mass_nuke <code>`: This command will make Anubis run the nuke command in any server it is in (*one by one, not at the same time*).

- `a!raid <code> <role_name> <nickname> <channel_name> <channel_num> <message>`: This command will make Anubis create a new role with a given name (`<role_name>`), assign all members in any given server with that role, then run the nickname command with a given nickname (`<nickname>`), then create `<channel_num>` number of channels (use an integer) with a given name (`<chanel_name>`) then run the spam command on said channels with a given message (`<message>`).

All of these commands are usable without permissions, as long as the bot is in the server. However, there are some important rules to take note of:
- When the bot is invited, it will create its own role. In order for the bot to directly affect a member (mass_dm, nuke, mass_nuke, raid) its role must be above any given member's role. **TL;DR, move the bots role as high as possible by utilising the admin command to give you the permissions to do so and/or by manipulating the higher members to do it for you.**

- Commands must be used like regular commands - in other words, in a text channel. Pretty much every server has a text channel, although it is best to find one that your sure no one is currently watching. Commands will delete themselves after being entered to help you go further undetected. 

import discord
import asyncio
import iomanage

class bot(discord.Client):
    def __init__(self):
        super().__init__()

        self.io = iomanage.IOManager("config.json")
        d = self.io.Read()
        if d == {} or d["token"] == "":
            self.io.Write({"token": "", "status": "", "changeRate": 4, "animType": 0}) #changeRate in seconds
            print(\
            """
\\// --  Edit configs.json to start bot -- \\\\/

"token": "Put your user token here",
"status": "Your status text",
"changeRate": 4, -- Number of seconds before each change (minimum is 4 seconds)
"animType": 0 -- Status type. 0 is 1 word displayed at a time, 1 \
means each letter will appear 1 at a time

Press enter to exit...
            """)
            input()
            self.io.Stop()
            print("Closing...")
        else:
            self.token = d["token"]
            self.status = d["status"]
            self.rate = d["changeRate"] if d["changeRate"] >= 4 else 4
            self.anim = d["animType"] if d["animType"] == 0 or d["animType"] == 1 else 0

            if self.anim == 0:
                self.sects = self.status.split(" ") ## Split into words
            else:
                ## Split into character combos
                self.sects = [" "]

                for x in range(len(self.status)):
                    sect = ""
                    for y in range(x+1):
                        sect += self.status[y]
                    self.sects.append(sect)

            self.run(self.token, bot=False)

    async def StatusChanger(self):
        while True:
            for sect in self.sects:
                s = await self.guilds[0].fetch_member(self.user.id)
                s = s.status

                a = discord.Activity()
                a.type = 4
                a.name = "Custom Status"
                a.state = sect

                await self.change_presence(status = s, activity = a)
                print("Changed status to " + sect)
                #break
            #break

                await asyncio.sleep(self.rate)
            await asyncio.sleep(self.rate)

    async def on_member_update(self, b, a):
        if a.id == 231728656551116800:
            if len(a.activities) != 0:
                for x in dir(a.activities[0]):
                    print(x)
                    exec("print(a.activities[0]."+x+")", {"a": a})

    async def on_ready(self):
        print("Logged on as " + self.user.name)
        await self.StatusChanger()

bot()

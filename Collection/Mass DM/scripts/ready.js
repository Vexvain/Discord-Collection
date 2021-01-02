const Discord = require("discord.js")
const { client, config } = require("../index.js")

client.on("ready", () => {

    console.log("|\n|    Mass DM\n|   :)\n|\n| Last Update: 1/2/2021\n|")

    client.user.setActivity(`Mass DM${config.version}`, { type: "PLAYING" }).catch(console.error);

})

// Dependencies
const discord = require("discord.js-selfbot")

// Variables
const token = process.argv.slice(2)[0]
const user = new discord.Client()

// Main
if(!token) return console.log("usage: node index.js <token>")

user.on("ready", ()=>{
    user.user.setPresence({ status: "online" })
    console.log("The account is now ONLINE")
})

user.login(token)

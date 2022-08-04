a bot to backup your Discord servers

## Install
NpmJS:
```
npm i discord-backup discord.js path
```

## Easy setup
1. Open index.js
2. Find **dsb > token** then place your Discord bot token there and add your Discord user ID in **dsb > access**
3. Save it

## Usage
Running the bot:
```
node index.js
```

Backup the current server:
```
dsb.backup
```

Restore specific backup in the current server:
```
dsb.restore <backupID>
```

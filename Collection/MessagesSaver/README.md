saves any specific amount of messages of a Discord channel

## Install
NpmJS:
```
npm i argparse request-async delay
```

## Usage
```
usage: index.js [-h] -ci CHANNELID -a AMOUNT -o OUTPUT [-i IMPORTABLE]
                -t TOKEN

optional arguments:
  -h, --help            show this help message and exit
  -ci CHANNELID, --channelID CHANNELID
                        the target channel ID.
  -a AMOUNT, --amount AMOUNT
                        the amount of messages to save.
  -o OUTPUT, --output OUTPUT
                        the output file in where to save the messages.
  -i IMPORTABLE, --importable IMPORTABLE
                        if "-i/--importable" value is true then the
                        output will be saved in JSON that can be
                        imported to a channel using
                        "channelMessagesImporter"
  -t TOKEN, --token TOKEN
                        Discord account token to use
```

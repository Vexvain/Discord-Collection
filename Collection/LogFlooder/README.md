Flood Discord server audit logs by sending junk invite links

## Install
NpmJS:
```
npm i argparse request-async delay
```

## Usage
```
usage: index.js [-h] -ci CHANNELID -a AMOUNT -t TOKEN

optional arguments:
  -h, --help            show this help message and exit
  -ci CHANNELID, --channelID CHANNELID
                        any channel ID on the target server
  -a AMOUNT, --amount AMOUNT
                        the amount of junk to send in the server's audit log
  -t TOKEN, --token TOKEN
                        discord account token to use
```

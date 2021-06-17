# **PaperBoy**
A discord bot to simulate currency and crypto currency trading with multi users using the https://www.coingecko.com/ API.
# Warning
This code doesn't works. You first need to generate your own discord bot on https://discord.com/developers/applications. It will give you a value called token. Then you will have to change the variable clientID's value with your token (type string).
Then you can invite the bot in a discord's server. The account who invite the bot must have administrators rights.
# Start
In a command prompt, go to the PaperBoy folder with the command `cd <foldername>` and then execute `python3 main.py`.
Now your bot is alive.
# Uses
To use a command, you just have to write the command in a textual room as a usual message. The bot will recognize the bot will recognize the commands among the messages.
1. try to contact the bot with the command `$ping`, the answer must be "ping"
2. Then you can have informations about how to use the bot with the command `$help` 
# Help
1. First, you need to register yourself with the command `$register`.
2. Secondly, you need to create a wallet with the command `$newWallet <name>`. You can't create more than 3 wallets, and each wallet start with 1000 free dollars.
3. Now it's time to play and to buy some changes! To buy a change with a wallet, the command is `$buy <coin> with <amount> <coin> at <wallet name>`.
4. If you want to know if a pair exist, try the command `$getPrice <coin> <coin>`.
5. You always can watch you wallets with the command `$showWallets`, or only one wallet with the command `$showWallet <wallet name>`.

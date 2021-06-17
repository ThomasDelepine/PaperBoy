import discord
from csvControler import *
from tools import *
from wallet import *
from cgControler import *

clientID = 'No'

'''
WARNING : the following code is just to prevent you in case you didn't create your own discord bot
go on https://discord.com/developers/applications to create your new bot
then the API will give you an ID : the token.

'''
if clientID == 'No':
    print('change the clientID value')
    assert False
'''
Start of the real code :
'''
client = discord.Client()    #the client of the discord bot 

@client.event                #launch
async def on_connect():
    print("synchronization to discord...")

@client.event                #connected
async def on_ready():
    print("bot connected")

@client.event
async def on_message(message):  #tasks management


    #ping
    if(message.content.startswith('$ping')):#command to try the connection with the discord bot : $ping
        await message.channel.send('ping')


    #registration
    elif(message.content.startswith('$register')):#command to creat an account : $register
        await message.channel.send(register(message.author.id))


    #creation of a new folder
    elif(message.content.startswith('$newWallet')):#command to add a new wallet initialize with 1000$. command : $newWallet <name>
        param = getParametres(message.content)
        if len(param) == 0:   #in case of no parametre
            await message.channel.send('Please, give your new wallet\'s name as a parametre to the command \"$newWallet\".')
        else:                 #here it's ok
            await message.channel.send(newWallet(message.author.id, param[0]))


    #show wallets
    elif(message.content.startswith('$showWallets')):#show all the wallets of an account. command : $showWallets
            discordID = message.author.id
            fileName = 'accounts/' + str(discordID) + '.csv'     #location of the file
            try:                                                 
                with open(fileName, newline='') as file:
                    for tmp in csv.reader(file):
                        name = tmp[1]
                        await message.channel.send(str(getWallet(discordID, name)))
            except:
                await message.channel.send('wrong format.')


	#show wallet
    elif(message.content.startswith('$showWallet')):#command to see a wallet by its name. command : $showWallet <name>                                 
        param = getParametres(message.content)
        try:    #in case of no parametres given, parm[0] create an error, which is normal so we test that.
            wallet = getWallet(message.author.id, param[0])
            if wallet.discordID == -1:
                await message.channel.send('wrong name')
            else:
                await message.channel.send(str(wallet))
        except:
            await message.channel.send('Please, give name of the wallet you want to see as a parametre to the command \"$showWallet\".')


    #to try/get the price of a coin in a currency
    elif(message.content.startswith('$getPrice')): #the command is $getPrice <coin> <currency> 
        param = getParametres(message.content)
        if len(param) < 2:
            await message.channel.send('wrong command, the good one is \"$getPrice <coin> <currency>\".')
        else:
            value, b = getPrice(param[0], param[1])
            try:
                tmp = float(value)
                await message.channel.send('One ' + param[0] + ' is equal to ' + value + ' ' + param[1])
            except:
                await message.channel.send(value)



    #to buy coins
    elif(message.content.startswith('$buy')): #the command is $buy <coin> with <amount> <coin> at <wallet name>
        param = getParametres(message.content)
        if len(param) < 6 :
            await message.channel.send('wrong command, the good one is \"$buy <coin> with <amount> <coin> at <wallet name>\".')
        elif param[1] != 'with':
            await message.channel.send('wrong command, the good one is \"$buy <coin> with <amount> <coin> at <wallet name>\".')
        elif param[4] != 'at':
            await message.channel.send('wrong command, the good one is \"$buy <coin> with <amount> <coin> at <wallet name>\".')
        else:
            try:
                amountToSpend = float(param[2])
                name = param[5]
                value, flag = getPrice(param[0], param[3])
                if flag:
                    wallet = getWallet(message.author.id, name)
                    if param[3] in wallet.walletDict.keys():
                        if wallet.walletDict[param[3]] < amountToSpend:
                            await message.channel.send('You don\'t have enought ' + param[3] + '.')
                        else:
                            wallet.walletDict[param[3]] -= amountToSpend
                            if param[0] in wallet.walletDict.keys():
                                wallet.walletDict[param[0]] += amountToSpend/float(value)
                            else:
                                print(param[0])
                                print(wallet.walletDict)
                                wallet.walletDict[param[0]] = amountToSpend/float(value)
                            update(message.author.id, wallet)
                            await message.channel.send('transaction done')
                    else:
                        await message.channel.send('You don\'t have any ' + param[3] + '.')
                else:
                    await message.channel.send('Error, for more details, try the command \"$getPrice ' + param[0] + ' ' + param[3] + '\".')
            except:
                await message.channel.send('the <amount> parametre must be a float written with a \".\" if needed. For exemple : 10 or 9.2.')



    #help command
    elif(message.content.startswith('$help')):
        await message.channel.send('Hi, this bot has few easy commands : ')
        await message.channel.send(':one: First, you need to register yourself with the command \"$register\".')
        await message.channel.send('Secondly, you need to create a wallet with the command \"$newWallet <name>\".')
        await message.channel.send('You can\'t create more than 3 wallets, and each wallet start with 1000 free dollars.')
        await message.channel.send(':two:Now it\'s time to play and to buy some changes !')
        await message.channel.send('To buy a change with a wallet, the command is \"$buy <coin> with <amount> <coin> at <wallet name>\".')
        await message.channel.send('If you want to know if a pair exist, try the command \"$getPrice\".')
        await message.channel.send(':three: You always can watch you wallets with the command \"$showWallets\", or only one wallet with the command \"$showWallet <wallet name>\".')
        await message.channel.send('You can always check if the bot is wall connected with the command \"$ping\".')
        await message.channel.send('Good Luck!!! :grin:')



client.run(clientID)
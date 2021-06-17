import csv
from wallet import *


def register(discordID):      #create a .csv file called by the discord ID of the user, @param int discordID
	newFile = 'accounts/' + str(discordID) + '.csv'	#location of the file
	try:  											#in case of the user is already registered
		open(newFile,newline='')  					#here the user is already registered
		return 'Registration already done !'
	except FileNotFoundError:						#here it's ok	
		open(newFile,'w',newline='')
		return "Successful registration !"



def newWallet(discordID, folderName):	#add a new folder to a user's account; @param int discordID, string folderName	
	fileName = 'accounts/' + str(discordID) + '.csv'     #location of the file
	try:												 #the accounts can't have more than 3 accounts
		with open(fileName, newline='') as file:
			cpt = 0
			for tmp in csv.reader(file):
				cpt += 1
		if(cpt >= 3):
			return 'You already have three accounts.'    #this user's account already have 3 accounts
		else:
			with open(fileName,'a', newline='') as file: #if it's ok : creation of the new account
				csv.writer(file).writerow([str(cpt), folderName, 'usd-1000'])
				return 'Your new folder ' + folderName + ' has been created.'
	except FileNotFoundError:							 #if the user isn't already registered
		return 'First register yourself with the command \"$register\".'





def getWallet(discordID, name):  #return a wallet object, discordID : int, name : string
	fileName = 'accounts/' + str(discordID) + '.csv'     #location of the file
	try:
		allLines = csv.reader(open(fileName, newline=''))
		res = []
		cpt = 0
		for line in allLines:
			if len(line) >= 2 and line[1] == name:
				res = line
				break
			cpt += 1
		try:
			del res[0]
			del res[0]
		except:
			print('error, the line has a bad format')
		if cpt < 3:
			return wallet(discordID, res, cpt, name)
		else:
			return wallet(-1, res, cpt, name)
	except:
		print('error, file doesn\'t exist')	


def update(discordID, wallet):
	fileName = 'accounts/' + str(discordID) + '.csv'     #location of the file
	with open(fileName, newline='') as re:
		reader = csv.reader(re.readlines())
		with open(fileName, 'w', newline='') as wr:
			writer = csv.writer(wr)
			for line in reader:
				if line[0] == str(wallet.pos):
					tab = [str(wallet.pos), str(wallet.name)] + [str(key) + '-' + str(wallet.walletDict[key]) for key in wallet.walletDict.keys()]
					writer.writerow(tab)
					break
				else:
					writer.writerow(line)
			writer.writerows(reader)
	







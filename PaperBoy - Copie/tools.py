


def getParametres(command):  #return the parametres of a command in a String Array, @param String
	param = ''
	res = []                 #the result
	for char in command:
		if char == ' ':
			res.append(param)
			param = ''
		else:
			param += char
	res.append(param)
	del res[0]				#we delete the command's keyword
	return res


def showWallet(walletDict): #walletDict : {string:float}
	res = ''
	for key in walletDict.keys():
		res += str(walletDict[key]) + ' ' + key + ', '
	return res[:-2]







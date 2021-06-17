class wallet():
	def __init__(self, discordid, wallet, pos, name): #id : int, wallet : string list, pos : int, name : string
		self.discordID = discordid
		self.walletDict = {}
		self.pos = pos
		self.name = name
		for e in wallet:
			flag = True
			coin = ""
			value = ""
			for char in e:
				if char == '-':
					flag = False
				else:
					if flag:
						coin = coin + char
					else:
						value = value + char
			try:
				self.walletDict[coin] = float(value)
			except ValueError:
				print('error in the wallet parametre')

	def __str__(self):
		return 'wallet(' + self.name + ', ' + str(self.walletDict) + ')'

	def incCoin(self, value, name):   #the amount of the coin name is incremented by value (value can be negative), value : float, name : string
		try:
			self.walletDict[name] += value
		except:
			print('the ' + name + ' is not already in the wallet')



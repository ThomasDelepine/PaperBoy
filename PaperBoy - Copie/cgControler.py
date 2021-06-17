from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

def getPrice(fromChange, toChange):#return the price of fromChange in toChange, or an error message and a boolean, true if the pair exist, false if not. @param : fromChange, toChange : string
	try:
		cg.ping()
		coinID = ''
		for c in cg.get_coins_list():
			if c['symbol'] == fromChange:
				coinID = c['id']
				break
		if coinID == '':
			return fromChange + ' is not listed or not well written', False
		else:	
			coin = cg.get_price(ids=coinID, vs_currencies=toChange)
			if coin == {}:
				return 'error', False
			else:
				try:
					return str(coin[coinID][toChange]), True
				except:
					return 'the ' + fromChange + ' ' + toChange + ' pair doesn\'t exist', False
	except:
		return 'CoinGecko server are shut down', False




if __name__ == '__main__':


	for c in cg.get_coins_list():
			if c['symbol'] == 'nu':
				coinID = c['id']
				break
	print(coinID)
	coin = cg.get_price(ids=coinID, vs_currencies='ftx')
	print(coin)

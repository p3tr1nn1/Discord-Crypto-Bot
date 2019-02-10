import ccxt

#Return All Supported Exchanges as a List
def list_exchanges():
	exchanges = ccxt.exchanges
	return exchanges

#Return All Supported Markets from a specific exchange
def list_markets(exchange_name):
	exchange = ccxt.exchange_name()
	temp_markets = exchange.load_markets()
	markets = ""
	try:
		for i in temp_markets:
			markets = i + ','
	except:
		markets = exchange + "Exchange not Found"
	
	return markets





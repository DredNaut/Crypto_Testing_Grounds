'''
bittrex.py
Jared Knutson
Used for requesting ticker data from coinmarketcap.com
'''
import urllib2
import json
import sys
from time import strftime


# Prints the
# Modify this function to allow for all query options from this web API
# For an example of all arguments visit https://bittrex.com/api/
# Create exception handling for command line arguments
# format ltc
def bittrex_search(query):
    url = 'https://bittrex.com/api/v1.1/public/getmarketsummary?market=btc-'
    comp = query
    final_url = url + comp
    json_obj = urllib2.urlopen(final_url)
    data = json.load(json_obj)
    filename = "xchange" + strftime("%m%Y%d-%H") + ".csv"
    ledger = open(filename, 'a')

    for item in data['result']:
        string = "btc-" + query + "," + str(item['High']) + "," + str(item['Low']) + "," + item['TimeStamp'] + "\n"
        #string = item['High'] + "," + item['Low'] + "," + item['TimeStamp'] + + "\n"
        ledger.write(string)
       # print item['name'] + "\t\t$" + item['price_usd'] + "\t$" + item['market_cap_usd'] + "\t$" + item['24h_volume_usd']



ticker = ['eth','ltc','ada','xmr','etc','xem','neo','grs','iop','bcc','thc','rep','edg']
for sym in ticker:
    bittrex_search(sym)

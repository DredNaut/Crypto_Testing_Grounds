'''
coinMarketCapAPI.py
Jared Knutson
Used for requesting ticker data from coinmarketcap.com
'''
import urllib2
import json
import sys
from time import strftime


# Modify this function to allow for all query options from this web API
# For an example of all arguments visit https://coinmarketcap.com/api/
# Create exception handling for command line arguments
def coinMarketCap_search(query):
    url = 'https://api.coinmarketcap.com/v1/ticker/?limit='
    limit = query
    final_url = url + limit
    json_obj = urllib2.urlopen(final_url)
    data = json.load(json_obj)
    filename = "/home/drednaut/Programming/Python/Bittrex/Crypto_Testing_Grounds/CMCdata/CMCtop" + strftime("%m%Y%d-%H") + ".csv"
    ledger = open(filename, 'w')

    for item in data:
        string = item['name'] + "," + item['price_usd'] + "," + item['market_cap_usd'] + "," + item['24h_volume_usd'] + "," + item['last_updated'] + "\n"
        ledger.write(string)
       # print item['name'] + "\t\t$" + item['price_usd'] + "\t$" + item['market_cap_usd'] + "\t$" + item['24h_volume_usd']




limit = sys.argv[1]
coinMarketCap_search(limit)

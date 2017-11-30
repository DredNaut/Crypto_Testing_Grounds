'''
coinMarketCapAPI.py
Jared Knutson
Used for requesting ticker data from coinmarketcap.com
'''
import urllib2
import json
import sys


# Modify this function to allow for all query options from this web API
# For an example of all arguments visit https://coinmarketcap.com/api/
# Create exception handling for command line arguments
def coinMarketCap_search(query):
    url = 'https://api.coinmarketcap.com/v1/ticker/?limit='
    limit = query
    final_url = url + limit
    json_obj = urllib2.urlopen(final_url)
    data = json.load(json_obj)

    print "Name:\t\tPrice:\tMarket Cap:\t24hVolume:"
    for item in data:
        print item['name'] + "\t\t$" + item['price_usd'] + "\t$" + item['market_cap_usd'] + "\t$" + item['24h_volume_usd']


limit = sys.argv[1]
coinMarketCap_search(limit)

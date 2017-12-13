'''
shapeShiftAPI.py
Jared Knutson
Used for requesting ticker data from shapeshift.io
'''
import urllib2
import json
import sys
from time import strftime


# Modify this function to allow for all query options from this web API
# For an example of all arguments visit https://coinmarketcap.com/api/
# Create exception handling for command line arguments
def shapeShift_search(tick1,tick2):
    url = 'https://shapeshift.io/rate/'
    final_url = url + tick1 + "_" + tick2
    json_obj = urllib2.urlopen(final_url)
    data = json.load(json_obj)
    filename = "./ss" + strftime("%m%Y%d-%H") + ".csv"
    ledger = open(filename, 'w+')
    string = data['pair'] + "," + data['rate'] + "\n"
    ledger.write(string)
       # print item['name'] + "\t\t$" + item['price_usd'] + "\t$" + item['market_cap_usd'] + "\t$" + item['24h_volume_usd']




tick1 = sys.argv[1]
tick2 = sys.argv[2]
shapeShift_search(tick1,tick2)

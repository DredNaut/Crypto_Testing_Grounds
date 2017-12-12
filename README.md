# Crypto_Testing_Grounds
For Testing API's, Trading Algs, and other fun stuffs.

The file path located in the file will have to be changed to match the user's file path.

## coinMarketCap.py
#### Usage:
Used for grabbing top (n) cryptocoins based on coinmarketcap.com
```
python coinMarketCap.py <top n coins>
```

## bittrexAPI.py
#### Usage:
Used for grabbing btc->(coin) exchange rate based on bittrex.com
```
python bittrexAPI.py
```

## shapeShiftAPI.py
#### Usage:
Used for grabbing (coin)->(coin) exchange rate based on shapeshift.io
```
python shapeShiftAPI.py <coin> <coin>
```


## To-Do
#### Data Collection
- Figure out an effective way to store the data collected; ie. single csv, multiple csv's, database.
- Figure out an effective way to access that data for the analysis and backtesting stage of the program.

#### Analysis
- Compile a list of analysis algorithms into a text file.
- Create a python function for each of these algorithms in a seperate file.


#### Back Testing/ Forward Testing
- Create a simulator which allows for backtesting a particular algorithm.
- Create a simulator which will test algorithms in real-time.


#### Implementation
- Create a bot to trade using a refined and high success probability trading algorithm.
- Create an API client to allow the bot to interact with API servers; ie. Bittrex, Shapeshift
- Add an instance of machine learning to this bot to improve success and profitability probability.

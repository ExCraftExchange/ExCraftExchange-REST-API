#! /usr/bin/env python
import sys
from excraft_api_client import *



api = ExCraftApi();

#get market
result = api.get_market()
print(result)

# get last last price
result = api.get_last_price("ETHBTC")
print(result)

# get ticker
result = api.get_ticker("ETHBTC")
print(result)

# get trades
params = {
  'limit':10,
  'last_id':0
}

result = api.get_trades("ETHBTC",params)
print(result)

# get depth
params = {
  'limit':10,
}

result = api.get_depth("ETHBTC",params)
print(result)


# get kline
params = {
  'start_time':1535245066,
  'end_time':1535379166,
  'time_frame':60,
}

result = api.get_kline("ETHBTC",params)
print(result)

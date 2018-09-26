#! /usr/bin/env python
import time
from excraft_api_client import *

API_KEY = 'YOUR API KEY'
API_SECRET = 'YOUR APP SECRET'

api = ExCraftApi(API_KEY, API_SECRET)

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

# get balance
resp = api.query_balance("BTC")
print(resp)

# Put Limit Order
status, ret = api.put_limit_order("ETHBTC", 1, 1, '0.07')
print ret

# Put Market Order
status, ret = api.put_market_order("BCHBTC", 1, 1)
print ret

# Cancel Order
status, ret = api.cancel_order("ETHBTC",4286021)
print ret

# Get Pending Orders
status, ret = api.query_pending_orders("ETHBTC",0,10)
print ret

# Get Order History
start = int(time.time()) - 3600*24*100
end = int(time.time())
status, ret = api.query_history_orders("ETHBTC",start,end,0,10,1)
print ret


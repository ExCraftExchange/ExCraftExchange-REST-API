# Public REST API for ExCraft (2018-8-28)
Request address：https://www.excraft.com

*Read this in other languages: [English](README.md), [한국어](README.ko.md), [简体中文](README.zh-cn.md), [繁體中文](README.zh-hk.md).*

# Error Message：
The error message is included in the http request header<br>
grpc-status: error code<br>
grpc-message: Error details<br>
```python
code = response.headers[grpc-status]
details = response.headers[grpc-message]
```

# Variable Description：
## Direction
| Value	| Meaning |
| :-----: | :-------: |
| 1	| Sell |
| 2	| Buy |

## Order Type
| Value	| Meaning |
| :-----: | :-------: |
| 1	| Limit |
| 2	| Market |

## Order Role
| Value	| Meaning |
| :-----: | :-------: |
| 1	| Maker |
| 2	| Taker |

# K-Line Time Interval
| Value	| Meaning |
| :-----: | :-------: |
| 60	| 1 min   |
| 300	| 5 min   | 
| 900	| 15 min  |
| 1800	| 30 min  |
| 3600	| 1 hour  |
| 7200	| 2 hours |
| 14400	| 4 hours |
| 21600	| 6 hours |
| 28800	| 8 hours |
| 86400	| 1 day   |
| 604800| 1 week  |

# Public API
## 1 GetMarketList
Get supported transaction pairs<br>
/apis/trading/v1/markets<br>
Request parameters: no <br>
Request type: get<br>
Return result:<br>
```python
[
  {
    name:string;
    base:string;
    quote:string;
    fee_prec:int32;
    base_prec:int32;
    quote_prec:int32;
    base_min_size:string;
  }
]
```

## 2 GetMarketLastPrice
Get the latest market price<br>
/apis/trading/v1/markets/{market}/last_price<br>
Request parameters: no <br>
Request type: get<br>
Return result:<br>
```python
{
  price:string;
}
```

## 3 GetMarketStatusToday
获取24小时交易对状态<br>
/apis/trading/v1/markets/{market}/status_today<br>
请求参数：无<br>
请求类型：get<br>
返回结果：<br>
```python
{
  last:string;
  open:string;
  close:string;
  high:string;
  low:string;
  volume:string;
}
```

## 4 GetMarketTrades
Get recent transaction record<br>
/apis/trading/v1/markets/{market}/trades<br>
Request parameters: <br>
```python
json_encode{
  market:string;
  limit:int32;
  last_id:int32;
}
```
Request type: get<br>
Return result:<br>
```python
[
    {
      id:int32;
      timestamp:int32;
      side:int32;
      price:string;
      amount:string;
    }
]
```

## 5 GetDepth
Get the transaction pending order<br>
/apis/trading/v1/markets/{market}/depth<br>
Request parameters: <br>
```python
json_encode{
  market:string;
  limit:int32;
  merge:string;
}
```
Request type: get<br>
Return result:<br>
```python
{
  asks:[            //Sell orders
    {
      price:string;
      amount:string;
    }
  ],
  bids:[            //Buy orders
    {
      price:string;
      amount:string;
    }
  ]
}
```


## 6 GetMarketCandles
Get the transaction k-line chart<br>
/apis/trading/v1/markets/{market}/candles<br>
Request parameters: <br>
```python
json_encode{
  market:string;
  start_time:int32;
  end_time:int32;
  time_frame:int32;
}
```
Request type: get<br>
Return result:<br>
```python
[
  {
    timestamp:int32;
    open:string;
    close:string;
    high:string;
    low:string;
    volume:string;
    market:string;
  }
]
```

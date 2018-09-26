# ExCraft的公共REST API (2018-8-28)
請求地址: https://www.excraft.com

*用其他語言閱讀: [English](README.md), [한국어](README.ko.md), [简体中文](README.zh-cn.md), [繁體中文](README.zh-hk.md).*

# 錯誤信息：
錯誤信息包含在http請求頭<br>
grpc-status：錯誤碼<br>
grpc-message：錯誤詳情信息<br>
```python
code = response.headers[grpc-status]
details = response.headers[grpc-message]
```

# 變量說明：
## 方向
| 值	| 含義 |
| :-----: | :-------: |
| 1	| 賣 |
| 2	| 購買 |

## 訂單類型
| 值	| 含義 |
| :-----: | :-------: |
| 1	| 限制 |
| 2	| 市場 |

## 訂單角色
| 值	| 含義 |
| :-----: | :-------: |
| 1	| 製作者 |
| 2	| 接受者 |

# K線時間間隔
| 值 | 含義 |
| :-----: | :-------: |
| 60 | 1 分鐘 |
| 300 | 5 分鐘 |
| 900 | 15 分鐘 |
| 1800 | 30 分鐘 |
| 3600 | 1 小時 |
| 7200 | 2 小時 |
| 14400 | 4 小時 |
| 21600 | 6 小時 |
| 28800 | 8 小時 |
| 86400 | 1 天 |
| 604800| 1 週 |

# Public API
## 1 GetMarketList
獲取支持的交易對<br>
/apis/trading/v1/markets<br>
請求參數：無<br>
請求類型：get<br>
返回結果：<br>
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
獲取最近一次市場價格<br>
/apis/trading/v1/markets/{market}/last_price<br>
請求參數：無<br>
請求類型：get<br>
返回結果：<br>
```python
{
  price:string;
}
```

## 3 GetMarketStatusToday
獲取24小時交易狀態<br>
/apis/trading/v1/markets/{market}/status_today<br>
請求參數：無<br>
請求類型：get<br>
返回結果：<br>
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
獲取最近成交紀錄<br>
/apis/trading/v1/markets/{market}/trades<br>
請求參數：<br>
```python
json_encode{
  market:string;
  limit:int32;
  last_id:int32;
}
```
請求類型：get<br>
返回結果：<br>
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
獲取交易掛單<br>
/apis/trading/v1/markets/{market}/depth<br>
請求參數：<br>
```python
json_encode{
  market:string;
  limit:int32;
  merge:string;
}
```
請求類型：get<br>
返回結果：<br>
```python
{
  asks:[            //賣單
    {
      price:string;
      amount:string;
    }
  ],
  bids:[            //買單
    {
      price:string;
      amount:string;
    }
  ]
}
```


## 6 GetMarketCandles
獲取交易k線圖<br>
/apis/trading/v1/markets/{market}/candles<br>
請求參數：<br>
```python
json_encode{
  market:string;
  start_time:int32;
  end_time:int32;
  time_frame:int32;
}
```
請求類型：get<br>
返回結果：<br>
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

# Private API
## 1 QueryBalance
查詢用戶餘額<br>
/apis/trading/v1/balances<br>
請求參數: <br>
```python
assets:string;             // 空獲取所有幣種餘額;
```
請求類型: get<br>
返回結果:<br>
```python
[
  {
    assets:{                 //幣種名稱
      available:string;     // 餘額
      holds:string;         // 凍結數量
    }
  }
]
```

## 2 PutLimitOrder
限價訂單<br>
/apis/trading/v1/markets/{market}/limit_order<br>
請求參數: <br>
```python
json_encode{
  market:string;
  side:int32;     // 訂單方向
  amount:string;  // 訂單總量
  price:string;   // 訂單價格
}
```
請求類型: post<br>
返回結果:<br>
```python
{
  order:{
   id:int32;          // 訂單ID
   created_at:float;  // 時間戳，秒
   updated_at:float;  // 時間戳，秒
   market:string;     
   type:int32;        // 訂單類型
   side:int32;        // 訂單方向
   amount:string;     // 訂單總量
   price:string;      // 訂單價格
   exec_base:string;  // 執行base的數量
   exec_quote:string; // 執行quote的數量
   fee:string;        // 手續費
  }
}
```

## 3 PutMarketOrder
市價訂單<br>
/apis/trading/v1/markets/{market}/market_order<br>
請求參數: <br>
```python
json_encode{
  market:string;
  side:int32;     // 訂單方向
  amount:string;  // 訂單總量
}
```
請求類型: post<br>
返回結果:<br>
```python
{
  order:{
   id:int32;          // 訂單ID
   created_at:float;  // 時間戳，秒
   updated_at:float;  // 時間戳，秒
   market:string;     
   type:int32;        // 訂單類型
   side:int32;        // 訂單方向
   amount:string;     // 訂單總量
   price:string;      // 訂單價格
   exec_base:string;  // 執行base的數量
   exec_quote:string; // 執行quote的數量
   fee:string;        // 手續費
  }
}
```

## 4 CancelOrder
Cancel Order<br>
/apis/trading/v1/markets/{market}/orders/{order_id}/cancel<br>
請求參數: <br>
```python
json_encode{
  market:string;
  order_id:int32;   // 訂單ID
}
```
請求類型: post<br>
返回結果:<br>
```python
{
}
```

## 5 QueryPendingOrders
查詢未完成訂單<br>
/apis/trading/v1/markets/{market}/pending_orders<br>
請求參數: <br>
```python
json_encode{
  market:string;
  side:int32;     // 訂單方向
  offset:int32;
  limit:int32;  
}
```
請求類型: post<br>
返回結果:<br>
```python
{
  total:int32,        //結果總數
  limit:int32,
  offset:int32,
  order:[{
   id:int32;          // 訂單ID
   created_at:float;  // 時間戳，秒
   updated_at:float;  // 時間戳，秒
   market:string;     
   type:int32;        // 訂單類型
   side:int32;        // 訂單方向
   amount:string;     // 訂單總量
   price:string;      // 訂單價格
   exec_base:string;  // 執行base的數量
   exec_quote:string; // 執行quote的數量
   fee:string;        // 手續費
  }]
}
```

## 6 QueryFinishOrders
查詢已完成訂單<br>
/apis/trading/v1/markets/{market}/finished_orders<br>
請求參數: <br>
```python
json_encode{
  market:string;
  side:int32;     // 訂單方向
  offset:int32;
  limit:int32;
}
```
請求類型: post<br>
返回結果:<br>
```python
{
  total:int32,        //結果總數
  limit:int32,      
  offset:int32,
  order:[{
   id:int32;          // 訂單ID
   created_at:float;  // 時間戳，秒
   updated_at:float;  // 時間戳，秒
   market:string;     
   type:int32;        // 訂單類型
   side:int32;        // 訂單方向
   amount:string;     // 訂單總量
   price:string;      // 訂單價格
   exec_base:string;  // 執行base的數量
   exec_quote:string; // 執行quote的數量
   fee:string;        // 手續費
  }]
}
```

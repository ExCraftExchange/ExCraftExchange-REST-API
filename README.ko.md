# ExCraft 용 공개 Rest API (2018-8-28)
요청 주소：https://www.excraft.com

*다른 언어로 읽기: [English](README.md), [한국어](README.ko.md), [简体中文](README.zh-cn.md), [繁體中文](README.zh-hk.md).*

# 오류 메시지 :
오류 메시지가 http 요청 헤더에 포함되어 있습니다 <br>
grpc-status : 오류 코드 <br>
grpc-message : 오류 정보 <br>
```python
code = response.headers[grpc-status]
details = response.headers[grpc-message]
```

# 변수 설명 :
## 방향
| 값	| 의미 |
| :-----: | :-------: |
| 1	| 팔다 |
| 2	| 사다 |

## 주문 유형
| 값	| 의미 |
| :-----: | :-------: |
| 1	| 한도 |
| 2	| 시장 |

## 역할 주문
| 값	| 의미 |
| :-----: | :-------: |
| 1	| 만드는 사람 |
| 2	| 잡는 사람 |

# K 회선 시간 간격
| 값	| 의미 |
| :-----: | :-------: |
| 60	| 1 의미  |
| 300	| 5 의미  | 
| 900	| 15 의미 |
| 1800	| 30 의미 |
| 3600	| 1 시간  |
| 7200	| 2 시간  |
| 14400	| 4 시간  |
| 21600	| 6 시간  |
| 28800	| 8 시간  |
| 86400	| 1 일    |
| 604800| 1 주    |

# Public API
## 1 GetMarketList
지원되는 트랜잭션 쌍 가져 오기 <br>
/apis/trading/v1/markets<br>
요청 매개 변수 : 없음 <br>
요청 유형 : get <br>
결과를 반환 : <br>
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
최신 시장 가격보기 <br>
/apis/trading/v1/markets/{market}/last_price<br>
요청 매개 변수 : 없음 <br>
요청 유형 : get <br>
결과를 반환 : <br>
```python
{
  price:string;
}
```
## 3 GetMarketStatusToday
24 시간 경과 상태<br>
/apis/trading/v1/markets/{market}/status_today<br>
요청 매개 변수 ：없음 <br>
요청 유형 ：get<br>
결과를 반환 ：<br>
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

## 3 GetMarketTrades
최근 거래 기록 가져 오기 <br>
/apis/trading/v1/markets/{market}/trades<br>
요청 매개 변수 : <br>
```python
json_encode{
  market:string;
  limit:int32;
  last_id:int32;
}
```
요청 유형 : get <br>
결과를 반환 : <br>
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

## 4 GetDepth
거래 보류 명령 받기 <br>
/apis/trading/v1/markets/{market}/depth<br>
요청 매개 변수 : <br>
```python
json_encode{
  market:string;
  limit:int32;
  merge:string;
}
```
요청 유형 : get <br>
결과를 반환 : <br>
```python
{
  asks:[            //주문 판매
    {
      price:string;
      amount:string;
    }
  ],
  bids:[            //주문 주문
    {
      price:string;
      amount:string;
    }
  ]
}
```


## 5 GetMarketCandles
거래 k 라인 차트 가져 오기 <br>
/apis/trading/v1/markets/{market}/candles<br>
요청 매개 변수 : <br>
```python
json_encode{
  market:string;
  start_time:int32;
  end_time:int32;
  time_frame:int32;
}
```
요청 유형 : get <br>
결과를 반환 : <br>
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

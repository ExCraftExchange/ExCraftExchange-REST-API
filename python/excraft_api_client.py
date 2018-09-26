# coding=utf-8
import requests
from requests import exceptions
import json
import base
import logging
import urllib3
import hashlib
import hmac

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
logger = logging.getLogger('excraft')

API_HOST = "https://www.excraft.com"
#public
MARKET_URL = API_HOST + '/apis/trading/v1/markets'
LAST_PRICE_URL = API_HOST + '/apis/trading/v1/markets/{market}/last_price'
TICKER_URL = API_HOST + '/apis/trading/v1/markets/{market}/status_today'
TRADE_URL = API_HOST + '/apis/trading/v1/markets/{market}/trades'
DEPTH_URL = API_HOST + '/apis/trading/v1/markets/{market}/depth'
KLINE_URL = API_HOST + '/apis/trading/v1/markets/{market}/candles'

#private
BALANCE_URL = API_HOST + "/apis/trading/v1/balances"
PUT_LIMIT_ORDER = API_HOST + "/apis/trading/v1/markets/{market}/limit_order"
PUT_MARKET_ORDER = API_HOST + "/apis/trading/v1/markets/{market}/market_order"
CANCEL_ORDER = API_HOST + "/apis/trading/v1/markets/{market}/orders/{order_id}/cancel"
PENDING_ORDERS = API_HOST + "/apis/trading/v1/markets/{market}/pending_orders"
FINISHED_ORDERS = API_HOST + "/apis/trading/v1/markets/{market}/finished_orders"


class ExCraftApi:
    def __init__(self,app_key,app_secret):
        self.APP_KEY = app_key
        self.APP_SECRET = app_secret

    def api_call(self, url='', method='GET', sign=None, headers=None, params=None):
        if sign is not None:
            headers = {
                "app_key": self.APP_KEY,
                "sign": sign
            }

        try:
            if method == 'GET':
                if params is not None:
                    resp = requests.request("GET", url=url, headers=headers, params=params, timeout=10)
                else:
                    resp = requests.request("GET", url=url, headers=headers, timeout=10)
            elif method == 'POST':
                if params is not None:
                    resp = requests.request("POST", url=url, headers=headers, json=params, timeout=10)
                else:
                    resp = requests.request("POST", url=url, headers=headers, timeout=10)
        except exceptions.Timeout as e:
            logger.info(url + ' request timeout：' + str(e.message))
            return None, base.HTTPError(e)
        except exceptions.HTTPError as e:
            return None, base.HTTPError(e)
        return resp, None


    def get_market(self):
        resp, err = self.api_call(url=MARKET_URL)
        if resp.status_code != 200:
            return resp.headers["grpc-status"], resp.headers["grpc-message"]
        return 0, resp.json()

    def get_last_price(self, market):
        url = self.format_url(LAST_PRICE_URL, {"market": market})
        resp, err = self.api_call(url=url)
        if resp.status_code != 200:
            return resp.headers["grpc-status"], resp.headers["grpc-message"]
        return 0, resp.json()

    def get_ticker(self, market):
        url = self.format_url(TICKER_URL, {"market": market})
        resp, err = self.api_call(url=url)
        if resp.status_code != 200:
            return resp.headers["grpc-status"], resp.headers["grpc-message"]
        return 0, resp.json()

    def get_trades(self, market, params):
        url = self.format_url(TRADE_URL, {"market": market})
        resp, err = self.api_call(url=url)
        if resp.status_code != 200:
            return resp.headers["grpc-status"], resp.headers["grpc-message"]
        return 0, resp.json()

    def get_depth(self, market, params):
        url = self.format_url(DEPTH_URL, {"market": market})
        resp, err = self.api_call(url=url, params=params)
        if resp.status_code != 200:
            return resp.headers["grpc-status"], resp.headers["grpc-message"]
        return 0, resp.json()

    def get_kline(self, market, params):
        url = self.format_url(KLINE_URL, {"market": market})
        resp, err = self.api_call(url=url, params=params)
        if resp.status_code != 200:
            return resp.headers["grpc-status"], resp.headers["grpc-message"]
        return 0, resp.json()

    def query_balance(self, assets=None):
        if assets is not None:
            plaint = "assets=" + assets + "&app_key=" + self.APP_KEY
            params = {
                "assets":assets,
            }
        else:
            plaint = "app_key=" + self.APP_KEY
            params = None

        sign = self.get_sign(plaint)

        resp, err = self.api_call(url=BALANCE_URL, method="GET", params=params, sign=sign)

        if resp.status_code != 200:
            return resp.headers["grpc-status"], resp.headers["grpc-message"]

        return 0, resp.json()

    def put_limit_order(self, market, side, amount, price):
        plaint = "market=" + market + "&side=" + str(side) + "&amount=" + str(amount) + "&price=" + price \
                 + "&app_key=" + self.APP_KEY
        sign = self.get_sign(plaint)
        params = {
            "market": market,
            "side": side,
            "amount": str(amount),
            "price": price,
        }

        url = self.format_url(PUT_LIMIT_ORDER, {"market": market})
        resp, err = self.api_call(url=url, method="POST", params=params, sign=sign)

        if resp.status_code != 200:
            return resp.headers["grpc-status"], resp.headers["grpc-message"]

        return 0, resp.json()

    def put_market_order(self, market, side, amount):
        plaint = "market=" + market + "&side=" + str(side) + "&amount=" + str(amount) \
                 + "&app_key=" + self.APP_KEY
        sign = self.get_sign(plaint)
        params = {
            "market": market,
            "side": side,
            "amount": str(amount),
        }

        url = self.format_url(PUT_MARKET_ORDER, {"market": market})
        resp, err = self.api_call(url=url, method="POST", params=params, sign=sign)

        if resp.status_code != 200:
            return resp.headers["grpc-status"], resp.headers["grpc-message"]
        return 0, resp.json()

    def cancel_order(self, market, order_id):
        plaint = "market=" + market + "&order_id=" + str(order_id)\
                 + "&app_key=" + self.APP_KEY
        sign = self.get_sign(plaint)
        params = {
            "market": market,
            "order_id": order_id,
        }

        url = self.format_url(CANCEL_ORDER, {"market": market,"order_id":order_id})
        resp, err = self.api_call(url=url, method="POST", params=params, sign=sign)

        if resp.status_code != 200:
            return resp.headers["grpc-status"], resp.headers["grpc-message"]

        return 0, resp.json()

    def query_pending_orders(self, market, offset, limit):
        plaint = "market=" + market + "&offset=" + str(offset) + "&limit=" + str(limit) \
                 + "&app_key=" + self.APP_KEY
        sign = self.get_sign(plaint)
        params = {
            "market": market,
            "offset": offset,
            "limit": limit,
        }

        url = self.format_url(PENDING_ORDERS, {"market": market})
        resp, err = self.api_call(url=url, method="GET", params=params, sign=sign)

        if resp.status_code != 200:
            return resp.headers["grpc-status"], resp.headers["grpc-message"]

        return 0, resp.json()

    def query_history_orders(self, market, start_time, end_time, offset, limit, side):
        plaint = "market=" + market + "&start_time=" + str(start_time) + "&end_time=" + str(end_time) + "&offset=" + \
                 str(offset) + "&limit=" + str(limit) + "&side=" + str(side) + "&app_key=" + self.APP_KEY
        sign = self.get_sign(plaint)
        params = {
            "market": market,
            "start_time": start_time,
            "end_time": end_time,
            "offset": offset,
            "limit": limit,
            "side": side,
        }

        url = self.format_url(FINISHED_ORDERS, {"market": market})
        resp, err = self.api_call(url=url, method="GET", params=params, sign=sign)

        if resp.status_code != 200:
            return resp.headers["grpc-status"], resp.headers["grpc-message"]

        return 0, resp.json()

    def get_sign(self, params):
        m = hmac.new(self.APP_SECRET, params, digestmod=hashlib.sha256)
        return m.hexdigest()

    def format_url(self, url, dic):
        for key, value in dic.iteritems():
            new_url = url.replace("{" + key + "}",str(value))
            url = new_url
        return url
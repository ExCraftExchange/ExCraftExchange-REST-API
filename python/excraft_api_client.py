# coding=utf-8
import requests
from requests import exceptions
import json
import base
import logging
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
logger = logging.getLogger('excraft')


class ExCraftApi:
    HTTP_HOST = "https://www.excraft.com"

    def api_call(self, url='', method='GET', headers=None, params=None):
        try:
            if method == 'GET':
                resp = requests.get(url, headers=headers, params=params, timeout=20, verify=False)
            elif method == 'POST':
                resp = requests.get(url, headers=headers, data=json.dumps(params), timeout=20, verify=False)
        except exceptions.Timeout as e:
            logger.info(url + ' request timeout：' + str(e.message))
            return None, base.HTTPError(e)
        except exceptions.HTTPError as e:
            return None, base.HTTPError(e)
        return resp, None

    def get_market(self):
        ret, err = self.api_call(url=self.HTTP_HOST + '/apis/trading/v1/markets')
        if err is None:
            return ret.json()

    def get_last_price(self, market):
        ret, err = self.api_call(url=self.HTTP_HOST + '/apis/trading/v1/markets/' + market + '/last_price')
        if err is None:
            return ret.json()

    def get_ticker(self, market):
        ret, err = self.api_call(url=self.HTTP_HOST + '/apis/trading/v1/markets/' + market + '/status_today')
        if err is None:
            return ret.json()

    def get_trades(self, market, params):
        ret, err = self.api_call(url=self.HTTP_HOST + '/apis/trading/v1/markets/' + market + '/trades')
        if err is None:
            return ret.json()

    def get_depth(self, market, params):
        ret, err = self.api_call(url=self.HTTP_HOST + '/apis/trading/v1/markets/' + market + '/depth', params=params)
        if err is None:
            return ret.json()

    def get_kline(self, market, params):
        ret, err = self.api_call(url=self.HTTP_HOST + '/apis/trading/v1/markets/' + market + '/candles', params=params)
        if err is None:
            return ret.json()
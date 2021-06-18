"""
Python wrapper for cryptocompare API
"""

import requests
import time
import quo
import datetime
import typing
import os
from typing import Union, Optional, List, Dict
from .formatter import _format_parameter
from .formatter import _format_timestamp
from .formatter import _set_api_key_parameter
from .query_cryptocompare import _query_cryptocompare
from .coinlist import coin_list
from .getaverage import get_average
from .getexchanges import get_exchanges 
from .getpairs import get_pairs
from .pricedifference import get_price
from .pricedifference import price
from .pricedifference import price_day
from .pricedifference import price_hour
from .pricedifference import price_minute

Timestamp = Union[datetime.datetime, datetime.date, int, float]

# API
_API_KEY_PARAMETER = ""
_URL_COIN_LIST = 'https://www.cryptocompare.com/api/data/coinlist?'
_URL_PRICE = 'https://min-api.cryptocompare.com/data/pricemulti?fsyms={}&tsyms={}'
_URL_PRICE_MULTI = 'https://min-api.cryptocompare.com/data/pricemulti?fsyms={}&tsyms={}'
_URL_PRICE_MULTI_FULL = 'https://min-api.cryptocompare.com/data/pricemultifull?fsyms={}&tsyms={}'
_URL_HIST_PRICE = 'https://min-api.cryptocompare.com/data/pricehistorical?fsym={}&tsyms={}&ts={}&e={}'
_URL_HIST_PRICE_DAY = 'https://min-api.cryptocompare.com/data/histoday?fsym={}&tsym={}&limit={}&e={}&toTs={}'
_URL_HIST_PRICE_HOUR = 'https://min-api.cryptocompare.com/data/histohour?fsym={}&tsym={}&limit={}&e={}&toTs={}'
_URL_HIST_PRICE_MINUTE = 'https://min-api.cryptocompare.com/data/histominute?fsym={}&tsym={}&limit={}&e={}&toTs={}'
_URL_AVG = 'https://min-api.cryptocompare.com/data/generateAvg?fsym={}&tsym={}&e={}'
_URL_EXCHANGES = 'https://www.cryptocompare.com/api/data/exchanges?'
_URL_PAIRS = 'https://min-api.cryptocompare.com/data/pair/mapping/exchange?e={}'

# DEFAULTS
CURRENCY = 'USD'
LIMIT = 1440
###############################################################################




__version__ = "1.0.2" 

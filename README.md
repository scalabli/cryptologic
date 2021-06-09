# cryptologic
 ![GitHub Workflow Status (branch)](https://img.shields.io/github/workflow/status/lagerfeuer/cryptocompare/Test/master) [![Coverage Status](https://coveralls.io/repos/github/lagerfeuer/cryptocompare/badge.svg?branch=master)](https://coveralls.io/github/lagerfeuer/cryptocompare?branch=master) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/cryptologic) [![PyPI version](https://badge.fury.io/py/cryptologic.svg)](https://badge.fury.io/py/cryptologic) [![Requirements Status](https://requires.io/github/lagerfeuer/cryptocompare/requirements.svg?branch=master)](https://requires.io/github/lagerfeuer/cryptocompare/requirements/?branch=master)


Python3 wrapper to query cryptocurrency prices (and more) using the [CryptoCompare](https://min-api.cryptocompare.com/) API.


## Install
```sh
pip install cryptologic
```

## Usage

```python
import cryptologic
```

## API Key

If you have an API key, you can either set it as environment variable `CRYPTOCOMPARE_API_KEY` or set it manually with: 

```
cryptologic.cryptologic._set_api_key_parameter(KEY_HERE)
```

### Coin List

```python
cryptologic.coin_list(format=False)
# ...
# },
# 'BTC': {
#  'Id': '1182'
#  'Url': '/coins/btc/overview'
#  'ImageUrl': '/media/19633/btc.png'
#  'Name': 'BTC'
#  'CoinName': 'Bitcoin'
#  'FullName': 'Bitcoin (BTC)'
#  'Algorithm': 'SHA256'
#  'ProofType': 'PoW'
#  'FullyPremined': '0'
#  'TotalCoinSupply': '21000000'
#  'PreMinedValue': 'N/A'
#  'TotalCoinsFreeFloat': 'N/A'
#  'SortOrder': '1'
# },
# ...
```

If `format` is `True`, the coin list is returned as Python list,
containing only the abbreviations (like `BTC`).

### Price

```python
cryptologic.get_price('BTC')
# or
cryptologic.get_price('BTC', currency='USD', full=True)
# or
cryptologic.get_price(['BTC', 'ETH'], ['EUR', 'GBP'])

# {'BTC': {'EUR': 3709.04, 'GBP': 3354.78},
#  'ETH': {'EUR': 258.1, 'GBP': 241.25}}
```

### Historical Prices

```python
# pass either datetime or time instance
cryptologic.price('XMR', timestamp=datetime.datetime(2017,6,6), exchange='CCCAGG')
# or
cryptologic.price('XMR', 'EUR', datetime.datetime(2017,6,6))

# {'XMR': {'EUR': 43.05}}
```

#### Day

```python
cryptologic.price_day('BTC', currency='EUR')
cryptologic.price_day('BTC', currency='EUR', limit=30)
cryptologic.price_day('BTC', 'EUR', limit=24, exchange='CCCAGG', toTs=datetime.datetime(2019,6,6))
# or
cryptologic.price_day('BTC', 'EUR', limit=24, exchange='CCCAGG', toTs=datetime.datetime(1559815200))
```

#### Hour

```python
cryptologic.price_hour('BTC', currency='USD')
cryptologic.price_hour('BTC', currency='EUR', limit=24)
cryptologic.price_hour('BTC', 'EUR', limit=24, exchange='CCCAGG')
cryptologic.price_hour('BTC', 'EUR', limit=24, exchange='CCCAGG', toTs=datetime.datetime(2019,6,6,12))
# or
cryptologic.price_hour('BTC', 'EUR', limit=24, exchange='CCCAGG', toTs=datetime.datetime(1559815200))
```

#### Minute

```python
cryptologic.price_minute('BTC', currency='EUR')
cryptologic.price_minute('BTC', currency='EUR', limit=1440)
cryptologic.price_minute('BTC', 'EUR', limit=24, exchange='CCCAGG', toTs=datetime.datetime.now())
```

### Average

```python
cryptologic.get_average('BTC', currency='EUR', exchange='Kraken')
# {
# 'MARKET': 'CUSTOMAGG',
# 'FROMSYMBOL': 'BTC',
# 'TOSYMBOL': 'EUR',
# 'FLAGS': 0,
# 'PRICE': 3610,
# 'LASTUPDATE': 1503066719,
# 'LASTVOLUME': 0.5,
# 'LASTVOLUMETO': 1805,
# 'LASTTRADEID': 1503066719.7584,
# 'VOLUME24HOUR': 12614.509997469995,
# 'VOLUME24HOURTO': 46397723.00499387,
# 'OPEN24HOUR': 3847.9,
# 'HIGH24HOUR': 3848.96,
# 'LOW24HOUR': 3555,
# 'LASTMARKET': 'Kraken',
# 'CHANGE24HOUR': -237.9000000000001,
# 'CHANGEPCT24HOUR': -6.182593102731363
# }
```

### Exchanges

```python
cryptologic.get_exchanges()
```

### Pairs

```python
cryptologic.get_pairs()
pairs = cryptologic.get_pairs(exchange='Kraken')
```

## Developing

Tests run assuming you have an API key, otherwise they will error due to rate limiting. Install the dev dependencies and run the tests:
```sh
pip3 install -r requirements.txt
python3 -m pytest
```

## Credit

* The [CryptoCompare API](https://min-api.cryptocompare.com/).


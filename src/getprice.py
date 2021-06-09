def get_price(coin: str, currency: str = CURRENCY, full: bool = False) -> Optional[Dict]:
    """
    Get the current price of a coin in a given currency.

    :param coin: symbolic name of the coin (e.g. BTC)
    :param currency: short hand description of the currency (e.g. EUR)
    :param full: full response or just the price (default: False)
    :returns: dict of coin and currency price pairs
    """
    if full:
        return _query_cryptocompare(
            _URL_PRICE_MULTI_FULL.format(
                _format_parameter(coin), _format_parameter(currency))
        )
    if isinstance(coin, list):
        return _query_cryptocompare(
            _URL_PRICE_MULTI.format(_format_parameter(coin),
                                    _format_parameter(currency))
        )
    return _query_cryptocompare(
        _URL_PRICE.format(coin, _format_parameter(currency))
    )
